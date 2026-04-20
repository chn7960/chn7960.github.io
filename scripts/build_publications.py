"""One-shot generator for _publications/*.md from achievements.md.

Run: python scripts/build_publications.py
Re-runnable: overwrites files with matching slugs.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_publications"
OUT.mkdir(exist_ok=True)

# Legend for `category`: manuscripts | conferences | domestic
# `first_author` toggles bold rendering for "Choi, H." in citation
PUBS = [
    # ======= 2026 =======
    dict(
        slug="2026-empirical-occupant-participatory-geb",
        date="2026-01-01",
        title="Empirical evaluation of an occupant-participatory schedule-based control for GHP cooling systems",
        venue="Energy and Buildings",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., ..., & Kim, T.",
        year=2026,
    ),
    dict(
        slug="2026-practical-demand-flexibility-geb",
        date="2026-01-01",
        title="A practical control strategy for demand flexibility with ensured occupant comfort in GEB",
        venue="Energy and Buildings",
        category="manuscripts",
        first_author=False,
        authors="..., Choi, H., ...",
        year=2026,
    ),
    # ======= 2025 =======
    dict(
        slug="2025-gpt4o-korean-exams",
        date="2025-06-01",
        title="Performance evaluation of GPT-4o on South Korean national exams for building mechanical equipment maintenance",
        venue="Scientific Reports",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., Lee, J., & Kim, J.",
        year=2025,
    ),
    dict(
        slug="2025-geb-korean-standards",
        date="2025-01-01",
        title="Analysis of domestic building energy design standards and certification for Grid-interactive Efficient Buildings (GEB)",
        venue="Korean Journal of Air-Conditioning and Refrigeration Engineering",
        category="domestic",
        first_author=True,
        authors="Choi, H., Han, S., & Kim, J.",
        year=2025,
    ),
    dict(
        slug="2025-range-hood-pm25",
        date="2025-03-01",
        title="Effect of a range hood with make-up air-supply system for indoor PM2.5",
        venue="Air Quality, Atmosphere & Health",
        category="manuscripts",
        first_author=False,
        authors="..., Choi, H., ...",
        year=2025,
    ),
    dict(
        slug="2025-data-driven-demand-flexibility",
        date="2025-09-01",
        title="A scalable data-driven framework for demand flexibility in commercial building clusters",
        venue="Journal of Building Engineering",
        category="manuscripts",
        first_author=False,
        authors="..., Choi, H., ...",
        year=2025,
    ),
    # ======= 2024 =======
    dict(
        slug="2024-mrt-machine-learning",
        date="2024-06-01",
        title="Field test of machine-learning based mean radiant temperature estimation methods",
        venue="Energy Reports",
        category="manuscripts",
        first_author=False,
        authors="..., Choi, H., ...",
        year=2024,
    ),
    dict(
        slug="2024-bim-ar-evacuation",
        date="2024-11-01",
        title="BIM-based augmented reality navigation for indoor emergency evacuation",
        venue="Expert Systems with Applications",
        category="manuscripts",
        first_author=False,
        authors="..., Choi, H., ...",
        year=2024,
    ),
    # ======= 2023 =======
    dict(
        slug="2023-indoor-air-noise-classrooms",
        date="2023-06-01",
        title="Optimizing indoor air quality and noise levels in old school classrooms with air purifiers and HRV: A CONTAM simulation study",
        venue="Journal of Building Engineering",
        category="manuscripts",
        first_author=False,
        authors="Na, H., Choi, H., Kim, H., & Kim, T.",
        year=2023,
    ),
    dict(
        slug="2023-fire-detection-cctv",
        date="2023-03-01",
        title="Development of early fire detection model for buildings using computer vision-based CCTV",
        venue="Journal of Building Engineering",
        category="manuscripts",
        first_author=False,
        authors="Ahn, Y., Choi, H., & Kim, B. S.",
        year=2023,
    ),
    # ======= 2022 =======
    dict(
        slug="2022-deep-vision-metabolic-rate",
        date="2022-08-01",
        title="Deep-vision-based metabolic rate and clothing insulation estimation for occupant-centric control",
        venue="Building and Environment",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., Jeong, B., Lee, J., Na, H., Kang, K., & Kim, T.",
        year=2022,
    ),
    dict(
        slug="2022-deep-vision-occupancy-counting",
        date="2022-10-01",
        title="Deep vision-based occupancy counting: Experimental performance evaluation and implementation of ventilation control",
        venue="Building and Environment",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., Lee, J., Yi, Y., Na, H., Kang, K., & Kim, T.",
        year=2022,
    ),
    dict(
        slug="2022-iot-rl-fire-evacuation",
        date="2022-02-01",
        title="Development of a real-time safest evacuation route using IoT and reinforcement learning in case of fire in a building",
        venue="Journal of the Korean Society of Safety",
        category="domestic",
        first_author=True,
        authors="Ahn, Y., & Choi, H.",
        year=2022,
    ),
    dict(
        slug="2022-slim-double-skin-remodeling",
        date="2022-10-01",
        title="Empirical analysis of the effects of window remodeling using the slim double-skin window on thermal properties of old buildings",
        venue="Energy and Buildings",
        category="manuscripts",
        first_author=False,
        authors="An, Y., Choi, H., Kim, E., Kang, K., Kim, S., & Kim, T.",
        year=2022,
    ),
    dict(
        slug="2022-slim-double-skin-seasonal",
        date="2022-02-01",
        title="Experimental analysis of seasonal temperature characteristics and cooling/heating energy consumption of a slim double-skin window",
        venue="Energy and Buildings",
        category="manuscripts",
        first_author=False,
        authors="An, Y., Choi, H., Kim, E., & Kim, T.",
        year=2022,
    ),
    dict(
        slug="2022-occupant-behavior-daycare",
        date="2022-04-01",
        title="Occupant behavior and indoor particulate concentrations in daycare centers",
        venue="Science of The Total Environment",
        category="manuscripts",
        first_author=False,
        authors="Um, C. Y., Zhang, N., Kang, K., Na, H., Choi, H., & Kim, T.",
        year=2022,
    ),
    # ======= 2021 =======
    dict(
        slug="2021-vision-occupancy-deep-learning",
        date="2021-10-01",
        title="Application of vision-based occupancy counting method using deep learning and performance analysis",
        venue="Energy and Buildings",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., Um, C. Y., Kang, K., Kim, H., & Kim, T.",
        year=2021,
    ),
    dict(
        slug="2021-review-vision-occupant-sensing",
        date="2021-08-01",
        title="Review of vision-based occupant information sensing systems for occupant-centric control",
        venue="Building and Environment",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., Um, C. Y., Kang, K., Kim, H., & Kim, T.",
        year=2021,
    ),
    dict(
        slug="2021-vision-clothing-insulation",
        date="2021-08-01",
        title="Vision-based estimation of clothing insulation for building control: A case study of residential buildings",
        venue="Building and Environment",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., Na, H., Kim, T., & Kim, T.",
        year=2021,
    ),
    dict(
        slug="2021-pmv-hvac-mrt-kuwait",
        date="2021-11-01",
        title="Development of novel PMV-based HVAC control strategies using a mean radiant temperature prediction model by machine learning in Kuwaiti climate",
        venue="Building and Environment",
        category="manuscripts",
        first_author=False,
        authors="Park, J., Choi, H., Kim, D., & Kim, T.",
        year=2021,
    ),
    # ======= 2020 =======
    dict(
        slug="2020-ventilation-pm25-classrooms",
        date="2020-09-01",
        title="Development of supply ventilation strategy to reduce PM2.5 in school classrooms",
        venue="Journal of the Architectural Institute of Korea",
        category="domestic",
        first_author=True,
        authors="Choi, H., Lee, J., Jia, R., Kim, D., Na, H., & Kim, T.",
        year=2020,
    ),
    dict(
        slug="2020-cfd-circular-ventilation",
        date="2020-10-01",
        title="Evaluating natural ventilation performance of the circular ventilation window using CFD simulation",
        venue="Journal of the Architectural Institute of Korea",
        category="domestic",
        first_author=True,
        authors="Choi, H., Na, H., Jia, R., Kim, H., Kim, N., & Kim, T.",
        year=2020,
    ),
    dict(
        slug="2020-cfd-toluene-adsorption",
        date="2020-12-01",
        title="Performance evaluation of toluene adsorption material installation locations using CFD in small apartments",
        venue="KIEAE Journal",
        category="domestic",
        first_author=True,
        authors="Choi, H., Zhang, N., Kim, D., & Kim, T.",
        year=2020,
    ),
    dict(
        slug="2020-metabolic-rate-image-deep-learning",
        date="2020-05-01",
        title="Metabolic rate estimation method using image deep learning",
        venue="Building Simulation",
        category="manuscripts",
        first_author=False,
        authors="Na, H., Choi, H., & Kim, T.",
        year=2020,
    ),
    dict(
        slug="2020-high-clothing-insulation-prediction",
        date="2020-01-01",
        title="Assessment of a real-time prediction method for high clothing thermal insulation using a thermoregulation model and an infrared camera",
        venue="Atmosphere",
        category="manuscripts",
        first_author=False,
        authors="Lee, K., Choi, H., Kim, H., Kim, D. D., & Kim, T.",
        year=2020,
    ),
    # ======= 2019 =======
    dict(
        slug="2019-sdsw-cooling-energy",
        date="2019-10-01",
        title="Cooling energy performance and thermal characteristics of a naturally ventilated slim double-skin window",
        venue="Applied Thermal Engineering",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., An, Y., Kang, K., Yoon, S., & Kim, T.",
        year=2019,
    ),
    dict(
        slug="2019-long-term-pollutant-simulation",
        date="2019-11-01",
        title="Long-term simulation for predicting indoor air pollutant concentration considering pollutant distribution based on the concept of CRPS index",
        venue="Building Simulation",
        category="manuscripts",
        first_author=True,
        authors="Choi, H., Kim, H., & Kim, T.",
        year=2019,
    ),
    dict(
        slug="2019-data-driven-clothing-insulation",
        date="2019-10-01",
        title="Development of a data-driven predictive model of clothing thermal insulation estimation by using advanced computational approaches",
        venue="Sustainability",
        category="manuscripts",
        first_author=False,
        authors="Lee, K., Choi, H., Choi, J. H., & Kim, T.",
        year=2019,
    ),
    # ======= 2017 =======
    dict(
        slug="2017-crps-toluene-residential",
        date="2017-09-01",
        title="Health risk assessment by CRPS and the numerical model for toluene in residential buildings",
        venue="KIEAE Journal",
        category="domestic",
        first_author=True,
        authors="Choi, H., Kim, H., & Kim, T.",
        year=2017,
    ),
]


def format_citation(p):
    authors = p["authors"]
    if p["first_author"]:
        # Replace leading "Choi, H." with bold
        authors = authors.replace("Choi, H.", "<b>Choi, H.</b>", 1)
    else:
        # Replace mid-list "Choi, H." with bold
        authors = authors.replace("Choi, H.", "<b>Choi, H.</b>")
    return (
        f'{authors} ({p["year"]}). &quot;{p["title"]}.&quot; '
        f'<i>{p["venue"]}</i>.'
    )


def build():
    for p in PUBS:
        path = OUT / f'{p["slug"]}.md'
        front = [
            "---",
            f'title: "{p["title"].replace(chr(34), chr(92) + chr(34))}"',
            "collection: publications",
            f'category: {p["category"]}',
            f'permalink: /publication/{p["slug"]}',
            "excerpt: ''",
            f'date: {p["date"]}',
            f'venue: "{p["venue"]}"',
            f"citation: '{format_citation(p)}'",
            "lang: en",
            f'ref: pub-{p["slug"]}',
            "---",
            "",
        ]
        path.write_text("\n".join(front), encoding="utf-8")
        print(f"wrote {path.name}")
    print(f"total: {len(PUBS)} publications")


if __name__ == "__main__":
    build()
