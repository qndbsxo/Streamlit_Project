import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import requests
from fbprophet import Prophet
import string
import FinanceDataReader as fdr
import bs4
from PIL import Image
from kospi import run_kospi
from america import run_america



def run_search():
    df_krx = fdr.StockListing('KRX')
    df_krx_drop = df_krx.dropna()
    st.header('KOSPI , KOSDAQ 종목검색')
    st.write('종목코드를 확인하세요.(Symbol)')
    st.dataframe(df_krx_drop)

    code_input = st.text_input('종목코드')
    
    if len(code_input) != 0 :
        st.write( df_krx_drop.loc[ df_krx_drop['Symbol'] == code_input, ] )

        sel_df = fdr.DataReader(code_input, '2000')
        sel_df.columns = ['종가', '시가', '고가', '저가', '거래량', '전일비']
        st.write(' 주가현황 ')
        st.write(sel_df)
        
        
        if st.button('차트 보기') :
            st.line_chart( sel_df['종가'])


        sel_df_re = sel_df.reset_index()
        sel_df_re.rename(columns={'Date':'ds', '종가':'y'},inplace=True)
        # st.write(sel_df_re)

        if st.button('주가예측') :
            m = Prophet()
            m.fit(sel_df_re)

            future = m.make_future_dataframe(periods= 180)
            forecast = m.predict(future)

            st.dataframe(forecast)

            fig1 = m.plot(forecast)
            st.pyplot(fig1)

            fig2 = m.plot_components(forecast)
            st.pyplot(fig2)


    

        