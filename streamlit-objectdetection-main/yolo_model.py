import os
import time
import cv2
import numpy as np
from yolo.model.yolo_model import YOLO
import streamlit as st




def process_image( img ) :
    """ 이미지 리사이즈하고, 차원 확장 
    img : 원본이미지
    결과는 ( 64, 64, 3 ) 으로 프로세싱된 이미지 반환 """

    image_org = cv2.resize( img, ( 416, 416 ), interpolation = cv2.INTER_CUBIC) 
    image_org = np.array( image_org, dtype='float32' )
    image_org = image_org / 255.0
    image_org = np.expand_dims( image_org, axis = 0 )

    return image_org


def get_classes( file ) :
    """ 클래스의 이름을 가져온다.
    리스트로 클래스 이름을 반환한다. """
    with open(file) as f :
        name_of_class = f.readlines()

    name_of_class = [ class_name.strip() for class_name in name_of_class  ]

    return name_of_class


def box_draw( image, boxes, scores, classes, all_classes):
   
    """ image : 원본이미지
    boxes : 오브젝트의 박스데이터, ndarry
    classes : 오브젝트의 클래스
    scores : 오브젝트의 확률
    all_classes : 모든 클래스 이름 """

    for box, score, cl in zip(boxes, scores, classes):
        x, y, w, h = box

        top = max(0, np.floor(x + 0.5).astype(int))
        left = max(0, np.floor(y + 0.5).astype(int))
        right = min(image.shape[1], np.floor(x + w + 0.5).astype(int))
        bottom = min(image.shape[0], np.floor(y + h + 0.5).astype(int))

        cv2.rectangle(image, (top, left), (right, bottom), (255, 0, 0), 3)
        cv2.putText(image, '{0} {1:.2f}'.format(all_classes[cl], score),
                    (top, left - 6),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 3,
                    cv2.LINE_AA)

        print('class: {0}, score: {1:.2f}'.format(all_classes[cl], score))
        print('box coordinate x,y,w,h: {0}'.format(box))

    print()    




def detect_image( image, yolo, all_classes ) :
    """ image : 원본 이미지
    yolo : YOLO 모델
    all_classes : 전체 클래스 이름 
    변환된 이미지 리턴 """

    pimage = process_image(image)

    image_boxes, image_classes, image_scores = yolo.predict(pimage, image.shape)

    if image_boxes is not None : 
        box_draw(image, image_boxes, image_scores, image_classes, all_classes)

    return image





def yolo_img(image_path) :
    
    yolo = YOLO(0.6, 0.5)

    all_classes = get_classes('yolo/data/coco_classes.txt')

    image = cv2.imread(str(image_path))

    result_image = detect_image( image, yolo, all_classes)
    
    result_image = cv2.resize(result_image, (800,600))

    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)


    st.image(result_image)



