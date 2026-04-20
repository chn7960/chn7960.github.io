"""Generate _talks, _portfolio, _teaching markdown files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TALKS = [
    dict(
        slug="2022-plea-droplet-diffusion",
        date="2022-11-01",
        title="Analysis of the effect of droplet diffusion (COVID-19 surrogate) according to the use of portable air purifier under cooling conditions in summer",
        venue="PLEA 2022",
        location="Santiago, Chile",
        type="Conference paper",
        authors="Na, H., <b>Choi, H.</b>, Lee, Y., & Kim, T.",
    ),
    dict(
        slug="2021-kieae-thermal-comfort-prediction",
        date="2021-11-01",
        title="Comparison of the performance of several data-driven prediction models using small-sized thermal comfort datasets",
        venue="KIEAE 2021",
        location="Seoul, Republic of Korea",
        type="Conference paper",
        authors="Kim, J. J., <b>Choi, H.</b>, Jeong, B., & Kim, T.",
    ),
    dict(
        slug="2020-kieae-shading-lighting",
        date="2020-11-01",
        title="A review of integrated automatic shading and lighting control strategies",
        venue="KIEAE 2020",
        location="Seoul, Republic of Korea",
        type="Conference paper",
        authors="Um, C. Y., <b>Choi, H.</b>, & Kim, T.",
    ),
    dict(
        slug="2019-building-simulation-sdsf-cfd",
        date="2019-09-01",
        title="Analysis of heat transfer in a slim double skin facade using CFD simulation",
        venue="16th International IBPSA Conference (Building Simulation 2019)",
        location="Rome, Italy",
        type="Conference paper",
        authors="<b>Choi, H.</b>, Kang, K., An, Y., Kim, E., Lee, Y., & Kim, T.",
    ),
    dict(
        slug="2019-iaqvec-ventilation-pm",
        date="2019-09-01",
        title="An effective ventilation system for preventing indoor PM2.5 dispersion",
        venue="10th International Conference on IAQVEC",
        location="Bari, Italy",
        type="Conference paper",
        authors="Park, H., <b>Choi, H.</b>, Kang, K. M., Kim, H. K., & Kim, T.",
    ),
    dict(
        slug="2019-sbe-sdsf-cooling",
        date="2019-08-01",
        title="Cooling load reduction effect in slim double skin facade (SDSF)",
        venue="Sustainable Built Environment Conference 2019",
        location="Tokyo, Japan",
        type="Conference paper",
        authors="Kang, K., Kim, T., <b>Choi, H.</b>, An, Y., & Kim, E.",
    ),
    dict(
        slug="2018-aivc-cfd-adsorption",
        date="2018-09-01",
        title="CFD analysis of the optimal installation location of adsorption material in two ventilation conditions in residential buildings: natural convection and mechanical ventilation",
        venue="39th AIVC Conference",
        location="Antibes Juan-Les-Pins, France",
        type="Conference paper",
        authors="<b>Choi, H.</b>, Kim, D., & Kim, T.",
    ),
]

PORTFOLIO = [
    # KIER (PI)
    dict(
        slug="kier-autonomous-building-energy",
        title="Autonomous Operation-based Integrated Building Energy & Environment Management System",
        excerpt="Principal Investigator · KIER internal R&D · 2024.04 – 2024.12 · ₩400M. Development and field validation at KIER Building No. 3.",
        period="2024.04 – 2024.12",
        sponsor="Korea Institute of Energy Research (KIER)",
        role="Principal Investigator",
    ),
    dict(
        slug="kier-energy-efficiency-program-2025",
        title="2025 Analysis and Field-based Enhancement of the National Energy-Efficiency Program",
        excerpt="Principal Investigator · Korea Energy Foundation · 2024.06 – 2025.02 · ₩222.7M.",
        period="2024.06 – 2025.02",
        sponsor="Korea Energy Foundation",
        role="Principal Investigator",
    ),
    dict(
        slug="kier-energy-efficiency-program-2024",
        title="2024 Analysis and Field-based Enhancement of the National Energy-Efficiency Program",
        excerpt="Principal Investigator · Korea Energy Foundation · 2025.05 – 2025.12 · ₩145M.",
        period="2025.05 – 2025.12",
        sponsor="Korea Energy Foundation",
        role="Principal Investigator",
    ),
    # Graduate school
    dict(
        slug="grad-vision-occupant-sensing",
        title="Vision-based Occupant Information Sensing Technology",
        excerpt="Doctoral research project at Yonsei AE Lab.",
        period="2017 – 2020",
        sponsor="National Research Foundation of Korea (NRF)",
        role="Researcher",
    ),
    dict(
        slug="grad-occupant-centric-hvac",
        title="Occupant-Centric HVAC Control Strategies and Field Demonstration",
        excerpt="Development and demonstration of occupant-centric HVAC control, leading to the dissertation.",
        period="2020 – 2022",
        sponsor="Korea Institute of Energy Technology Evaluation and Planning (KETEP)",
        role="Researcher",
    ),
    dict(
        slug="grad-mrt-kuwait-ac",
        title="MRT-based Air-Conditioning Control Algorithm for Kuwait",
        excerpt="Machine-learning based mean radiant temperature prediction for cooling control under Kuwaiti climate.",
        period="2019 – 2021",
        sponsor="Korea Testing and Research Institute (KTR)",
        role="Researcher",
    ),
    dict(
        slug="grad-slim-double-skin-window",
        title="Slim Double-Skin Window: Heat Transfer Analysis & Energy Demonstration",
        excerpt="Experimental + CFD analysis of a naturally-ventilated slim double-skin window, field-validated on a remodeled building.",
        period="2017 – 2018",
        sponsor="Kolon Global",
        role="Researcher",
    ),
    dict(
        slug="grad-pm25-school-classrooms",
        title="Supply-Ventilation Strategies to Reduce PM2.5 in School Classrooms",
        excerpt="CFD-based evaluation of ventilation strategies to mitigate particulate matter in naturally-ventilated school classrooms.",
        period="2020 – 2021",
        sponsor="National Research Foundation of Korea (NRF)",
        role="Researcher",
    ),
    dict(
        slug="grad-toluene-adsorption-apartments",
        title="Optimal Installation Algorithm for Toluene-Adsorption Material in Residential Buildings",
        excerpt="Numerical modeling (CRPS) + CFD to evaluate adsorption material placement strategies in small apartments.",
        period="2017 – 2020",
        sponsor="Korea Agency for Infrastructure Technology Advancement (KAIA)",
        role="Researcher",
    ),
]

TEACHING = [
    dict(
        slug="2022-daejin-guest-lecturer",
        title="Architectural Environment and Mechanical Systems",
        role="Guest Lecturer",
        venue="Daejin University",
        period="2022.05",
        excerpt="Guest lecture on thermal comfort and HVAC controls.",
    ),
    dict(
        slug="2021-kict-contam-educator",
        title="CONTAM Simulation Tool Training",
        role="Tool Educator",
        venue="KICT (Korea Institute of Civil Engineering and Building Technology)",
        period="2021.09",
        excerpt="Instructor-led CONTAM training for building environment researchers.",
    ),
    dict(
        slug="2020-yonsei-contam-educator",
        title="CONTAM Simulation Tool Training (YouTube)",
        role="Tool Educator",
        venue="Yonsei University (ARC3210-01)",
        period="Spring 2020",
        excerpt="Pre-recorded video course on CONTAM for architectural environment students.",
    ),
    dict(
        slug="2017-2018-yonsei-ta",
        title="Teaching Assistant — Architecture & Engineering Courses",
        role="Teaching Assistant",
        venue="Yonsei University",
        period="2017 – 2018",
        excerpt="TA for ARC2302-01, ENG1108-02, ARC4204-01, ARC2204-01.",
    ),
    dict(
        slug="2017-yonsei-ose-tutor",
        title="Tutor — ARC3210-01, ARC3204-01",
        role="Tutor",
        venue="Yonsei University OSE Center",
        period="Spring 2017",
        excerpt="Peer tutoring at the Office of Student Engagement.",
    ),
]


def write_talks():
    out = ROOT / "_talks"
    out.mkdir(exist_ok=True)
    for t in TALKS:
        path = out / f'{t["slug"]}.md'
        front = [
            "---",
            f'title: "{t["title"]}"',
            "collection: talks",
            f'type: "{t["type"]}"',
            f'permalink: /talks/{t["slug"]}',
            f'venue: "{t["venue"]}"',
            f'date: {t["date"]}',
            f'location: "{t["location"]}"',
            "lang: en",
            f'ref: talk-{t["slug"]}',
            "---",
            "",
            f'**Authors**: {t["authors"]}',
            "",
        ]
        path.write_text("\n".join(front), encoding="utf-8")
        print(f"talk: {path.name}")


def write_portfolio():
    out = ROOT / "_portfolio"
    out.mkdir(exist_ok=True)
    for p in PORTFOLIO:
        path = out / f'{p["slug"]}.md'
        front = [
            "---",
            f'title: "{p["title"]}"',
            "collection: portfolio",
            f'excerpt: "{p["excerpt"]}"',
            f'permalink: /portfolio/{p["slug"]}',
            "lang: en",
            f'ref: portfolio-{p["slug"]}',
            "---",
            "",
            f'**Role**: {p["role"]}  ',
            f'**Period**: {p["period"]}  ',
            f'**Sponsor**: {p["sponsor"]}',
            "",
        ]
        path.write_text("\n".join(front), encoding="utf-8")
        print(f"portfolio: {path.name}")


def write_teaching():
    out = ROOT / "_teaching"
    out.mkdir(exist_ok=True)
    for t in TEACHING:
        path = out / f'{t["slug"]}.md'
        front = [
            "---",
            f'title: "{t["title"]}"',
            "collection: teaching",
            f'type: "{t["role"]}"',
            f'permalink: /teaching/{t["slug"]}',
            f'venue: "{t["venue"]}"',
            f'date: "{t["period"]}"',
            f'excerpt: "{t["excerpt"]}"',
            "lang: en",
            f'ref: teaching-{t["slug"]}',
            "---",
            "",
        ]
        path.write_text("\n".join(front), encoding="utf-8")
        print(f"teaching: {path.name}")


if __name__ == "__main__":
    write_talks()
    write_portfolio()
    write_teaching()
    print(f"totals: talks={len(TALKS)}, portfolio={len(PORTFOLIO)}, teaching={len(TEACHING)}")
