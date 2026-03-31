from extract import fetch_spotify_tracks
from transform import transform_tracks, validate_data
from load import load_to_database

if __name__ == "__main__":
    print("--- ETL Process Started ---")
    
    # 1. Extract
    print("Step 1: Extracting data from Spotify...")
    raw_data = fetch_spotify_tracks()
    
    if raw_data:
        # 2. Transform
        print("Step 2: Transforming and validating data...")
        df = transform_tracks(raw_data)
        
        if validate_data(df):
            # 3. Load
            print("Step 3: Loading data into Database...")
            load_to_database(df)
            print("--- ETL Process Completed Successfully ---")
    else:
        print("Failed to fetch data. Please check your Token.")