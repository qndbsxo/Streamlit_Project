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




def run_america() :
    
    
    sel_ame = st.radio('선택하세요.',['DJI', 'NASDAQ'] )
    if sel_ame == 'DJI' :

        df_dji = fdr.DataReader('DJI', '2000')
        df_dji.columns = ['종가', '시가', '고가', '저가', '거래량', '전일비']
        
        
        st.write(df_dji)
        
        btn = st.button('차트 보기')
        

        if btn :
            st.write('종가기준')
            st.line_chart( df_dji['종가'])



    if sel_ame == 'NASDAQ' :
        df_ixic = fdr.DataReader('IXIC', '2000')
        df_ixic.columns = ['종가', '시가', '고가', '저가', '거래량', '전일비']
        st. write(df_ixic)

        btn1 = st.button('차트 보기')
        

        if btn1 :
            st.write('종가기준')
            st.line_chart( df_ixic['종가'])

        
