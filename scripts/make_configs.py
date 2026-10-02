"""Write one analysis.json per city, all with the Dallas decisions, so the cities are measured the same way.

Source: the FBI's NIBRS state files for Texas, 2022 to 2025 (data/raw/TX-<year>.zip). Each city is its own police
department only. Aggravated (13A) and simple (13B) assault, individual victims of any age; officers, intimidation and
homicide are out. Hispanic of any race first, otherwise the recorded race. Partner flag from the victim-offender
relationship. Black women against Hispanic, White and Asian women. Window January 2022 to December 2025.

  python scripts/make_configs.py      ->  <city>/analysis.json for each city below
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CITIES = {  # slug: (name, ORI, Census place)
    "houston": ("Houston", "TXHPD0000", "16000US4835000"),
    "san_antonio": ("San Antonio", "TXSPD0000", "16000US4865000"),
    "austin": ("Austin", "TX2270100", "16000US4805000"),
    "fort_worth": ("Fort Worth", "TX2201200", "16000US4827000"),
    "el_paso": ("El Paso", "TX0710200", "16000US4824000"),
}
WEAPONS = [{"label": "Firearm", "keywords": ["FIREARM", "HANDGUN", "RIFLE", "SHOTGUN"]},
           {"label": "Knife or cutting", "keywords": ["KNIFE", "CUTTING"]},
           {"label": "Blunt object or vehicle", "keywords": ["BLUNT", "CLUB", "MOTOR VEHICLE"]},
           {"label": "Hands, fists, feet", "keywords": ["PERSONAL WEAPON", "ASPHYXIATION", "STRANGULATION"]}]


def main():
    for slug, (name, ori, geoid) in CITIES.items():
        cfg = {
            "title": f"Assault victims in {name}",
            "author": "Martin Ngoh",
            "place": {"name": name, "short": name, "census_geoid": geoid},
            "acs_release": "acs2024_5yr",
            "window": {"start": "2022-01-01", "end": "2025-12-31"},
            "event": {"noun": "assault", "plural": "assaults", "verb": "assaulted"},
            "incidents": [{"path": f"data/{slug}_simple.csv", "kind": "simple"}, {"path": f"data/{slug}_aggravated.csv", "kind": "aggravated"}],
            "kind_labels": {"simple": "Simple assault", "aggravated": "Aggravated assault"},
            "columns": {"id": "victim_id", "date": "incident_date", "race": "race_group", "sex": "sex", "age": "age",
                        "premise": "premise", "weapon": "weapon", "code": "offense_code"},
            "race_map": {"B": "Black", "H": "Hispanic", "W": "White", "A": "Asian"},
            "sex_values": {"F": "F", "M": "M"},
            "groups": ["Black", "Hispanic", "White", "Asian"],
            "focus": {"group": "Black", "sex": "F", "label": "Black women"},
            "flags": {"partner": {"column": "partner", "values": ["Y"], "label": "Intimate partner"}},
            "weapon_classes": WEAPONS,
            "sources": [f"FBI National Incident-Based Reporting System (NIBRS) state files for Texas, {name} Police Department ({ori}), 2022 to 2025",
                        "US Census Bureau ACS 2020 to 2024 five-year estimates via Census Reporter"],
            "_ori": ori,
        }
        d = ROOT / slug
        d.mkdir(exist_ok=True)
        (d / "analysis.json").write_text(json.dumps(cfg, indent=1) + "\n")
        print("wrote", d / "analysis.json")


if __name__ == "__main__":
    main()
