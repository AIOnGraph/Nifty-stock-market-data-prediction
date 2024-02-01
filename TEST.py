import joblib 
import streamlit as st
from datetime import date,timedelta,datetime,time
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
st.set_page_config(layout="wide",initial_sidebar_state='collapsed',page_icon='📉')
st.title('**Time Series Forcasting**')
prediction_date=st.subheader('**Enter the prediction date in sidebar**',divider=True)
model1=joblib.load('OpenNewAutoReg.joblib')
model2 = joblib.load('HighNewAutoReg.joblib')
model3=joblib.load('LowNewAutoReg.joblib')
model4=joblib.load('CloseNewAutoReg.joblib')
model5=joblib.load('AdjCloseNewAutoReg.joblib')
with st.sidebar:
    startdate = st.date_input("**Start Date**",min_value=date.today())
    enddate = st.date_input("**End Date**",min_value=startdate,max_value=startdate+timedelta(days=370),value= None)
if startdate and enddate:
    prediction_date.empty()
    indexrange = []
    current_date = startdate
    while current_date <= enddate:
        indexrange += pd.date_range(start=datetime.combine(current_date, time(9, 15)),
                                    end=datetime.combine(current_date, time(15, 15)),
                                    freq='H').tolist()
        current_date += timedelta(days=1)
    if st.sidebar.button('**Start Prediction**'):
        predictions1=model1.forecast(len(indexrange))
        predictions2=model2.forecast(len(indexrange))
        predictions3=model3.forecast(len(indexrange))
        predictions4=model4.forecast(len(indexrange))
        predictions5=model5.forecast(len(indexrange))

        # predictions4=model2.predict(start=len(indexrange), end=len(indexrange), dynamic=False, exog_oos=model2.model.exog)
        # predictions4=model2.forecast(y=model2.endog, steps=len(indexrange),exog_future=model2.exog[:len(indexrange)])
        # columns = ["Open","High","Low","Close","Adj Close"]
        st.subheader('**Predicted Values**',divider=True)
        print(111111111111111111111111111111111111111111111111111111111111111111111111111)
        df = pd.DataFrame(list(predictions1),index=indexrange,columns=['Open'])
        df['High']=list(predictions2)
        df['Low']=list(predictions3)
        df['Close']=list(predictions4)
        df['Adj Close']=list(predictions5)
        df = df.round(0)
        st.dataframe(data=df,width=700)
        st.subheader("Prediction chart",divider=True)
        plt.figure(figsize=(21,11))
        line=px.line(data_frame=df,x=df.index,y=df.columns,title="NIFTY-50 Stock Prices")
        line.show()
        st.plotly_chart(line)
    

    

