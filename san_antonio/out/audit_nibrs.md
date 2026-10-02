# Audit: /Users/Martin1/Desktop/GIT/Texas-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/victim_offenses_san_antonio.csv

628,427 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 545,134 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 8.8% | 24 |
| offense_id | 0.0% | 0.0% | 593,120 |
| offense_code | 0.0% | 0.0% | 51 |
| offense_name | 0.0% | 0.0% | 52 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 36 |
| victim_id | 0.0% | 0.0% | 591,372 |
| victim_seq_num | 0.0% | 0.0% | 127 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 26.7% | 4 |
| race | 0.0% | 8.9% | 7 |
| ethnicity | 0.0% | 38.9% | 4 |
| resident_status | 100.0% | nan% | 0 |
| relationship | 64.6% | 0.0% | 280 |
| weapon | 78.6% | 0.1% | 116 |
| injury | 87.5% | 0.0% | 58 |

## Duplicates

37,055 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23F | Theft From Motor Vehicle | 83,371 |
| 13B | Simple Assault | 80,094 |
| 290 | Destruction/Damage/Vandalism of Property | 78,927 |
| 240 | Motor Vehicle Theft | 54,635 |
| 23H | All Other Larceny | 48,909 |
| 23C | Shoplifting | 48,572 |
| 220 | Burglary/Breaking & Entering | 33,529 |
| 35A | Drug/Narcotic Violations | 33,193 |
| 13A | Aggravated Assault | 27,977 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 19,424 |
| 13C | Intimidation | 18,440 |
| 23D | Theft From Building | 14,569 |
| 26B | Credit Card/Automated Teller Machine Fraud | 12,556 |
| 26F | Identity Theft | 11,357 |
| 26A | False Pretenses/Swindle/Confidence Game | 9,051 |
| 120 | Robbery | 8,714 |
| 520 | Weapon Law Violations | 8,444 |
| 35B | Drug Equipment Violations | 8,037 |
| 250 | Counterfeiting/Forgery | 7,052 |
| 11A | Rape | 4,251 |
| 26E | Wire Fraud | 2,523 |
| 280 | Stolen Property Offenses | 2,304 |
| 370 | Pornography/Obscene Material | 2,166 |
| 11D | Criminal Sexual Contact | 1,629 |
| 270 | Embezzlement | 1,073 |
| 200 | Arson | 937 |
| 11D | Fondling | 818 |
| 40A | Prostitution | 639 |
| 09A | Murder and Nonnegligent Manslaughter | 626 |
| 11C | Sexual Assault With An Object | 618 |
| 11B | Sodomy | 617 |
| 23E | Theft From Coin-Operated Machine or Device | 514 |
| 720 | Animal Cruelty | 471 |
| 26C | Impersonation | 410 |
| 100 | Kidnapping/Abduction | 349 |
| 23A | Pocket-picking | 336 |
| 210 | Extortion/Blackmail | 285 |
| 26D | Welfare Fraud | 277 |
| 23B | Purse-snatching | 189 |
| 26G | Hacking/Computer Invasion | 179 |
| 09B | Negligent Manslaughter | 83 |
| 40C | Purchasing Prostitution | 60 |
| 64A | Human Trafficking, Commercial Sex Acts | 51 |
| 09C | Justifiable Homicide | 47 |
| 40B | Assisting or Promoting Prostitution | 43 |
| 39B | Operating/Promoting/Assisting Gambling | 27 |
| 510 | Bribery | 20 |
| 64B | Human Trafficking, Involuntary Servitude | 16 |
| 39A | Betting/Wagering | 7 |
| 39C | Gambling Equipment Violation | 7 |
| 36B | Statutory Rape | 3 |
| 36A | Incest | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 13,364 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:12598 2022-02:12168 2022-03:13560 2022-04:13476 2022-05:13869 2022-06:13504 2022-07:14275 2022-08:13573 2022-09:13613 2022-10:14059 2022-11:12649 2022-12:13303 2023-01:13512 2023-02:12606 2023-03:13960 2023-04:13782 2023-05:12024 2023-06:14080 2023-07:15076 2023-08:14708 2023-09:13821 2023-10:14325 2023-11:13274 2023-12:14138 2024-01:13052 2024-02:13215 2024-03:14198 2024-04:14341 2024-05:13696 2024-06:13667 2024-07:14286 2024-08:13895 2024-09:13426 2024-10:12588 2024-11:11506 2024-12:11722 2025-01:11643 2025-02:10683 2025-03:12629 2025-04:11644 2025-05:12474 2025-06:12232 2025-07:12667 2025-08:12238 2025-09:12055 2025-10:12070 2025-11:11393 2025-12:11154

Use only full calendar years where you can; weight any partial year by its share of the year.