# Audit: /Users/Martin1/Desktop/GIT/Texas-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/victim_offenses_fort_worth.csv

221,230 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 186,613 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 12.3% | 24 |
| offense_id | 0.0% | 0.0% | 201,475 |
| offense_code | 0.0% | 0.0% | 49 |
| offense_name | 0.0% | 0.0% | 50 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 211,259 |
| victim_seq_num | 0.0% | 0.0% | 125 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 28.1% | 4 |
| race | 0.0% | 1.4% | 7 |
| ethnicity | 0.0% | 31.5% | 4 |
| resident_status | 32.4% | 3.3% | 3 |
| relationship | 63.7% | 0.0% | 270 |
| weapon | 75.1% | 0.6% | 72 |
| injury | 87.1% | 0.0% | 45 |

## Duplicates

9,971 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23H | All Other Larceny | 37,126 |
| 13B | Simple Assault | 29,898 |
| 290 | Destruction/Damage/Vandalism of Property | 25,355 |
| 23F | Theft From Motor Vehicle | 23,064 |
| 240 | Motor Vehicle Theft | 18,471 |
| 220 | Burglary/Breaking & Entering | 15,660 |
| 13A | Aggravated Assault | 12,716 |
| 35A | Drug/Narcotic Violations | 11,487 |
| 23C | Shoplifting | 11,372 |
| 13C | Intimidation | 5,658 |
| 520 | Weapon Law Violations | 4,229 |
| 120 | Robbery | 3,930 |
| 35B | Drug Equipment Violations | 3,328 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 3,145 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,391 |
| 26F | Identity Theft | 2,051 |
| 11A | Rape | 1,828 |
| 250 | Counterfeiting/Forgery | 1,138 |
| 370 | Pornography/Obscene Material | 1,002 |
| 100 | Kidnapping/Abduction | 987 |
| 26A | False Pretenses/Swindle/Confidence Game | 956 |
| 280 | Stolen Property Offenses | 628 |
| 200 | Arson | 558 |
| 23B | Purse-snatching | 530 |
| 720 | Animal Cruelty | 439 |
| 11D | Criminal Sexual Contact | 426 |
| 40A | Prostitution | 401 |
| 09A | Murder and Nonnegligent Manslaughter | 337 |
| 11B | Sodomy | 324 |
| 270 | Embezzlement | 265 |
| 26G | Hacking/Computer Invasion | 221 |
| 11D | Fondling | 180 |
| 23D | Theft From Building | 160 |
| 23A | Pocket-picking | 158 |
| 11C | Sexual Assault With An Object | 153 |
| 26C | Impersonation | 153 |
| 40B | Assisting or Promoting Prostitution | 133 |
| 23E | Theft From Coin-Operated Machine or Device | 114 |
| 64A | Human Trafficking, Commercial Sex Acts | 66 |
| 40C | Purchasing Prostitution | 42 |
| 39B | Operating/Promoting/Assisting Gambling | 38 |
| 210 | Extortion/Blackmail | 21 |
| 64B | Human Trafficking, Involuntary Servitude | 18 |
| 09B | Negligent Manslaughter | 17 |
| 09C | Justifiable Homicide | 16 |
| 510 | Bribery | 15 |
| 26E | Wire Fraud | 13 |
| 39C | Gambling Equipment Violation | 5 |
| 36A | Incest | 4 |
| 26D | Welfare Fraud | 3 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 4,631 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:4660 2022-02:3956 2022-03:4619 2022-04:5053 2022-05:5102 2022-06:4951 2022-07:5031 2022-08:4839 2022-09:4418 2022-10:4591 2022-11:4407 2022-12:4315 2023-01:4643 2023-02:3901 2023-03:4810 2023-04:4866 2023-05:5062 2023-06:5019 2023-07:4899 2023-08:3763 2023-09:4648 2023-10:4834 2023-11:4795 2023-12:4698 2024-01:4664 2024-02:4440 2024-03:4772 2024-04:4580 2024-05:5237 2024-06:5195 2024-07:4926 2024-08:5273 2024-09:4773 2024-10:4914 2024-11:4559 2024-12:4521 2025-01:4393 2025-02:3788 2025-03:4388 2025-04:4494 2025-05:4565 2025-06:4075 2025-07:4385 2025-08:4343 2025-09:4176 2025-10:4452 2025-11:4190 2025-12:4247

Use only full calendar years where you can; weight any partial year by its share of the year.