# CORD-19 Research Explorer

## Overview
This project analyzes the CORD-19 metadata dataset to explore trends in COVID-19 research publications. It includes data cleaning, visualization, and an interactive Streamlit app.

## Files
- `explore_data.py` — Data loading and cleaning
- `visualizations.py` — Charts and word cloud
- `app.py` — Streamlit application
- `publications_by_year.png`, `top_journals.png`, etc. — Generated visuals
- `README.md` — This file

## Key Findings
- Most papers were published in 2020–2021.
- Top journals include "The Lancet", "Nature", etc.
- Common words in titles: "COVID", "SARS", "virus", "pandemic".

## Challenges & Learnings
- Handling missing data in `publish_time` and `abstract`.
- Learning Streamlit interactivity with sliders.
- Generating word clouds from textual data.

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run app: `streamlit run app.py`
