"""Render the nine-city page (index.html) and the README results block from out/comparison.json.

Uses the kit's page template, colors and chart conventions (dark theme, red for Black women's measure, outlined bars,
Chart.js, no em dashes), with horizontal bars so nine city names stay readable on a phone. Every sentence with a number
is generated from out/comparison.json, which scripts/compare.py builds from each city's own outputs.

  python scripts/build_page.py      ->  index.html, README.md block between <!-- results:start --> and <!-- results:end -->
"""
import json
import os
import pathlib
import sys

sys.path.insert(0, os.path.expanduser(os.environ.get("DISPARITY_KIT", "~/.claude/disparity-kit/kit")))
from build_page import TEMPLATE, esc, listing  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/mngoh/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025"
NEW = ["Houston", "San Antonio", "Austin", "Fort Worth", "El Paso"]
SOURCE_PROSE = {"LAPD records (pre-NIBRS)": "LAPD's records from before its move to NIBRS", "BPD legacy records": "the Baltimore Police Department's legacy records"}
WORDS = {9: "all nine", 8: "eight", 7: "seven", 6: "six", 5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}


def x(v):
    r = round(v, 1)
    return str(int(r)) if r == int(r) else str(r)


def n_of(k, n):
    return WORDS[n] if k == n == 9 else f"{WORDS.get(k, k)} of {WORDS.get(n, n) if n != 9 else 'nine'}"


