import streamlit as st
import cv2
from ssd import run_ssd
from yolop import run_yolo
from semantic_segmentation import run_seg
from home import run_home



def main():
    
    st.set_page_config(layout='wide')

    st.title('Streamlit Object Detection & Semantic Segmentation')

    # st.subheader('SSD , YOLO 를 활용한 Object Detection')

    menu = ['Home', 'SSD', 'YOLO','Semantic_Segmentation']

    choice = st.sidebar.selectbox('MENU', menu)

    if choice == 'Home' :
        run_home()
    
    if choice == 'SSD' :
        
        run_ssd()

    if choice == 'YOLO' :
        
        run_yolo()

    if choice == 'Semantic_Segmentation' :
        run_seg()

            















if __name__ == '__main__' :
    main()
