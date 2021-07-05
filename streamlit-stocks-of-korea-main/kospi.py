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




def run_kospi() :
    
    
    sel_kor = st.radio('선택하세요.',['KOSPI', 'KOSDAQ'] )
    if sel_kor == 'KOSPI' :

        df_kospi = fdr.DataReader('KS11', '2000')
        df_kospi.columns = ['종가', '시가', '고가', '저가', '거래량', '전일비']
        
        
        st.write(df_kospi)
        
        btn = st.button('차트 보기')
        

        if btn :
            st.write('종가기준')
            st.line_chart( df_kospi['종가'])



    if sel_kor == 'KOSDAQ' :
        df_kosdaq = fdr.DataReader('kq11', '2000')
        df_kosdaq.columns = ['종가', '시가', '고가', '저가', '거래량', '전일비']
        st. write(df_kosdaq)

        btn1 = st.button('차트 보기')
        

        if btn1 :
            st.write('종가기준')
            st.line_chart( df_kosdaq['종가'])

        