def main():
    rows = json.loads((ROOT / "out/comparison.json").read_text())
    by = {r["city"]: r for r in rows}
    cities = [r["city"] for r in rows]
    js = []

    def box(cid, title, sub, height=None):
        style = f' style="height:{height}px"' if height else ""
        return (f'<div class="chart-box"><h3>{esc(title)}</h3><div class="chart-sub">{esc(sub)}</div>'
                f'<div class="chart-wrap"{style}><canvas id="{cid}"></canvas></div></div>')

    def hbars(cid, labels, datasets, xtitle):
        ds = ",".join(f"{{label:{json.dumps(lab)},data:{json.dumps(data)},...bar({col})}}" for lab, data, col in datasets)
        js.append(f"new Chart(document.getElementById('{cid}'),{{type:'bar',data:{{labels:{json.dumps(labels)},datasets:[{ds}]}},"
                  f"options:{{...base,indexAxis:'y',plugins:{{legend:{{display:true}}}},"
                  f"scales:{{y:{{grid:{{display:false}},ticks:{{color:C.text}}}},x:{{min:0,title:{{display:true,text:{json.dumps(xtitle)}}}}}}}}}}});")

    grid = lambda boxes: (f'<div class="charts section-end"{" style=\"grid-template-columns:1fr\"" if len(boxes) == 1 else ""}>'
                          f'{"".join(boxes)}</div>')  # a lone chart takes the full width
    H = lambda n: 90 + 34 * n  # chart height for n cities with two bars each

    # numbers used in prose
    vsW = {c: by[c]["ratio"]["White"] for c in cities}
    vsH = {c: by[c]["ratio"]["Hispanic"] for c in cities}
    lowW = {c: by[c]["range"]["White"][0] for c in cities}
    lowH = {c: by[c]["range"]["Hispanic"][0] for c in cities}
    rate = {c: by[c]["black_women_rate"] for c in cities}
    cW_lo, cW_hi = min(vsW, key=vsW.get), max(vsW, key=vsW.get)
    cH_lo, cH_hi = min(vsH, key=vsH.get), max(vsH, key=vsH.get)
    c_r_lo, c_r_hi = min(rate, key=rate.get), max(rate, key=rate.get)
    hold_W = [c for c in cities if lowW[c] > 1]
    fail_H = [c for c in cities if lowH[c] <= 1]
    sev = [c for c in cities if by[c]["aggravated"]["White"] > by[c]["simple"]["White"]]
    rel = [c for c in cities if by[c]["partner_ratio"]]
    smaller_in_partner = [c for c in rel if by[c]["partner_ratio"]["Hispanic"] < by[c]["non_partner_ratio"]["Hispanic"]]
    larger_in_partner = [c for c in rel if c not in smaller_in_partner]
    lowest_share = [c for c in rel if by[c]["partner_share"]["Black"] < min(by[c]["partner_share"][g] for g in ("Hispanic", "White", "Asian"))]
    chg = lambda c, g: (by[c]["halves"]["second"][g] / by[c]["halves"]["first"][g] - 1) * 100
    narrowed_H = [c for c in cities if chg(c, "Hispanic") < -3]
    flat_H = [c for c in cities if abs(chg(c, "Hispanic")) <= 3]
    chg_W = [round(chg(c, "White")) for c in cities]
    age_down = [c for c in cities if by[c]["age_standardized"]["White"] < vsW[c] * 0.9]
    adj = [c for c in cities if by[c]["adjusted"]]
    adj_vals = [by[c]["adjusted"][g] for c in adj for g in ("Hispanic", "White")]
    eth = {c: by[c]["eth_unknown_pct_women"] for c in cities if by[c]["eth_unknown_pct_women"] is not None}
    c_eth_lo, c_eth_hi = min(eth, key=eth.get), max(eth, key=eth.get)
    unk_new = [by[c]["unknown_race_pct"]["F"] for c in NEW]
    asian = {c: by[c]["women_victims"].get("Asian") for c in cities if by[c]["women_victims"].get("Asian")}
    c_as_lo = min(asian, key=asian.get)
    ep = by["El Paso"]
    combo = [round((by[c]["combo_ratio"] - 1) * 100) for c in cities if by[c].get("combo_ratio")]
    total = sum(by[c]["victims_total"] for c in cities)
    n_focus = sum(by[c]["women_n"]["focus"] for c in cities)
    n_other = sum(by[c]["women_n"]["other"] for c in cities)

    lede = (f"In {n_of(len(cities), 9) if len(cities) == 9 else len(cities)} cities, Black women's reported assault rate is higher than Hispanic and White women's. "
            f"Against White women the gap runs from {x(vsW[cW_lo])} times in {cW_lo} to {x(vsW[cW_hi])} times in {cW_hi}, "
            f"and it holds at the most conservative bound in {'every city' if len(hold_W) == len(cities) else n_of(len(hold_W), len(cities)) + ' cities'}. "
            f"It is widest for aggravated assault in {n_of(len(sev), len(cities))}.")
    question = "Across nine large cities, are Black women assaulted at a higher reported rate than Hispanic, White and Asian women, and does the gap look the same everywhere?"
    answer = [
        f"Per 100,000 residents a year, Black women's rate runs from {rate[c_r_lo]:,} in {c_r_lo} to {rate[c_r_hi]:,} in {c_r_hi}. "
        f"Against Hispanic women it is {x(vsH[cH_lo])} to {x(vsH[cH_hi])} times, and the most conservative bound stays above 1 in "
        + ("every city but " + listing(f"{c}, where ethnicity is unknown for {by[c]['eth_unknown_pct_women']}% of women victims" for c in fail_H) if fail_H else "every city") + ".",
        f"Where neighborhood could be controlled ({listing(c + (' for non-family assaults only' if 'non-family' in (by[c]['adjusted_note'] or '') else '') for c in adj)}), "
        f"{x(min(adj_vals))} to {x(max(adj_vals))} times remains against Hispanic and White women. "
        f"The gap is not concentrated in partner assault: in {n_of(len(smaller_in_partner), len(rel))} cities with relationship data, it is smaller within partner assault than outside it.",
        f"Between the first and second half of each city's window, the gap with Hispanic women narrowed in {n_of(len(narrowed_H), len(cities))} cities"
        + (f" and held in {listing(flat_H)}" if flat_H else "") + f"; the gap with White women changed by between {min(chg_W)}% and {max(chg_W):+d}%.",
        "What this number measures: police reports, not how often women are hurt. In the national victimization survey, which counts assaults whether or not police "
        "learned of them, Black and White women describe being assaulted at about the same rate nationally and about 1.5 to 2 times in large cities. A follow-up "
        "(github.com/mngoh/Police-Records-vs-Survey-Assault-Victims-by-Race-and-Sex-2015-2025) tested why police records differ more: not reporting rates, not how "
        "police write up a call (or only a little), not the same women counted repeatedly, but largely where assaults happen and who calls.",
    ]

    # overview: rates and the two main ratios
    rates_box = box("rateChart", "Women's assault rate, by city",
                    "Victims per 100,000 residents per year. Asian women's rates are in the table below.", height=90 + 46 * len(cities))
    hbars("rateChart", cities, [("Black women", [rate[c] for c in cities], "C.red"),
                                ("Hispanic women", [by[c]["rates_women"]["Hispanic"] for c in cities], "C.blue"),
                                ("White women", [by[c]["rates_women"]["White"] for c in cities], "C.blueLight")], "Victims per 100,000 per year")
    w_box = box("whiteChart", "Against White women",
                f"Black women's rate as a multiple of White women's: {x(vsW[cW_lo])}x in {cW_lo} to {x(vsW[cW_hi])}x in {cW_hi}. "
                f"The lowest bound (grey) assumes the worst case for race coding and missing ethnicity; it stays above 1 in "
                f"{'every city' if len(hold_W) == len(cities) else n_of(len(hold_W), len(cities)) + ' cities'}.", height=H(len(cities)))
    hbars("whiteChart", cities, [("Lowest bound", [lowW[c] for c in cities], "C.muted"), ("As recorded", [vsW[c] for c in cities], "C.red")], "Rate ratio")
    h_box = box("hispChart", "Against Hispanic women",
                f"{x(vsH[cH_lo])}x in {cH_lo} to {x(vsH[cH_hi])}x in {cH_hi}. The lowest bound stays above 1 everywhere but {listing(fail_H)}.", height=H(len(cities)))
    hbars("hispChart", cities, [("Lowest bound", [lowH[c] for c in cities], "C.muted"), ("As recorded", [vsH[c] for c in cities], "C.red")], "Rate ratio")

    # tests
    sev_box = box("sevChart", "Severity",
                  f"Against White women, the gap is wider for aggravated assault than for simple assault in {n_of(len(sev), len(cities))} cities.", height=H(len(cities)))
    hbars("sevChart", cities, [("Simple assault", [by[c]["simple"]["White"] for c in cities], "C.muted"),
                               ("Aggravated assault", [by[c]["aggravated"]["White"] for c in cities], "C.red")], "Rate ratio, Black to White women")
    age_box = box("ageChart", "Age",
                  "Against White women, before and after standardizing to one age mix. " +
                  (f"Age narrows the gap by more than a tenth only in {listing(age_down)}." if age_down else "Age barely moves the gap anywhere."), height=H(len(cities)))
    hbars("ageChart", cities, [("Crude", [vsW[c] for c in cities], "C.muted"), ("Age-standardized", [by[c]["age_standardized"]["White"] for c in cities], "C.red")],
          "Rate ratio, Black to White women")
    p_box = box("partnerChart", "Intimate partner assault",
                f"Against Hispanic women, within partner assault and outside it. The gap is smaller within partner assault in {n_of(len(smaller_in_partner), len(rel))} cities"
                + (f", larger in {listing(larger_in_partner)}" if larger_in_partner else "") + ". "
                + (f"Black women have the lowest partner share of the four groups in {listing(lowest_share)}." if lowest_share else "")
                + (" Baltimore's data has no relationship field." if "Baltimore" not in rel else ""), height=H(len(rel)))
    hbars("partnerChart", rel, [("Partner assault", [by[c]["partner_ratio"]["Hispanic"] for c in rel], "C.blue"),
                                ("Other assault", [by[c]["non_partner_ratio"]["Hispanic"] for c in rel], "C.red")], "Rate ratio, Black to Hispanic women")
    t_box = box("timeChart", "Over time",
                f"Against Hispanic women, first half of each city's window and second half. Narrower in {n_of(len(narrowed_H), len(cities))} cities"
                + (f", about the same in {listing(flat_H)}" if flat_H else "") + ".", height=H(len(cities)))
    hbars("timeChart", cities, [("First half", [by[c]["halves"]["first"]["Hispanic"] for c in cities], "C.muted"),
                                ("Second half", [by[c]["halves"]["second"]["Hispanic"] for c in cities], "C.red")], "Rate ratio, Black to Hispanic women")

    # neighborhood: the cities with victim locations
    labels = [[c, f"vs {g}"] for c in adj for g in ("Hispanic", "White")]
    m_box = box("modelChart", "After neighborhood controls",
                "Tract-level Poisson models with age, year, police district and tract poverty, income, unemployment, renting and density. "
                + "After every control: " + "; ".join(f"{c} {x(by[c]['adjusted']['Hispanic'])}x Hispanic, {x(by[c]['adjusted']['White'])}x White women" for c in adj)
                + ". Dallas's model covers non-family assaults on adults only.", height=90 + 38 * len(labels))
    hbars("modelChart", labels, [("Crude", [by[c]["model_crude"][g] for c in adj for g in ("Hispanic", "White")], "C.muted"),
                                 ("Fully adjusted", [by[c]["adjusted"][g] for c in adj for g in ("Hispanic", "White")], "C.red")], "Rate ratio")
    no_loc = [c for c in cities if not by[c]["adjusted"]]
    model_html = ('<div class="section-title">Where neighborhood could be tested</div>'
                  f'<p class="note">Only {listing(adj)} have victim locations. The FBI\'s files for {listing(no_loc)} record none.</p>'
                  + grid([m_box]) +
                  '<div class="findings"><div class="finding red"><h4>Located, not explained away</h4><p>'
                  + esc("Tract poverty, income, jobs and housing are shaped by segregation and disinvestment. Where these controls narrow a gap, the gap has been located in where women live; it has not been explained away.")
                  + "</p></div></div>")

    # city by city table and links
    head = ["City", "Source, years", "Black women, per 100,000", "vs Hispanic", "vs White", "vs Asian", "Lowest bound vs Hispanic", "Lowest bound vs White"]
    trs = "".join(f'<tr><td><a href="{esc(by[c]["page"])}">{esc(c)}</a></td><td>{esc(by[c]["source"])}, {esc(by[c]["window"])}</td><td>{rate[c]:,}</td>'
                  f'<td>{vsH[c]}x</td><td>{vsW[c]}x</td><td>{by[c]["ratio"]["Asian"]}x</td><td>{lowH[c]}x</td><td>{lowW[c]}x</td></tr>' for c in cities)
    table = ('<style>.tbl-wrap{overflow-x:auto;margin-bottom:40px;border:1px solid var(--border);border-radius:8px}'
             '.tbl{border-collapse:collapse;width:100%;font-size:12px;min-width:720px}.tbl th,.tbl td{padding:9px 12px;border-bottom:1px solid var(--border);text-align:right;white-space:nowrap}'
             '.tbl th:first-child,.tbl td:first-child,.tbl th:nth-child(2),.tbl td:nth-child(2){text-align:left}.tbl th{color:var(--muted);font-weight:600;font-size:11px}'
             '.tbl tr:last-child td{border-bottom:none}</style>'
             '<div class="section-title">City by city</div>'
             '<p class="note">Each city links to its own analysis. The lowest bound assumes every multiracial Black resident is recorded as Black and the least favorable reading of missing ethnicity.</p>'
             f'<div class="tbl-wrap"><table class="tbl"><thead><tr>{"".join(f"<th>{esc(h)}</th>" for h in head)}</tr></thead><tbody>{trs}</tbody></table></div>')
    reporting = ('<div class="findings"><div class="finding"><h4>Reporting: not testable here</h4><p>'
                 + esc("Police data holds only what was reported. If Black women report assaults more or less often than other women, every ratio here moves, and this data cannot say which way.")
                 + "</p></div></div>" + table)

    # caveats
    cav = [
        ("This shows what, not why", "The data says Black women are assaulted at a higher reported rate in each of these cities. It does not say why. Nothing here measures causes, offenders or circumstances."),
        ("Reported crimes only", "Every number is a report that reached the police. Willingness to report, and recording practice, differ by group, area, city and time."),
        ("Reports, not people", "Rates count reports. Someone assaulted twice counts twice, so a rate is not the share of people assaulted."),
        ("Exposure is not population", "Rates divide by where people live, not where they spend time."),
        ("Policing and reporting", "Police data reflects where officers patrol and who calls them. This data cannot separate more policing or more reporting from more assaults."),
        ("Sources differ by city", " ".join(f"{c} uses {SOURCE_PROSE.get(by[c]['source'], by[c]['source'])} ({by[c]['window']})." for c in cities if by[c]['source'] != 'FBI NIBRS')
                                   + f" {listing(c for c in cities if by[c]['source'] == 'FBI NIBRS')} use the FBI's NIBRS files. Offense definitions are close but not identical, so compare patterns across cities, not levels."),
        ("Five cities had lighter checks", f"{listing(NEW)} ran on the FBI's files alone, with the decisions made for Dallas. Each has all {min(by[c]['months'] for c in NEW)} months of data, "
                                           f"and race is unknown or outside the compared groups for {min(unk_new)}% to {max(unk_new)}% of women victims. There is no location test, no second source and no city-specific check like Dallas's."),
        ("Who is recorded as Black", f"Race is recorded by officers; the Census counts people who are Black alone. Across these cities, {min(combo)}% to {max(combo)}% more residents are Black alone or in combination. "
                                     "The lowest bounds assume every one of them is recorded as Black."),
        ("Hispanic ethnicity", f"Unknown or unspecified ethnicity runs from {eth[c_eth_lo]}% of women victims in {c_eth_lo} to {eth[c_eth_hi]}% in {c_eth_hi}. "
                               "Where it is high the Hispanic comparison is uncertain" + (", and in " + listing(fail_H) + " it cannot be settled" if fail_H else "")
                               + ". Los Angeles records Hispanic as a descent code, not a separate field."),
        ("Agencies", "Each city counts its own police department only. Assaults recorded only by transit, school, campus, hospital or county police are missing."),
        ("Small numbers", f"El Paso's figures rest on {ep['women_victims']['Black']:,} Black women victims and about {round(ep['black_women_pop'], -3):,.0f} Black women residents. "
                          f"Asian women's counts are small in most cities, as few as {asian[c_as_lo]:,} in {c_as_lo}, so their ratios stay out of the headline."),
        ("Windows differ", f"{listing(c + ' covers ' + by[c]['window'] for c in cities if by[c]['window'] != '2022 to 2025')}; the rest cover 2022 to 2025. Populations are ACS 2020 to 2024 five-year estimates."),
        ("Not a national sample", f"Nine large cities, {WORDS[sum(1 for c in cities if c in NEW + ['Dallas'])]} of them in Texas, chosen because their data was available. They show a consistent pattern in police data; they do not measure a national rate or a trend."),
    ]
    cav_html = '<div class="section-title">Caveats</div><div class="findings">' + "".join(f'<div class="finding red"><h4>{esc(h)}</h4><p>{esc(t)}</p></div>' for h, t in cav) + "</div>"

    cards = [("Cities", str(len(cities)), f"{sum(1 for c in cities if c in NEW + ['Dallas'])} in Texas"), ("Victims", f"{total:,}", "all groups, both sexes"),
             ("Black women victims", f"{n_focus:,}", "used for rates"), ("Other women victims", f"{n_other:,}", "Hispanic, White and Asian")]
    cards_html = '<div class="cards">' + "".join(f'<div class="card"><div class="label">{esc(l)}</div><div class="value">{v}</div><div class="sub">{esc(s)}</div></div>' for l, v, s in cards) + "</div>"
    nav = f'<a href="{REPO}">Code</a><a href="https://martinngoh.com">martinngoh.com</a>'
    method = ("Rates are women victims of aggravated and simple assault per 100,000 residents of the same group per year. Each city's numbers come from its own analysis, "
              "built with disparity-kit; this page reads them through scripts/compare.py. Sources: FBI National Incident-Based Reporting System (NIBRS) files; "
              "Los Angeles Police Department and Baltimore Police Department records; US Census Bureau ACS five-year estimates via Census Reporter.")
    first = min(int(by[c]["window"][:4]) for c in cities)
    last = max(int(by[c]["window"][-4:]) for c in cities)
    page = TEMPLATE.format(
        title="Assault victims in nine cities", description=esc(lede), lede=esc(lede), author="Martin Ngoh", window=f"{first} to {last}", total=f"{total:,}",
        nav=nav, question=esc(question), answer="".join(f"<p>{esc(a)}</p>" for a in answer), cards=cards_html,
        overview=grid([rates_box]) + grid([w_box, h_box]), tests=grid([sev_box, age_box, p_box, t_box]), reporting=reporting, model=model_html,
        replication="", caveats=cav_html, method=esc(method), js="\n  ".join(js), groups_n=f"{n_focus:,}", others_n=f"{n_other:,}",
        focus="Black women", sexw="women", sexw_cap="Women")
    for bad in ["—", "–"]:
        page = page.replace(bad, ", " if bad == "—" else " to ")
    (ROOT / "index.html").write_text(page)
    print("wrote", ROOT / "index.html")

    # README block
    L = ["<!-- results:start -->", f"**{lede}**", "", "Live page: https://mngoh.github.io/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/", "",
         "| City | Source, years | Black women, per 100,000 | vs Hispanic | vs White | Lowest bound vs Hispanic | Lowest bound vs White |", "|---|---|---|---|---|---|---|"]
    L += [f"| [{c}]({by[c]['page']}) | {by[c]['source']}, {by[c]['window']} | {rate[c]:,} | {vsH[c]}x | {vsW[c]}x | {lowH[c]}x | {lowW[c]}x |" for c in cities]
    L += [""] + [a for a in answer] + ["", "Caveats:", ""] + [f"- {h}: {t}" for h, t in cav] + ["<!-- results:end -->"]
    block = "\n".join(L)
    rd = ROOT / "README.md"
    s = rd.read_text()
    if "<!-- results:start -->" in s:
        a, b = s.index("<!-- results:start -->"), s.index("<!-- results:end -->") + len("<!-- results:end -->")
        s = s[:a] + block + s[b:]
    else:
        s = s.replace("## Method", "## Results\n\n" + block + "\n\n## Method", 1)
    rd.write_text(s)
    print("updated README results block")


if __name__ == "__main__":
    main()
