# 🎧 Spotify ETL Pipeline

A data engineering project that extracts personal listening history from Spotify, transforms it into a structured format, and loads it into a MySQL database for analysis.

---

## 🚀 Project Overview

This project implements a complete ETL (Extract, Transform, Load) pipeline using the Spotify Web API.

* **Extract**: Fetch recently played tracks from Spotify API
* **Transform**: Clean and validate data using Pandas
* **Load**: Store structured data into MySQL database

> ⚠️ Note: This project currently uses manually generated access tokens for development and testing purposes. Future versions will implement OAuth Authorization Code Flow with refresh token support.

---

## 🏗️ Architecture

```mermaid
graph TD
    A[Spotify Web API] --> B[Extract Layer (Python)]
    B --> C[Transform Layer (Pandas)]
    C --> D[Data Validation]
    D --> E[MySQL Database]
```

---

## 📊 Data Schema

```sql
CREATE TABLE my_played_tracks (
    song_name VARCHAR(200) NOT NULL,
    artist_name VARCHAR(200),
    played_at VARCHAR(200) PRIMARY KEY,
    timestamp DATE
);
```

* `played_at` is used as the primary key to prevent duplicate records
* Indexing is applied on timestamp for efficient querying

---

## ⚙️ Tech Stack

* Python
* Pandas
* SQLAlchemy
* MySQL
* Spotify Web API

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/Zaya-M/Spotify-ETL-Pipeline.git
cd Spotify-ETL-Pipeline
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file and add:

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
TOKEN=your_access_token
```

---

### 4. Configure database

Update the database connection string in the code:

```python
DATABASE_LOCATION = "mysql+pymysql://user:password@localhost/spotify_db"
```

---

### 5. Run the ETL pipeline

```
python main.py
```

---

## ✅ Data Validation

The pipeline includes built-in validation checks:

* Ensures dataset is not empty
* Enforces primary key uniqueness (`played_at`)
* Detects null values for data quality assurance

---

## 📌 Future Improvements

* Implement OAuth Authorization Code Flow (with refresh token)
* Automate pipeline scheduling (cron / Airflow)
* Add data visualization (e.g., Spotify Wrapped analysis)
* Deploy pipeline to cloud environment (AWS / GCP)

---

## 👤 Author

Zaya (Zaya-M)
