import joblib 
import streamlit as st
from datetime import date,timedelta,datetime,time
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title('**Time Series Forcasting**')
model2 = joblib.load('Var.joblib')
print(1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
with st.sidebar:
    startdate = st.date_input("**Start Date**",min_value=date.today())
    enddate = st.date_input("**End Date**",min_value=startdate,max_value=startdate+timedelta(days=6),value= None)
    
if startdate and enddate:
    indexrange = []
    current_date = startdate
    while current_date <= enddate:
        indexrange += pd.date_range(start=datetime.combine(current_date, time(9, 15)),
                                    end=datetime.combine(current_date, time(15, 15)),
                                    freq='T').tolist()
        current_date += timedelta(days=1)
    if st.sidebar.button('**Start Prediction**'):
        predictions4=model2.forecast(y=model2.endog, steps=len(indexrange),exog_future=model2.exog[:len(indexrange)])
        columns = ["Open","High","Low","Close","Adj Close"]
        st.subheader('**DataFrame for prediction**',divider=True)
        df = pd.DataFrame(predictions4,index=indexrange,columns=columns)
        st.write(df)
        st.subheader("Prediction chart",divider=True)
        plt.figure(figsize=(15,7))
        line=px.line(data_frame=df,x=df.index,y=df.columns,title="NIFTY-50 Stock Prices")
        line.show()
        st.plotly_chart(line)
    

    

