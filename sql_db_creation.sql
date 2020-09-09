DROP DATABASE task_data;
CREATE DATABASE task_data ;
\c task_data;

CREATE TABLE measurements (
measurement_id INTEGER PRIMARY KEY,
time_stamp TIMESTAMP,
temperature FLOAT,
duration INTERVAL
);

CREATE TABLE get_request_logs (
request_type VARCHAR,
time_stamp TIMESTAMP PRIMARY KEY
);
