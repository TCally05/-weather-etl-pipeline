import pandas as pd

def transform_weather(df):
    """
    Cleans and transforms the raw weather DataFrame.
    - Converts timestamp strings to real datetime objects
    - Drops any rows with missing values
    - Adds a 'feels_like' comfort label column
    - Adds a 'loaded_at' column so we know when this ran
    Returns a clean pandas DataFrame ready to load.
    """

    print("Transforming data...")

    # Make a copy so we don't modify the original
    df = df.copy()

    # Convert the timestamp string (e.g. "2024-01-01T00:00") to a real datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Drop rows where any value is missing
    before = len(df)
    df = df.dropna()
    after = len(df)
    if before != after:
        print(f"  Dropped {before - after} rows with missing values.")

    # Add a human-readable comfort label based on temperature
    def comfort_label(temp_f):
        if temp_f >= 90:
            return "Hot"
        elif temp_f >= 75:
            return "Warm"
        elif temp_f >= 60:
            return "Comfortable"
        elif temp_f >= 45:
            return "Cool"
        else:
            return "Cold"

    df["comfort"] = df["temperature_f"].apply(comfort_label)

    # Record when this pipeline ran
    df["loaded_at"] = pd.Timestamp.now()

    # Round floats to 2 decimal places for cleanliness
    df["temperature_f"] = df["temperature_f"].round(2)
    df["wind_speed_mph"] = df["wind_speed_mph"].round(2)

    print(f"  Transformed {len(df)} clean rows.")
    return df
