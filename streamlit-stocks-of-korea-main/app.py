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
from search import run_search



def main() :
    
    menu = ['HOME', 'KOSPI & KOSDAQ', 'DJI & NASDAQ','종목검색' ]

    choice = st.sidebar.selectbox('메뉴', menu)

    
    if choice == 'HOME' :
        st.header('주가 예측 앱')
        st.write('한국 , 미국 증시 시세')
        st.write('KOSPI, KOSDAQ 종목 시세 및 예측')
        st.header('''
    
                ''')
    
        img = Image.open('data/pic.jpg')
        st.image(img)
    

    
    if choice == 'KOSPI & KOSDAQ' :
        run_kospi()

    if choice == 'DJI & NASDAQ' :
        run_america()

    if choice == '종목검색':
        run_search()
    





if __name__ == '__main__' :
    main()