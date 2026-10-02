"""Nine cities side by side: the five Texas cities run here, and LA, DC, Baltimore and Dallas from their own projects.

For every city, from that city's outputs: Black women's rate and the ratio to Hispanic, White and Asian women; a range
for the Hispanic and White ratios that spans the race-coding worst case and the ethnicity scenarios (White-race women
with unknown ethnicity left as White, left out, split in the known proportion, or all Hispanic); age-standardized
ratios; aggravated against simple assault; partner assault share and the ratios with and without it; women's rate
against men's by group; the first half of the window against the second; the adjusted ratio where a tract model ran.

Sources differ: LA uses LAPD's pre-NIBRS records (2020 to 2023) and Baltimore its legacy file (2022 to 2024); DC, Dallas
and the five Texas cities use the FBI's NIBRS files. Compare patterns, not levels.

  python scripts/compare.py      ->  out/comparison.json, out/comparison.md
"""
import json
import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
GIT = ROOT.parent
TEXAS = ["houston", "san_antonio", "austin", "fort_worth", "el_paso"]
OTHERS = ["Hispanic", "White", "Asian"]
LA_COMBO = 1.24  # LA-Crime README: 24% more people are Black alone or in combination than Black alone
PARTNER = {"SE", "CS", "BG", "HR", "XS", "XR"}


def rnd(v, n=2):
    return None if v is None else round(v, n)


def ethnicity_scenarios(cfg_dir, R):
    """White-race women with unknown ethnicity, moved the four ways, for a kit NIBRS project."""
    cfg = json.loads((cfg_dir / "analysis.json").read_text())
    pop = json.loads((cfg_dir / "out/population.json").read_text())["city"]
    raw = pd.concat([pd.read_csv(cfg_dir / s["path"], dtype=str) for s in cfg["incidents"]])
    raw = raw[(raw["incident_date"] >= cfg["window"]["start"]) & (raw["incident_date"] <= cfg["window"]["end"])]
    w = raw[raw["sex"] == "F"]
    yrs = R["years"]
    rate = lambda n, g: round(n / pop[g]["F"] / yrs * 1e5)
    n = {g: int((w["race_group"].map(cfg["race_map"]) == g).sum()) for g in cfg["groups"]}
    wr = w[w["race"] == "W"]
    h, nn, u = int((wr["ethnicity"] == "H").sum()), int((wr["ethnicity"] == "N").sum()), int(wr["ethnicity"].isin(["U", "X"]).sum())
    sh = h / (h + nn) if h + nn else 0
    scen = {"as mapped": (n["Hispanic"], n["White"]), "unknown ethnicity left out": (n["Hispanic"], n["White"] - u),
            "split in known proportion": (n["Hispanic"] + sh * u, n["White"] - sh * u), "all Hispanic": (n["Hispanic"] + u, n["White"] - u)}
    fr = rate(n["Black"], "Black")
    out = {k: {"Hispanic": rnd(fr / rate(a, "Hispanic")), "White": rnd(fr / rate(b, "White"))} for k, (a, b) in scen.items()}
    rel = w["relationship"].fillna("").str.split(";").apply(set)
    g = w["race_group"].map(cfg["race_map"])
    rel_unk = {k: round(float(v.mean() * 100), 1) for k, v in rel.apply(lambda s: s <= {"RU", ""}).groupby(g)}
    return out, {"white_unknown_ethnicity": u, "eth_unknown_pct_women": round(float(w["ethnicity"].isin(["U", "X"]).mean() * 100), 1)}, rel_unk, n


