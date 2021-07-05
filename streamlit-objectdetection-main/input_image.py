import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img
import pathlib
import os
from yolo_model import yolo_img
from seg_enet_model import seg_img

def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2.이제는 디렉토리가 있으니, 파일을 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('Saved file : {} in {}'.format(file.name, directory))


def input_image() :
    
    image_file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'],accept_multiple_files=True)

    if image_file is not None :
        
        # st.write( image_file.name )
                
        # st.subheader('Image resized 800 X 600 (Original) ')
        file_path= []
        for img_file in image_file :
            
            save_uploaded_file('temp_files', img_file)
            file_path.append(img_file)
            img = Image.open(img_file)
            img = img.resize((800,600))
            st.image(img)
        # print(file_path)
        btn = st.button('Object Detection')
        

        if btn :
            st.subheader('Objecct Detection Image result')
            for file in file_path :    
                image_path = pathlib.Path('temp_files\\' + str(file.name))
                print(image_path)
                ssd_img(image_path)         



def input_image_yolo():
    image_file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'],accept_multiple_files=True)

    if image_file is not None :
        
        # st.write( image_file.name )
                
        # st.subheader('Image resized 800 X 600 (Original) ')
        file_path= []
        for img_file in image_file :
            
            save_uploaded_file('temp_files', img_file)
            file_path.append(img_file)
            img = Image.open(img_file)
            img = img.resize((800,600))
            st.image(img)
        # print(file_path)
        btn = st.button('Object Detection')
        

        if btn :
            st.subheader('Objecct Detection Image result')
            for file in file_path :    
                image_path = pathlib.Path('temp_files\\' + str(file.name))
                print(image_path)
                yolo_img(image_path)             



def input_image_seg() :
    image_file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'],accept_multiple_files=True)

    if image_file is not None :
        
        # st.write( image_file.name )
                
        # st.subheader('Image resized 800 X 600 (Original) ')
        file_path= []
        for img_file in image_file :
            
            save_uploaded_file('temp_files', img_file)
            file_path.append(img_file)
            img = Image.open(img_file)
            
            st.image(img,width=800)
        # print(file_path)
        btn = st.button('Object Detection')
        

        if btn :
           
            for file in file_path :    
                image_path = pathlib.Path('temp_files\\' + str(file.name))
                # print(image_path)
                seg_img(image_path)        

        

