"""
Project: Spotify-ETL-Pipeline
Author: Zaya (gzaiyu1209)
Description: Data Extraction layer using Spotify Web API.
Status: Validated and Tested
"""
import requests
import datetime
import base64

# --- Configuration (Sensitive info omitted for security) ---
CLIENT_ID = "" 
CLIENT_SECRET = "" 
TOKEN = ""

def get_auth_token():
    """
    Implements Client Credentials Flow for service-level access.
    Note: For user-specific playback data, Authorization Code Flow is preferred.
    """
    if not CLIENT_ID or not CLIENT_SECRET:
        return TOKEN

    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_base64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status() # 自动检查 4xx/5xx 错误
        return response.json().get("access_token")
    except Exception as e:
        print(f"Auth Error: {e}")
        return TOKEN

def fetch_spotify_tracks():
    """
    Extract Phase: Fetches listening history from the last 24 hours.
    Mathematical Context: Time Interval [T-24h, Now]
    """
    current_token = TOKEN if TOKEN else get_auth_token()

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {current_token}"
    }

    # Calculate Unix timestamp in milliseconds for the last 24 hours
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    # Official Spotify Endpoint
    url = f"https://api.spotify.com/v1/me/player/recently-played?after={yesterday_unix_timestamp}"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("Error: Unauthorized. Check if Token is expired.")
            return None
        else:
            print(f"Extraction Failed: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"Network Topology Error: {e}")
        return None

if __name__ == "__main__":
    data = fetch_spotify_tracks()
    if data:
        print(f"Successfully fetched {len(data.get('items', []))} tracks!")