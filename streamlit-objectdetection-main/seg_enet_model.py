import numpy as np
import argparse
import imutils
import time
import cv2
import os
import matplotlib.pyplot as plt
import streamlit as st



def seg_img(image_path):

    SET_WIDTH = int(600)
    
    
    normalize_image = 1/ 255.0
    resize_image_shape = (1024, 512)

    sample_img = cv2.imread(str(image_path))

    sample_img = imutils.resize(sample_img , width=SET_WIDTH)

    # opencv의 pre trained model 을 통해서, 예측하기 위해서는
    # 입력이미지를 blob으로 바꿔줘야한다.
    # 블랍 만들기
    # cv2.dnn 을 활용하기때문에 블랍을 만드는거임 . 그렇지 않으면 필요없음

    blob_img = cv2.dnn.blobFromImage(sample_img, normalize_image, resize_image_shape, 0, swapRB=False, crop=False)

    # Enet 모델 가져오기
    cv_enet_model = cv2.dnn.readNet('enet-cityscapes/enet-model.net')

    cv_enet_model.setInput(blob_img) # 모델에 블랍을 넣음
    cv_enet_model_output = cv_enet_model.forward() # 블랍 결과를 받음

    # 레이블 정보 가져오기 ( 레이블 이름 로딩 )
    label_values = open('enet-cityscapes/enet-classes.txt').read().split('\n')
    label_values = label_values[ : -2+1]

    IMG_OUTPUT_SHAPE_START = 1
    IMG_OUTPUT_SHAPE_END = 4
    classes_num, h, w = cv_enet_model_output.shape[IMG_OUTPUT_SHAPE_START : IMG_OUTPUT_SHAPE_END]

    # 모델의 아웃풋 20개 행렬을 , 하나의 행렬로 만든다.
    class_map = np.argmax(cv_enet_model_output[0], axis=0)
    # 소프트맥스로 나온값의 인덱스 값을 가져온다.( 제일 큰 숫자의 행렬 번호), 쉐입을 보고 엑시스 설정


    # 클래스별로 색정보가 들어있는데, 문자열로 들어있다.
    CV_ENET_SHAPE_IMG_COLORS = open('enet-cityscapes/enet-colors.txt').read().split('\n')
    CV_ENET_SHAPE_IMG_COLORS = CV_ENET_SHAPE_IMG_COLORS[  :  -2+1]

    CV_ENET_SHAPE_IMG_COLORS = np.array([np.array(color.split(',')).astype('int')  for color in CV_ENET_SHAPE_IMG_COLORS  ])


    ## 하나의 행렬을 이미지로 만든다.
    ## 인덱스로 외어 있는 클래스를 색으로 바꾼다.
    # 각 픽셀별로, 클래스에 해당하는 숫자가 적힌 class_map을
    # 각 숫자에 매핑되는 색깔로 셋팅해 준것이다.
    # 따라서 각 픽셀별 색깔 정보가 들어가게 되었다.
    mask_class_map = CV_ENET_SHAPE_IMG_COLORS[class_map] # 3차원

    #원래 크기로 리사이즈 한다. 원본이미지에 합쳐야하기 때문에.
    # 인터폴레이션을 INTER_NEAREST 로 한 이유는?? 
    # 레이블 정보(0~19) 와 컬러정보 (23,100,243) 는 둘다 int 이므로, 
    # 가장 가까운 픽셀 정보와 동일하게 셋팅해주기 위해서.
    mask_class_map = cv2.resize(mask_class_map, (sample_img.shape[1], sample_img.shape[0]) , interpolation = cv2.INTER_NEAREST )

    class_map = cv2.resize(class_map, (sample_img.shape[1], sample_img.shape[0]) , 
                        interpolation=cv2.INTER_NEAREST)



    # 원본이미지와 색마스크 이미지를 합쳐서 보여준다.
    # 가중치 비율을 줘서 보여준다.    
    # 총합이 이미지 기준인 255를 넘어서는 안된다.
    cv_enet_model_output = (( 0.4 * sample_img)  + (0.6 * mask_class_map)).astype('uint8')


    # 레이블 보기
    my_legend = np.zeros( ( len(label_values) * 25 ,  300 , 3  )   , dtype='uint8' )
    #  i: 인덱스, class : label_values,   img_col : CV_ENT 이 들어감.   enumerate 문법
    for ( i, (class_name, img_color)) in enumerate( zip(label_values , CV_ENET_SHAPE_IMG_COLORS)) :
        color_info = [  int(color) for color in img_color  ] # 인트로 만들기
        cv2.putText(my_legend, class_name, (5, (i*25) + 17) , 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0) , 2 )
        cv2.rectangle(my_legend, (100, (i*25)), (300, (i*25) + 25) , tuple(color_info), -1)

    st.image(cv_enet_model_output, width=800) 
    # cv2.imshow('ori', sample_img)
    # st.image(mask_class_map)
    st.image(my_legend)
