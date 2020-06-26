import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS user;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE
(
);
""")

staging_songs_table_create = ("""
CREATE TABLE
(
);
""")

songplay_table_create = ("""
CREATE TABLE songplay
(
    songplay_id INTEGER NOT NULL,
    start_time TIMESTAMP NOT NULL sortkey,
    user_id INTEGER NOT NULL distkey,
    level varchar(25) NOT NULL,
    song_id varchar(32) NOT NULL distkey,
    artist_id varchar(32) NOT NULL distkey,
    session_id INTEGER NOT NULL distkey,
    location varchar(124),
    user_agent varchar(256)
)
diststyle KEY;
""")

user_table_create = ("""
CREATE TABLE
(
    user_id INTEGER NOT NULL distkey,
    first_name varchar(64) NOT NULL,
    last_name varchar(64) NOT NULL,
    gender varchar(32),
    level varchar(25) NOT NULL
)
diststyle ALL;
""")

song_table_create = ("""
CREATE TABLE
(
    song_id varchar(32) NOT NULL distkey,
    title varchar(256) NOT NULL,
    artist_id varchar(32) NOT NULL distkey,
    year INTEGER NOT NULL,
    duration DECIMAL(8,2) NOT NULL
)
diststyle ALL;
""")

artist_table_create = ("""
CREATE TABLE
(
    artist_id varchar(32) NOT NULL distkey,
    name varchar(128) NOT NULL,
    location varchar(124),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
)
diststyle ALL;
""")

time_table_create = ("""
CREATE TABLE
(
    start_time TIMESTAMP NOT NULL sortkey,
    hour INTEGER NOT NULL,
    day INTEGER NOT NULL,
    week INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    weekday BOOLEAN NOT NULL
)
diststyle ALL;
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent 
songplay_table_insert = ("""
INSERT INTO songplay
    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT ();
""")

#user_id, first_name, last_name, gender, level 
user_table_insert = ("""
INSERT INTO user
    (user_id, first_name, last_name, gender, level)
    VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ();
""")

#song_id, title, artist_id, year, duration 
song_table_insert = ("""
INSERT INTO user
    (song_id, title, artist_id, year, duration)
    VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ();
""")

#artist_id, name, location, lattitude, longitude 
artist_table_insert = ("""
INSERT INTO artist
    (artist_id, name, location, lattitude, longitude)
    VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ();
""")

#start_time, hour, day, week, month, year, weekday 
time_table_insert = ("""
INSERT INTO artist
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT ();
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