def from_kit(name, src, cfg_dir, checks=None, model_note=None):
    R = json.loads((cfg_dir / "out/results.json").read_text())
    cfg = json.loads((cfg_dir / "analysis.json").read_text())
    t = R["tests"]
    rates = {g: R["rates"][g]["F"] for g in R["rates"]}
    if checks is not None:
        scen = checks["ethnicity"]["scenarios"]
        eth = {"eth_unknown_pct_women": checks["ethnicity"].get("all_unknown_ethnicity_pct")}
        rel_unk = checks.get("relationship_unknown_pct")
        n = None
    else:
        scen, eth, rel_unk, n = ethnicity_scenarios(cfg_dir, R)
    std = t["age"]["standardized"]
    fl = t.get("flags", {}).get("partner")
    time = t["time"]
    ys = sorted(time)
    half = lambda part: {g: rnd(sum(time[y]["Black"] for y in part) / sum(time[y][g] for y in part)) for g in OTHERS}
    m = R.get("model")
    worst = R["race_coding_bound"]["ratios_worst_case"]
    row = {
        "city": name, "source": src, "window": f"{cfg['window']['start'][:4]} to {cfg['window']['end'][:4]}",
        "black_women_rate": rates["Black"], "rates_women": rates, "black_men_rate": R["rates"]["Black"]["M"],
        "ratio": R["ratios"],
        "range": {g: [min([R["ratios"][g], worst[g]] + [v[g] for v in scen.values()]), max([R["ratios"][g], worst[g]] + [v[g] for v in scen.values()])] for g in ("Hispanic", "White")},
        "race_coding_worst": worst, "ethnicity_scenarios": scen, **eth,
        "age_standardized": {g: rnd(std["Black"] / std[g]) for g in OTHERS if std.get(g)},
        "aggravated": {g: rnd(t["type"]["aggravated"]["Black"] / t["type"]["aggravated"][g]) for g in OTHERS},
        "simple": {g: rnd(t["type"]["simple"]["Black"] / t["type"]["simple"][g]) for g in OTHERS},
        "partner_share": fl["share"] if fl else None,
        "partner_ratio": fl["ratios"]["flagged"] if fl else None, "non_partner_ratio": fl["ratios"]["unflagged"] if fl else None,
        "relationship_unknown_pct": rel_unk,
        "women_over_men": R["ratio_to_other_sex"],
        "halves": {"years": [ys[:len(ys) // 2], ys[len(ys) // 2:]], "first": half(ys[:len(ys) // 2]), "second": half(ys[len(ys) // 2:])},
        "women_victims": n or {g: None for g in R["groups"]},
        "adjusted": {g: m["pairwise"][g]["adjusted"]["rate_ratio"] for g in OTHERS} if m else None,
        "adjusted_note": model_note if m else None,
        "black_women_pop": json.loads((cfg_dir / "out/population.json").read_text())["city"]["Black"]["F"],
    }
    return row


def la_row():
    d = GIT / "LA-Crime/data"
    p, m, nb = (json.loads((d / f).read_text()) for f in ("page_data.json", "model_results.json", "nibrs_comparison.json"))
    rates = {g: p["rates"][g]["F"] for g in p["rates"]}
    ratio = {g: rnd(rates["Black"] / rates[g]) for g in OTHERS}
    worst = {g: rnd(ratio[g] / LA_COMBO) for g in OTHERS}
    std = p["tests"]["age"]["standardized"]
    ty, time = p["tests"]["type"], p["tests"]["time"]
    ys = sorted(time)
    half = lambda part: {g: rnd(sum(time[y]["Black"] for y in part) / sum(time[y][g] for y in part)) for g in OTHERS}
    return {"city": "Los Angeles", "source": "LAPD records (pre-NIBRS)", "window": "2020 to 2023",
            "black_women_rate": rates["Black"], "rates_women": rates, "black_men_rate": p["rates"]["Black"]["M"],
            "ratio": ratio, "range": {g: [min(ratio[g], worst[g]), max(ratio[g], worst[g])] for g in ("Hispanic", "White")},
            "race_coding_worst": worst, "ethnicity_scenarios": None, "eth_unknown_pct_women": None,
            "age_standardized": {g: rnd(std["Black"] / std[g]) for g in OTHERS},
            "aggravated": {g: rnd(ty["aggravated"]["Black"] / ty["aggravated"][g]) for g in OTHERS},
            "simple": {g: rnd(ty["simple"]["Black"] / ty["simple"][g]) for g in OTHERS},
            "partner_share": nb["intimate_share"]["legacy"], "partner_ratio": nb["ratios"]["legacy"]["intimate"],
            "non_partner_ratio": nb["ratios"]["legacy"]["general"], "relationship_unknown_pct": None,
            "women_over_men": {g: p["rates"][g]["ratio"] for g in p["rates"]},
            "halves": {"years": [ys[:2], ys[2:]], "first": half(ys[:2]), "second": half(ys[2:])},
            "women_victims": {g: p["counts"]["race_sex_all"][g]["F"] for g in p["counts"]["race_sex_all"]},
            "adjusted": {g: m["pairwise"][g]["adjusted"]["rate_ratio"] for g in OTHERS}, "adjusted_note": "all assaults, tract model",
            "black_women_pop": p["rates"]["Black"]["popF"]}


def main():
    rows = [la_row()]
    rows.append(from_kit("DC", "FBI NIBRS", GIT / "DC-Assault", json.loads((GIT / "DC-Assault/out/dc_checks.json").read_text())))
    rows.append(from_kit("Baltimore", "BPD legacy records", GIT / "Baltimore-Assault-Victims",
                         json.loads((GIT / "Baltimore-Assault-Victims/out/baltimore_checks.json").read_text()), "all assaults, tract model"))
    dal = GIT / "Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025"
    d = from_kit("Dallas", "FBI NIBRS", dal, json.loads((dal / "out/dallas_checks.json").read_text()))
    cm = json.loads((dal / "city/out/results.json").read_text())["model"]
    d["adjusted"] = {g: cm["pairwise"][g]["adjusted"]["rate_ratio"] for g in OTHERS}
    d["adjusted_note"] = "non-family assaults on adults only (city file), tract model"
    raw = pd.concat([pd.read_csv(dal / s, dtype=str) for s in ("data/dallas_simple.csv", "data/dallas_aggravated.csv")])
    w = raw[raw["sex"] == "F"]
    d["women_victims"] = {g: int((w["race_group"] == c).sum()) for g, c in (("Black", "B"), ("Hispanic", "H"), ("White", "W"), ("Asian", "A"))}
    rows.append(d)
    names = {"houston": "Houston", "san_antonio": "San Antonio", "austin": "Austin", "fort_worth": "Fort Worth", "el_paso": "El Paso"}
    for c in TEXAS:
        rows.append(from_kit(names[c], "FBI NIBRS", ROOT / c))
    (ROOT / "out/comparison.json").write_text(json.dumps(rows, indent=1) + "\n")

    f = lambda v: "n/a" if v is None else (f"{v:,}" if isinstance(v, int) else f"{v}")
    rng = lambda r: f"{r[0]} to {r[1]}" if r[0] != r[1] else f"{r[0]}"
    L = ["# Nine cities: Black women's reported assault rate against other women's", "",
         "Women victims of aggravated and simple assault reported to police, per 100,000 residents a year. Generated by `scripts/compare.py` from each city's outputs.", "",
         "| City | Source, years | Black women | vs Hispanic | vs White | vs Asian | Range vs Hispanic | Range vs White | Age-standardized vs White | Aggravated / simple vs White | Adjusted (tract model) vs Hispanic, White |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        adj = f"{r['adjusted']['Hispanic']}, {r['adjusted']['White']}" if r["adjusted"] else "n/a"
        L.append(f"| {r['city']} | {r['source']}, {r['window']} | {r['black_women_rate']:,} | {r['ratio']['Hispanic']} | {r['ratio']['White']} | {r['ratio']['Asian']} | "
                 f"{rng(r['range']['Hispanic'])} | {rng(r['range']['White'])} | {r['age_standardized']['White']} | {r['aggravated']['White']} / {r['simple']['White']} | {adj} |")
    L += ["", "| City | Women's rate: Black, Hispanic, White, Asian | Black women / Black men | Partner share, Black women vs others | vs Hispanic with / without partner | Halves vs Hispanic | Halves vs White | Black women victims | Asian women victims |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        rw = r["rates_women"]
        ps = r["partner_share"]
        share = f"{ps['Black']}% vs {min(ps[g] for g in OTHERS)}% to {max(ps[g] for g in OTHERS)}%" if ps else "n/a"
        pr = f"{r['partner_ratio']['Hispanic']} / {r['non_partner_ratio']['Hispanic']}" if r["partner_ratio"] else "n/a"
        h = r["halves"]
        L.append(f"| {r['city']} | {rw['Black']:,}, {rw['Hispanic']:,}, {rw['White']:,}, {rw['Asian']:,} | {r['women_over_men']['Black']} | {share} | {pr} | "
                 f"{h['first']['Hispanic']} then {h['second']['Hispanic']} | {h['first']['White']} then {h['second']['White']} | {f(r['women_victims'].get('Black'))} | {f(r['women_victims'].get('Asian'))} |")
    L += ["", "Ranges span the race-coding worst case (multiracial residents counted as Black) and the ethnicity scenarios. Adjusted ratios come from tract-level Poisson models (age, year, police district, tract socioeconomics); "
          "Dallas's covers only the city file's non-family assaults on adults, and DC and the other Texas cities have no victim locations. Sources differ by city, so compare patterns, not levels."]
    (ROOT / "out/comparison.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
