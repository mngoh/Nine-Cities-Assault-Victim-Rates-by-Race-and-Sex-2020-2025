# Audit: /Users/Martin1/Desktop/GIT/Texas-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/victim_offenses_austin.csv

296,309 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 262,130 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 8.8% | 24 |
| offense_id | 0.0% | 0.0% | 281,728 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 46 |
| victim_id | 0.0% | 0.0% | 281,384 |
| victim_seq_num | 0.0% | 0.0% | 92 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 21.4% | 4 |
| race | 0.0% | 4.0% | 7 |
| ethnicity | 0.0% | 26.0% | 4 |
| resident_status | 20.7% | 56.1% | 3 |
| relationship | 60.1% | 0.0% | 268 |
| weapon | 78.2% | 0.4% | 79 |
| injury | 86.2% | 0.0% | 65 |

## Duplicates

14,925 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 38,453 |
| 23H | All Other Larceny | 37,379 |
| 23F | Theft From Motor Vehicle | 35,544 |
| 290 | Destruction/Damage/Vandalism of Property | 25,170 |
| 240 | Motor Vehicle Theft | 22,973 |
| 13C | Intimidation | 20,398 |
| 220 | Burglary/Breaking & Entering | 18,637 |
| 35A | Drug/Narcotic Violations | 15,349 |
| 13A | Aggravated Assault | 12,829 |
| 26B | Credit Card/Automated Teller Machine Fraud | 9,378 |
| 23C | Shoplifting | 8,467 |
| 26A | False Pretenses/Swindle/Confidence Game | 8,330 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 7,549 |
| 26C | Impersonation | 5,754 |
| 35B | Drug Equipment Violations | 5,556 |
| 120 | Robbery | 4,368 |
| 520 | Weapon Law Violations | 3,985 |
| 23A | Pocket-picking | 3,277 |
| 250 | Counterfeiting/Forgery | 3,150 |
| 11A | Rape | 1,677 |
| 720 | Animal Cruelty | 1,376 |
| 370 | Pornography/Obscene Material | 1,237 |
| 100 | Kidnapping/Abduction | 1,042 |
| 11D | Criminal Sexual Contact | 926 |
| 200 | Arson | 660 |
| 23D | Theft From Building | 645 |
| 11C | Sexual Assault With An Object | 504 |
| 11D | Fondling | 341 |
| 09A | Murder and Nonnegligent Manslaughter | 251 |
| 11B | Sodomy | 235 |
| 23E | Theft From Coin-Operated Machine or Device | 183 |
| 210 | Extortion/Blackmail | 129 |
| 40A | Prostitution | 109 |
| 26G | Hacking/Computer Invasion | 73 |
| 40C | Purchasing Prostitution | 64 |
| 23B | Purse-snatching | 51 |
| 280 | Stolen Property Offenses | 47 |
| 270 | Embezzlement | 45 |
| 09B | Negligent Manslaughter | 40 |
| 39A | Betting/Wagering | 32 |
| 09C | Justifiable Homicide | 22 |
| 40B | Assisting or Promoting Prostitution | 19 |
| 64B | Human Trafficking, Involuntary Servitude | 18 |
| 64A | Human Trafficking, Commercial Sex Acts | 14 |
| 510 | Bribery | 9 |
| 39B | Operating/Promoting/Assisting Gambling | 8 |
| 39C | Gambling Equipment Violation | 2 |
| 36A | Incest | 2 |
| 26E | Wire Fraud | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 6,237 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:6512 2022-02:5958 2022-03:6702 2022-04:6228 2022-05:6307 2022-06:6827 2022-07:6810 2022-08:6437 2022-09:6515 2022-10:6522 2022-11:5554 2022-12:5946 2023-01:6267 2023-02:6011 2023-03:6631 2023-04:5388 2023-05:4865 2023-06:6321 2023-07:6338 2023-08:6210 2023-09:5972 2023-10:6510 2023-11:5870 2023-12:6069 2024-01:5922 2024-02:5863 2024-03:6393 2024-04:6231 2024-05:6640 2024-06:6046 2024-07:6543 2024-08:6113 2024-09:5584 2024-10:6183 2024-11:5783 2024-12:5769 2025-01:6222 2025-02:5350 2025-03:6533 2025-04:6296 2025-05:6288 2025-06:6332 2025-07:6465 2025-08:6602 2025-09:6243 2025-10:6567 2025-11:5845 2025-12:5726

Use only full calendar years where you can; weight any partial year by its share of the year.