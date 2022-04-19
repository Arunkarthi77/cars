import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import psycopg2
import postgreconnect
sql='SELECT * from cars;'
record=pd.DataFrame(postgreconnect.runquery(sql))
record.columns=['Name','Miles_Per_Gallon','Cylinders','Displacement','Horsepower','Weight_In_Lbs','Acceleration','year','Origin']
st.title('Cars Data - sourced from Heroku')
st.table(record)
