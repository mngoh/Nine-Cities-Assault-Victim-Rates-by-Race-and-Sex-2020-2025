"""Run every city through the kit at once, one process per city.

Needs data/interim/victim_offenses.csv (nibrs.py flatten, all five ORIs) and <city>/analysis.json (make_configs.py).
For each city, in parallel: its rows of the flat file, the audit, the NIBRS victim files, ACS denominators, then the
tests. Each city's log goes to <city>/out/run.log.

  python scripts/run_cities.py                 # all cities
  python scripts/run_cities.py houston el_paso # some
"""
import concurrent.futures as cf
import json
import os
import pathlib
import subprocess
import sys

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = pathlib.Path(os.path.expanduser(os.environ.get("DISPARITY_KIT", "~/.claude/disparity-kit/kit")))
PY = sys.executable


def run(city):
    cfg = json.loads((ROOT / city / "analysis.json").read_text())
    rows = ROOT / f"data/interim/victim_offenses_{city}.csv"
    steps = [
        [PY, KIT / "audit.py", rows, "--code", "offense_code", "--desc", "offense_name", "--id", "victim_id", "--date", "incident_date", "--out", ROOT / city / "out/audit_nibrs.md"],
        [PY, KIT / "nibrs.py", "victims", rows, "--ori", cfg["_ori"], "--kind", "aggravated=13A", "--kind", "simple=13B", "--race-rule", "hispanic-first",
         "--out-dir", ROOT / city / "data", "--prefix", f"{city}_"],
        [PY, KIT / "denominators.py", ROOT / city / "analysis.json"],
        [PY, KIT / "analyze.py", ROOT / city / "analysis.json"],
    ]
    (ROOT / city / "out").mkdir(parents=True, exist_ok=True)
    with open(ROOT / city / "out/run.log", "w") as log:
        for s in steps:
            subprocess.run([str(a) for a in s], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    return city, (ROOT / city / "out/run.log").read_text().strip().splitlines()[-1]


def main():
    cities = sys.argv[1:] or sorted(p.parent.name for p in ROOT.glob("*/analysis.json"))
    flat = pd.read_csv(ROOT / "data/interim/victim_offenses.csv", low_memory=False, dtype=str)
    for c in cities:
        ori = json.loads((ROOT / c / "analysis.json").read_text())["_ori"]
        flat[flat["ori"] == ori].to_csv(ROOT / f"data/interim/victim_offenses_{c}.csv", index=False)
    with cf.ProcessPoolExecutor(max_workers=len(cities)) as ex:
        for city, last in ex.map(run, cities):
            print(f"{city}: {last}")


if __name__ == "__main__":
    main()
