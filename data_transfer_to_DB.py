# I. Import packages
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# II. Import data
task_data = pd.read_csv('./task_data.csv')

# Rename columns to be compatible with the names in the PostgreSQL database
task_data.columns = ['measurement_id','time_stamp','temperature','duration']

# III. Transfer the data to the PostgreSQL database
engine = create_engine('postgresql://postgres@localhost:5432/task_data')
task_data.to_sql('measurements', engine,index=False,if_exists='append')
