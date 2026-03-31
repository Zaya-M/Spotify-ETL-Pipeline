import pandas as pd
import sqlalchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker

# 数据库连接配置 （MySQL） 
DATABASE_LOCATION = "mysql+pymysql://user:yourpassword@localhost/spotify_db"

# 数据加载 (Load): 通过 SQL Alchemy ORM 将处理后的数据持久化至数据库

def load_to_database(df: pd.DataFrame):
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    
    try:
        # 使用 append 模式，如果数据已存在则基于主键约束跳过或处理冲突
        df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
        print("Data successfully loaded to MySQL.")
    except Exception as e:
        print(f"Load Error: Possible duplicate data or connection issue. {e}")