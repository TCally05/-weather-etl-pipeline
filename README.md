# Weather ETL Pipeline

A Python data pipeline that extracts hourly weather data from
the Open-Meteo API, transforms it with pandas, and loads it
into a SQLite database for analysis.

## What it does
- Extracts: fetches temperature, wind speed, and humidity
  for Honolulu, HI from the Open-Meteo free API (no key needed)
- Transforms: cleans nulls, converts units, adds timestamps
- Loads: stores clean data in a local SQLite database

## Tech stack
Python · pandas · SQLite · SQLAlchemy · requests

## How to run it
1. Clone this repo
2. Create a virtual environment: python -m venv venv
3. Activate it: source venv/bin/activate
4. Install dependencies: pip install -r requirements.txt
5. Run the pipeline: python main.py

## Project structure
src/extract.py   — API fetch logic
src/transform.py — pandas cleaning
src/load.py      — database write
main.py          — runs the full ETL

## What I learned
[Write 2-3 sentences about what clicked for you — 
pipeline design, pandas, SQL schema, etc.]
