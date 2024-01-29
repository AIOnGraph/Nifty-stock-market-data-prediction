import joblib 
import streamlit as st
from datetime import date,timedelta,datetime,time
import pandas as pd
import plotly.graph_objects as go

st.title('**Time Series Forcasting**')
model2 = joblib.load('Var.joblib')
with st.sidebar:
    startdate = st.date_input("Enter start date",min_value=date.today())
    enddate = st.date_input("Enter the end ate",max_value=startdate+timedelta(days=7),value= None)
    
if startdate and enddate:
    indexrange = []
    current_date = startdate
    while current_date <= enddate:
        indexrange += pd.date_range(start=datetime.combine(current_date, time(9, 15)),
                                    end=datetime.combine(current_date, time(15, 29)),
                                    freq='T').tolist()
        current_date += timedelta(days=1)
    predictions4=model2.forecast(y=model2.endog, steps=len(indexrange),exog_future=model2.exog[:len(indexrange)])
    columns = ["Open","High","Low","Close","Adj Close"]
    st.subheader('**DataFrame for prediction**',divider=True)
    df = pd.DataFrame(predictions4,index=indexrange,columns=columns)
    st.write(df)
    st.subheader("Prediction chart",divider=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
    fig.update_layout(xaxis_title='Date',
                    yaxis_title='Close',
                    showlegend=True,)
    st.plotly_chart(fig)
    data=pd.DataFrame(df.index)

