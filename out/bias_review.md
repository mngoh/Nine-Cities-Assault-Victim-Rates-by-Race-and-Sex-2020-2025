# Racial bias review

Focus: Black women. This screen finds candidates; read every flag in context before acting.

## Data

- **note: race coding.** Officers record race by sight; the denominator is Black alone. Alone or in combination is 9% larger. Worst-case ratios: Hispanic 2.23x (from 2.43x), White 3.44x (from 3.76x), Asian 7.4x (from 8.08x). The writeup must state this bound.
- **note: overlapping denominators.** Share of each race-alone group that is also Hispanic: {'Black': 1.6, 'Asian': 1.0}. These residents count in two denominators; small shares are tolerable, large ones need non-Hispanic tables.
- **note: race outside the groups.** 1.2% of victims map to no group. Largest raw codes: `U` 1,702, `I` 215, `P` 195. Check none of them should belong to a group.
- **note: unknown race by sex.** Women 0.4%, men 0.8%.
- **note: enforcement and reporting.** Police data reflects where police patrol and who calls them. Heavier policing or more reporting in some neighborhoods raises recorded rates there. The writeup must say the data cannot separate this from real differences.
- **note: controls are not neutral.** Neighborhood, income and housing are shaped by segregation and discrimination. A gap that shrinks after these controls has been located, not explained away; say so.

## Writeup

Files: `index.html`, `README.md`

### index.html
- **review: Causal claim** (`causes`): "The data says Black women are assaulted at a higher reported rate in each of these cities. It does not say why. Nothing here measures causes, offenders or circumstances."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Causal claim** (`because`): "Nine large cities, six of them in Texas, chosen because their data was available. They show a consistent pattern in police data; they do not measure a national rate or a trend."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Offender implication** (`offenders`): "The data says Black women are assaulted at a higher reported rate in each of these cities. It does not say why. Nothing here measures causes, offenders or circumstances."  
  Victim data says nothing about who offended. Remove, or state that offenders are not in the data.
- **review: Explained-away language** (`accounts for the gap`): "Women only (168,969 Black women, 246,504 other women). Each cut asks whether a plain explanation accounts for the gap."  
  Controls like neighborhood and income are themselves shaped by segregation and discrimination. 'Explained by location' does not mean 'not related to race'.
- **review: Explained-away language** (`explained away`): "Located, not explained away"  
  Controls like neighborhood and income are themselves shaped by segregation and discrimination. 'Explained by location' does not mean 'not related to race'.
- **review: Explained-away language** (`explained away`): "Tract poverty, income, jobs and housing are shaped by segregation and disinvestment. Where these controls narrow a gap, the gap has been located in where women live; it has not been explained away."  
  Controls like neighborhood and income are themselves shaped by segregation and discrimination. 'Explained by location' does not mean 'not related to race'.

### README.md
- **review: Causal claim** (`causes`): "- This shows what, not why: The data says Black women are assaulted at a higher reported rate in each of these cities. It does not say why. Nothing here measures causes, offenders or circumstances."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Causal claim** (`because`): "- Not a national sample: Nine large cities, six of them in Texas, chosen because their data was available. They show a consistent pattern in police data; they do not measure a national rate or a trend."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Offender implication** (`offenders`): "- This shows what, not why: The data says Black women are assaulted at a higher reported rate in each of these cities. It does not say why. Nothing here measures causes, offenders or circumstances."  
  Victim data says nothing about who offended. Remove, or state that offenders are not in the data.
- **review: Offender implication** (`offender`): "- Groups: Hispanic of any race first, otherwise the recorded race. Partner flag from the victim-offender relationship."  
  Victim data says nothing about who offended. Remove, or state that offenders are not in the data.

### Required statements

- present: says it does not explain why
- present: names reporting differences
- present: names the race-coding limit
- present: separates reports from people

## Reviewer questions (answer in prose, not by regex)

- Does any sentence invite the reader to infer who the offenders are?
- Would the framing read the same if the groups were swapped?
- Is the comparison group chosen to make the gap look larger (for example, headlining the most extreme pair)?
- Are structural explanations (segregation, policing intensity, access to services) acknowledged as unmeasured, without being asserted?
- Does the headline survive the race-coding worst case and the least favorable comparison?
- Is the focus group described with agency and dignity, as people harmed, not as a problem?