import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from google.colab import drivest
import os
import h5py
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import tensorflow as tf
import tensorflow.keras 
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import CSVLogger
import pickle


def run_eda_app():
    st.subheader('EDA 화면입니다.')

    car_df = pd.read_csv('data/Car_Purchasing_Data.csv')
    
    radio_menu = ['데이터프레임', '통계치']
    selected_radio = st.radio('선택하세요', radio_menu)
    
    if selected_radio == '데이터프레임':
        st.dataframe(car_df)
    
    elif selected_radio == '통계치' :
        st.dataframe( car_df.describe())
    
    columns = car_df.columns
    columns = list(columns)
    selected_columns =  st.multiselect('컬럼을 선택하시오.', columns)
    if selected_columns:
        st.dataframe(car_df[selected_columns])

    # 상관계수를 화면에 보여주도록 만듭니다. 

    corr_columns = car_df.columns[car_df.dtypes != object]
    selected_columns = st.multiselect('상관계수 컬럼 선택', corr_columns)
    if selected_columns:
        if len(selected_columns) != object :
            st.dataframe( car_df[selected_columns])
        else:
            st.write('입력하세요')

    corr_columns = car_df.columns[car_df.dtypes != object]
    selected_corr = st.multiselect('상관계수 확인', corr_columns)

    if len(selected_corr) > 0:
        st.dataframe( car_df[selected_corr].corr())

    else :
        st.write('컬럼을 선택하세요')
    

    if len(selected_corr) > 0:
        fig1 = plt.figure()
        fig = sns.pairplot(data = car_df[selected_corr])
        st.pyplot(fig)



    # 컬럼을 하나만 선택하면, 해당 컬럼의 min과 max에 
    # 해당하는 사람의 데이터를 화면에 보여주는 기능
    number_columns  = car_df.columns[car_df.dtypes != object]
    selected_col = st.selectbox('컬럼 선택', number_columns)

    min_data = car_df[selected_col]  == car_df[selected_col]
    st.write('최소값 데이터')
    st.dataframe(car_df.loc[min_data,])

    max_data = car_df[selected_col]  == car_df[selected_col]
    st.write('최댓값 데이터')
    st.dataframe(car_df.loc[max_data,])
    
    
    # 고객이름을 검색할 수 있는 기능을 개발
    word =  st.text_input('검색어를 입력하세요.')
    word = word.lower()
    if word :
        # 1. 유저한테 검색어 받자
        result = car_df.loc[car_df['Customer Name'].str.lower().str.contains(word),]
        # 2. 검색어를 데이터프레임 커스터머 네임에서 검색하자.
        st.dataframe(result)
        # 3. 화면에 결과를 보여주자.
        result = car_df.loc[car_df['Customer Name'].str.contains(word, case = False),]
        st.dataframe(result)
       

