# Assault victims in five Texas cities, and nine cities side by side

Black women's reported assault rate against Hispanic, White and Asian women's in Houston, San Antonio, Austin, Fort Worth and El Paso, 2022 to 2025, measured exactly as in the Dallas analysis ([Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025](https://github.com/mngoh/Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025)), then set beside Los Angeles, DC, Baltimore and Dallas. Built with [disparity-kit](https://github.com/mngoh/disparity-kit).

The comparison is `out/comparison.md` (numbers in `out/comparison.json`). Each city's kit outputs are in `<city>/out/`.

## Method

- Source: the FBI's NIBRS state files for Texas, 2022 to 2025. Each city is its own police department only; transit, school, campus and county agencies are left out.
- Offenses: aggravated (13A) and simple (13B) assault, individual victims of any age. Officers, intimidation and homicide are out.
- Groups: Hispanic of any race first, otherwise the recorded race. Partner flag from the victim-offender relationship.
- Population: ACS 2020 to 2024 five-year estimates via Census Reporter, for the Census place of each city.
- Not run here: location tests (NIBRS has no location), city open-data replications and city-specific checks such as Dallas's premises codes. Compare patterns, not levels: LA and Baltimore come from their own records systems, the rest from NIBRS.

## Rebuild

Python from disparity-kit; `KIT=~/.claude/disparity-kit/kit`.

```bash
python scripts/fetch_nibrs.py 2022 2023 2024 2025      # or link the Dallas project's copies into data/raw/
python $KIT/nibrs.py flatten data/raw/TX-*.zip --ori TXHPD0000 --ori TXSPD0000 --ori TX2270100 --ori TX2201200 --ori TX0710200 --out data/interim/victim_offenses.csv
python scripts/make_configs.py                         # <city>/analysis.json, the Dallas decisions for every city
python scripts/run_cities.py                           # every city at once: audit, victims, denominators, tests
python scripts/compare.py                              # nine cities; reads the four earlier projects from ~/Desktop/GIT as well
```
