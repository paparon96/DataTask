## I. Import libraries
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from flask import Flask, request, render_template, session, redirect
import datetime

## II. Create engine object to be able to connect to the database
engine = create_engine('postgresql://postgres@localhost:5432/task_data')

## III. Extract data from the PostgreSQL tables
df = pd.read_sql_table("measurements", con=engine)

## IV. Create web application

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=(["GET"]))

def logging_and_html_table():

    # Log GET requests
    if request.method == "GET":
        log_dict = {"request_type":request.method, "time_stamp":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}

        # Export logs to the database
        con = psycopg2.connect("dbname=task_data  user=postgres host=localhost")
        cur = con.cursor()
        q = "INSERT INTO get_request_logs VALUES(%(request_type)s, %(time_stamp)s)"
        cur.execute(q, log_dict)
        con.commit()
        con.close()

    # Display the data as a simple table in html
    # Reference for this display: https://stackoverflow.com/questions/52644035/how-to-show-a-pandas-dataframe-into-a-existing-flask-html-table
    return render_template('./simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


## V. Run the web application
if __name__ == '__main__':
    app.run(host='0.0.0.0')
