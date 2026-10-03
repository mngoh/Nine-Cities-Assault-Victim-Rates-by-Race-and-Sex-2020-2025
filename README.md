# Assault victims in nine cities

Black women's reported assault rate against Hispanic, White and Asian women's in nine cities, 2020 to 2025: Los Angeles, DC, Baltimore and Dallas from their own analyses, and Houston, San Antonio, Austin, Fort Worth and El Paso run here, measured exactly as in the Dallas analysis ([Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025](https://github.com/mngoh/Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025)). Built with [disparity-kit](https://github.com/mngoh/disparity-kit).

The full page is `index.html`. The comparison table is `out/comparison.md` (numbers in `out/comparison.json`). Each Texas city's kit outputs are in `<city>/out/`.

## Results

<!-- results:start -->
**In all nine cities, Black women's reported assault rate is higher than Hispanic and White women's. Against White women the gap runs from 1.8 times in El Paso to 10.2 times in DC, and it holds at the most conservative bound in every city. It is widest for aggravated assault in all nine.**

Live page: https://mngoh.github.io/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/

| City | Source, years | Black women, per 100,000 | vs Hispanic | vs White | Lowest bound vs Hispanic | Lowest bound vs White |
|---|---|---|---|---|---|---|
| [Los Angeles](https://mngoh.github.io/LA-Crime/) | LAPD records (pre-NIBRS), 2020 to 2023 | 3,544 | 2.86x | 5.7x | 2.31x | 4.6x |
| [DC](https://mngoh.github.io/DC-Assault-Victims-by-Race-and-Sex-2022-2025/) | FBI NIBRS, 2022 to 2025 | 4,205 | 3.22x | 10.21x | 2.22x | 9.38x |
| [Baltimore](https://mngoh.github.io/Baltimore-Assault-Victims/) | BPD legacy records, 2022 to 2024 | 3,605 | 1.62x | 2.58x | 0.82x | 2.46x |
| [Dallas](https://mngoh.github.io/Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/) | FBI NIBRS, 2022 to 2025 | 3,798 | 2.26x | 3.91x | 2.11x | 3.64x |
| [Houston](https://github.com/mngoh/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/tree/main/houston) | FBI NIBRS, 2022 to 2025 | 4,193 | 2.43x | 3.76x | 2.23x | 3.44x |
| [San Antonio](https://github.com/mngoh/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/tree/main/san_antonio) | FBI NIBRS, 2022 to 2025 | 3,872 | 1.84x | 2.22x | 1.43x | 1.73x |
| [Austin](https://github.com/mngoh/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/tree/main/austin) | FBI NIBRS, 2022 to 2025 | 4,197 | 2.07x | 4.86x | 1.66x | 3.89x |
| [Fort Worth](https://github.com/mngoh/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/tree/main/fort_worth) | FBI NIBRS, 2022 to 2025 | 2,675 | 2.19x | 3.06x | 1.95x | 2.72x |
| [El Paso](https://github.com/mngoh/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/tree/main/el_paso) | FBI NIBRS, 2022 to 2025 | 2,036 | 1.67x | 1.83x | 1.18x | 1.29x |

Per 100,000 residents a year, Black women's rate runs from 2,036 in El Paso to 4,205 in DC. Against Hispanic women it is 1.6 to 3.2 times, and the most conservative bound stays above 1 in every city but Baltimore, where ethnicity is unknown for 41.6% of women victims.
Where neighborhood could be controlled (Los Angeles, Baltimore and Dallas for non-family assaults only), 2.1 to 3.1 times remains against Hispanic and White women. The gap is not concentrated in partner assault: in six of eight cities with relationship data, it is smaller within partner assault than outside it.
Between the first and second half of each city's window, the gap with Hispanic women narrowed in eight of nine cities and held in Houston; the gap with White women changed by between -1% and +6%.
What this number measures: police reports, not how often women are hurt. In the national victimization survey, which counts assaults whether or not police learned of them, Black and White women describe being assaulted at about the same rate nationally and about 1.5 to 2 times in large cities. A follow-up (github.com/mngoh/Police-Records-vs-Survey-Assault-Victims-by-Race-and-Sex-2015-2025) tested why police records differ more: not reporting rates, not how police write up a call, not the same women counted repeatedly, but largely where assaults happen and who calls.

Caveats:

- This shows what, not why: The data says Black women are assaulted at a higher reported rate in each of these cities. It does not say why. Nothing here measures causes, offenders or circumstances.
- Reported crimes only: Every number is a report that reached the police. Willingness to report, and recording practice, differ by group, area, city and time.
- Reports, not people: Rates count reports. Someone assaulted twice counts twice, so a rate is not the share of people assaulted.
- Exposure is not population: Rates divide by where people live, not where they spend time.
- Policing and reporting: Police data reflects where officers patrol and who calls them. This data cannot separate more policing or more reporting from more assaults.
- Sources differ by city: Los Angeles uses LAPD's records from before its move to NIBRS (2020 to 2023). Baltimore uses the Baltimore Police Department's legacy records (2022 to 2024). DC, Dallas, Houston, San Antonio, Austin, Fort Worth and El Paso use the FBI's NIBRS files. Offense definitions are close but not identical, so compare patterns across cities, not levels.
- Five cities had lighter checks: Houston, San Antonio, Austin, Fort Worth and El Paso ran on the FBI's files alone, with the decisions made for Dallas. Each has all 48 months of data, and race is unknown or outside the compared groups for 0.1% to 2.6% of women victims. There is no location test, no second source and no city-specific check like Dallas's.
- Who is recorded as Black: Race is recorded by officers; the Census counts people who are Black alone. Across these cities, 5% to 42% more residents are Black alone or in combination. The lowest bounds assume every one of them is recorded as Black.
- Hispanic ethnicity: Unknown or unspecified ethnicity runs from 0.7% of women victims in El Paso to 41.6% in Baltimore. Where it is high the Hispanic comparison is uncertain, and in Baltimore it cannot be settled. Los Angeles records Hispanic as a descent code, not a separate field.
- Agencies: Each city counts its own police department only. Assaults recorded only by transit, school, campus, hospital or county police are missing.
- Small numbers: El Paso's figures rest on 840 Black women victims and about 10,000 Black women residents. Asian women's counts are small in most cities, as few as 89 in El Paso, so their ratios stay out of the headline.
- Windows differ: Los Angeles covers 2020 to 2023 and Baltimore covers 2022 to 2024; the rest cover 2022 to 2025. Populations are ACS 2020 to 2024 five-year estimates.
- Not a national sample: Nine large cities, six of them in Texas, chosen because their data was available. They show a consistent pattern in police data; they do not measure a national rate or a trend.
<!-- results:end -->

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
python scripts/build_page.py                           # index.html and the results block above
```
