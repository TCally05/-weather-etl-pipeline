from src.extract import extract_weather
from src.transform import transform_weather
from src.load import load_weather, query_preview

def run_pipeline():
    """
    Runs the full ETL pipeline:
    1. Extract — fetch raw weather data from the API
    2. Transform — clean and enrich the data
    3. Load — save to SQLite database
    4. Preview — print a quick sample to the terminal
    """

    print("=" * 50)
    print("  Weather ETL Pipeline")
    print("=" * 50)

    # Step 1: Extract
    raw_df = extract_weather()

    # Step 2: Transform
    clean_df = transform_weather(raw_df)

    # Step 3: Load
    load_weather(clean_df)

    # Step 4: Quick preview in terminal
    query_preview()

    print("=" * 50)
    print("Pipeline complete!")


if __name__ == "__main__":
    run_pipeline()
