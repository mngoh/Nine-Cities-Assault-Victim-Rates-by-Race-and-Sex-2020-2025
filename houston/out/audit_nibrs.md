# Audit: /Users/Martin1/Desktop/GIT/Texas-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/victim_offenses_houston.csv

1,031,077 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 785,310 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.1% | 4.9% | 24 |
| offense_id | 0.0% | 0.0% | 857,513 |
| offense_code | 0.0% | 0.0% | 49 |
| offense_name | 0.0% | 0.0% | 50 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 46 |
| victim_id | 0.0% | 0.0% | 976,492 |
| victim_seq_num | 0.0% | 0.0% | 114 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 19.1% | 4 |
| race | 0.0% | 3.6% | 7 |
| ethnicity | 0.0% | 22.1% | 4 |
| resident_status | 18.4% | 4.8% | 3 |
| relationship | 18.5% | 0.0% | 578 |
| weapon | 77.1% | 0.2% | 123 |
| injury | 89.1% | 0.0% | 58 |

## Duplicates

54,585 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23F | Theft From Motor Vehicle | 126,457 |
| 13B | Simple Assault | 106,595 |
| 290 | Destruction/Damage/Vandalism of Property | 100,148 |
| 23C | Shoplifting | 89,233 |
| 23H | All Other Larceny | 88,909 |
| 13C | Intimidation | 83,236 |
| 240 | Motor Vehicle Theft | 74,539 |
| 220 | Burglary/Breaking & Entering | 73,965 |
| 13A | Aggravated Assault | 67,830 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 45,135 |
| 120 | Robbery | 36,218 |
| 35A | Drug/Narcotic Violations | 30,963 |
| 26F | Identity Theft | 14,184 |
| 250 | Counterfeiting/Forgery | 14,083 |
| 520 | Weapon Law Violations | 13,557 |
| 26A | False Pretenses/Swindle/Confidence Game | 12,604 |
| 26B | Credit Card/Automated Teller Machine Fraud | 9,369 |
| 23D | Theft From Building | 6,885 |
| 35B | Drug Equipment Violations | 6,766 |
| 11A | Rape | 3,234 |
| 11B | Sodomy | 2,563 |
| 280 | Stolen Property Offenses | 2,468 |
| 40A | Prostitution | 2,303 |
| 11D | Criminal Sexual Contact | 2,017 |
| 370 | Pornography/Obscene Material | 1,934 |
| 720 | Animal Cruelty | 1,878 |
| 40C | Purchasing Prostitution | 1,673 |
| 200 | Arson | 1,573 |
| 100 | Kidnapping/Abduction | 1,535 |
| 270 | Embezzlement | 1,497 |
| 09A | Murder and Nonnegligent Manslaughter | 1,368 |
| 23B | Purse-snatching | 1,277 |
| 210 | Extortion/Blackmail | 1,200 |
| 23A | Pocket-picking | 936 |
| 11D | Fondling | 586 |
| 26G | Hacking/Computer Invasion | 528 |
| 26C | Impersonation | 421 |
| 23E | Theft From Coin-Operated Machine or Device | 386 |
| 64A | Human Trafficking, Commercial Sex Acts | 310 |
| 26E | Wire Fraud | 205 |
| 40B | Assisting or Promoting Prostitution | 136 |
| 26D | Welfare Fraud | 120 |
| 39C | Gambling Equipment Violation | 50 |
| 09C | Justifiable Homicide | 49 |
| 510 | Bribery | 38 |
| 64B | Human Trafficking, Involuntary Servitude | 34 |
| 11C | Sexual Assault With An Object | 27 |
| 39B | Operating/Promoting/Assisting Gambling | 24 |
| 39A | Betting/Wagering | 16 |
| 09B | Negligent Manslaughter | 15 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 21,672 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:21693 2022-02:20273 2022-03:22395 2022-04:22259 2022-05:22984 2022-06:22127 2022-07:23645 2022-08:23154 2022-09:22028 2022-10:22628 2022-11:20637 2022-12:19460 2023-01:23004 2023-02:20378 2023-03:22592 2023-04:22054 2023-05:23333 2023-06:22216 2023-07:22778 2023-08:22314 2023-09:21392 2023-10:21117 2023-11:21163 2023-12:20842 2024-01:21235 2024-02:20161 2024-03:21771 2024-04:23036 2024-05:23738 2024-06:22325 2024-07:22135 2024-08:21966 2024-09:21568 2024-10:21811 2024-11:20317 2024-12:21138 2025-01:19970 2025-02:16580 2025-03:21159 2025-04:21652 2025-05:22588 2025-06:21089 2025-07:21026 2025-08:20778 2025-09:19905 2025-10:20111 2025-11:19043 2025-12:19509

Use only full calendar years where you can; weight any partial year by its share of the year.