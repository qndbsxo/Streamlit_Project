import streamlit as st
import cv2
from PIL import Image 
import imutils





def run_home() :
    st.subheader('SSD 와 YOLO를 이용한 Object Detection 과 E-NET 을 이용한 Semantic Segmentation')
    st.write('컴퓨터비전(Computer Vision)의 활용은 점점 진화하고 있으며, 현재 관심분야인 자율주행시스템과 관련이 있고 ,') 
    st.write('그것이 아니더라도 모든 분야에서 컴퓨터비전 기술이 접목되고 있어 중요한 기술로 자리 잡고 있다.')
    st.write('그 중 Semantic Segmentation과 Object Detection은 자율주행 관련하여서는 없어서는 안될 기술로 자리매김한다.')
    st.write('자율주행을 위한 그 주변지역의 사물(객체)를 구분함으로써 안전하게 운행을 가능하게 한다.')


    home_od_img = Image.open('data/images/object_detection2.PNG')
    home_od_img = home_od_img.resize((600,400))
    st.image(home_od_img)

    st.write('위는 Object Detection 모델의 발전과정을 나타내고 있고, 초기모델부터 현재까지 처리 속도 및 정확도를 향상하며')
    st.write('계속 발전되어 왔고, 앞으로도 계속 발전될 전망이다.')
    st.write('이러한 기술은 자율주행시스템 뿐만 아니라, 의료 등 많은 분야에 접속되어 사용되고 있고, 더 많은 분야에 접목될 것으로 보인다.')

    st.write('이번 프로젝트는 대표적인 Object Detection모델의 소개와 이미지 및 영상 Detection , Segmentation을 직접 처리한다.')
    
    img = Image.open('data/images/home_image.png')
    img = img.resize((600,400))
    st.image(img)

    st.write('참고 : 언젠가 정리 https://kyeonghyeon86.tistory.com/')
    

    