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
import joblib


def run_ml_app() :
    st.subheader('Machine Learning ')

    # 1. 유저한테 입력을 받는다. 

    # 성별
    gender = st.radio('성별을 선택하세요.', ['남자', '여자'])
    if gender == '남자' :
        gender = 1
    
    else:
        gender =  0
    
    age = st.number_input('나이 입력', min_value = 0, max_value=120)
    
    salary = st.number_input('연봉', min_value = 0)

    debt = st.number_input('카드 빚', min_value=0)

    worth = st.number_input('자산 입력', min_value=0)

    # 2. 예측한다.
    # 2-1. 모델 불러오기
    
    model = tensorflow.keras.models.load_model('data/car_ai.h5')

    # 2-2. 넘파이 어레이 만든다.

    new_data  = np.array([gender,  age, salary, debt, worth])
    
    # 2-3. 피처 스케일링 하자.
    # 피쳐 스케일링은 행렬을 넣어야 한다. // 2차원을 넣어야 한다.
    new_data = new_data.reshape(1,-1)

    sc_X = joblib.load('data/sc_X.pkl')
    

    new_data = sc_X.transform(new_data)
    
    # 2-4. 예측한다.
    y_pred = model.predict(new_data)
    
    # 예측 결과는, 스케일링 된 결과이므로, 다시 돌려야 한다.
    # st.write(y_pred[0][0])
    
    sc_y =joblib.load('data/sc_y.pkl')


    

    y_pred_original = sc_y.inverse_transform(y_pred)

    # 3. 결과를 화면에 보여준다.
    btn = st.button('결과 보기')
    if btn :
    
        st.write('예측 결과입니다. {:,.1f}달러의 차를 살 수 있습닌다.'.format(y_pred_original[0,0]))
    
  

