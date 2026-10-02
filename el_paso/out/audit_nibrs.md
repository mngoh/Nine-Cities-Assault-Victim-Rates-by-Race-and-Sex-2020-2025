# Audit: /Users/Martin1/Desktop/GIT/Texas-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/victim_offenses_el_paso.csv

127,001 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 113,086 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 7.3% | 24 |
| offense_id | 0.0% | 0.0% | 120,237 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 47 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 122,511 |
| victim_seq_num | 0.0% | 0.0% | 13 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 29.4% | 4 |
| race | 0.0% | 0.4% | 6 |
| ethnicity | 0.0% | 30.2% | 4 |
| resident_status | 62.5% | 1.2% | 3 |
| relationship | 70.0% | 0.0% | 153 |
| weapon | 71.7% | 0.3% | 37 |
| injury | 80.8% | 0.0% | 28 |

## Duplicates

4,490 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 24,454 |
| 290 | Destruction/Damage/Vandalism of Property | 16,898 |
| 23H | All Other Larceny | 15,157 |
| 35A | Drug/Narcotic Violations | 11,135 |
| 13C | Intimidation | 7,888 |
| 240 | Motor Vehicle Theft | 7,665 |
| 23C | Shoplifting | 7,568 |
| 26A | False Pretenses/Swindle/Confidence Game | 6,359 |
| 13A | Aggravated Assault | 6,313 |
| 23F | Theft From Motor Vehicle | 5,231 |
| 220 | Burglary/Breaking & Entering | 4,221 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,880 |
| 520 | Weapon Law Violations | 1,867 |
| 35B | Drug Equipment Violations | 1,643 |
| 120 | Robbery | 1,431 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,301 |
| 250 | Counterfeiting/Forgery | 896 |
| 11A | Rape | 714 |
| 370 | Pornography/Obscene Material | 571 |
| 720 | Animal Cruelty | 559 |
| 100 | Kidnapping/Abduction | 436 |
| 270 | Embezzlement | 398 |
| 23A | Pocket-picking | 355 |
| 11D | Criminal Sexual Contact | 327 |
| 200 | Arson | 326 |
| 26F | Identity Theft | 278 |
| 26G | Hacking/Computer Invasion | 239 |
| 11D | Fondling | 171 |
| 09A | Murder and Nonnegligent Manslaughter | 102 |
| 11B | Sodomy | 100 |
| 26C | Impersonation | 92 |
| 280 | Stolen Property Offenses | 82 |
| 23E | Theft From Coin-Operated Machine or Device | 80 |
| 23D | Theft From Building | 69 |
| 23B | Purse-snatching | 59 |
| 40A | Prostitution | 47 |
| 40C | Purchasing Prostitution | 33 |
| 09B | Negligent Manslaughter | 16 |
| 40B | Assisting or Promoting Prostitution | 12 |
| 11C | Sexual Assault With An Object | 9 |
| 26D | Welfare Fraud | 6 |
| 510 | Bribery | 4 |
| 64A | Human Trafficking, Commercial Sex Acts | 4 |
| 36A | Incest | 2 |
| 26E | Wire Fraud | 1 |
| 39A | Betting/Wagering | 1 |
| 09C | Justifiable Homicide | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,670 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2397 2022-02:2200 2022-03:2603 2022-04:2644 2022-05:2836 2022-06:2645 2022-07:2712 2022-08:2813 2022-09:2729 2022-10:2597 2022-11:2367 2022-12:2489 2023-01:2809 2023-02:2444 2023-03:2932 2023-04:2780 2023-05:3080 2023-06:2915 2023-07:2753 2023-08:2889 2023-09:2716 2023-10:2734 2023-11:2832 2023-12:2666 2024-01:2610 2024-02:2504 2024-03:2687 2024-04:2617 2024-05:2746 2024-06:2688 2024-07:2700 2024-08:2643 2024-09:2682 2024-10:2691 2024-11:2407 2024-12:2626 2025-01:2673 2025-02:2516 2025-03:2521 2025-04:2652 2025-05:2756 2025-06:2688 2025-07:2465 2025-08:2678 2025-09:2394 2025-10:2623 2025-11:2364 2025-12:2488

Use only full calendar years where you can; weight any partial year by its share of the year.