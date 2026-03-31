/* 底层 Schema 设计与优化:
  1. 定义主键约束确保数据唯一性 (Data Integrity)
  2. 针对查询频繁的字段建立索引优化 (SQL Tuning)
*/

CREATE TABLE IF NOT EXISTS my_played_tracks (
    song_name VARCHAR(200) NOT NULL,
    artist_name VARCHAR(200),
    played_at VARCHAR(200),
    `timestamp` DATE,
    -- 核心逻辑：定义 played_at 为主键，防止 ETL 过程中的重复录入
    CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
);

-- 为时间戳建立索引，支持后续的高级 SQL 趋势分析与窗口函数查询
CREATE INDEX idx_timestamp ON my_played_tracks(`timestamp`);