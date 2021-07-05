import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img

import pathlib
from input_image import input_image
from home import run_home


def run_ssd() : 

    menu = ['About SSD', 'Play SSD']

    select = st.sidebar.selectbox('SELECT', menu)
    
    # st.info('SSD Image Object Detection 활용')

    if select == 'About SSD' :
        st.subheader('Object Detection이란')
        st.write('Object Detection은 Classification의 확장된 개념으로 볼 수 있다.')
        st.write('Classifictation는 사전에 학습된 데이터를 기반으로 어떤 이미지가 데이터로 들어오면 그 이미지가 무엇을 나타내는지 확률적 분석을 통해서 이미지 분류를 해준다.')
        img = Image.open('data/images/cat1.PNG')
        st.image(img)

        st.write('위와 같이 Classification은 하나의 이미지를 하나의 객체로 분류해주는 반면, Object Detection은 Localization이라는 개념을 포함하여')
        st.write('다중 객체 분류를 가능하게 해준다. 이러한 기능을 하게 하는 모델 중 하나가 SSD이다.')

        od_img = Image.open('data/images/object_detection1.PNG')
        st.image(od_img)

        st.write('기존에는 물체를 감지하는 커널을 가지고 , Sliding window방식으로 Convolution하며 , 나온 결과를 히스토그램으로 그려가며 물체를 인식한다.')
        st.write('이때 원본스케일과 다른 여러개의 다른 스케일을 가진 이미지로 반복하며, 크고 작은 물체들을 인식하게 되는것이다.')
        st.write('처리속도가 느리고, 복잡하여 개발된것이 SSD이다.')

        st.subheader('SSD란 Single Shot Detector 의 약자로 , ')
        st.write('말 그대로 사진의 변형 없이 그 한 장으로 훈련, 검출을 하는 Detector를 의미한다. ')
        st.write('SSD는 기존 YOLO의 그리드셀 방식을 적용시키고, 처리속도 및 정확도를 개선하기 위해 개발되었다.')
                
        ssd_cap_img1 = Image.open('data/images/ssd_capture1.PNG')
        ssd_cap_img1 = ssd_cap_img1.resize((600,400))
        st.image(ssd_cap_img1)
        st.write('(SSD의 정확도 및 처리속도)')

        st.write('SSD는 VGG Net을 이용하였지만, 그대로 이용하지 않고, SSD모델에 맞게 수정하여 이용하였다. ')
        ssd_cap_img2 = Image.open('data/images/ssd_capture2.PNG')
        ssd_cap_img2 = ssd_cap_img2.resize((600,400))
        st.image(ssd_cap_img2)
        
        st.write('SSD는 YOLO V1과는 다르게, FC layer를 제거시켜 Object Detection 모델에서 입력이미지를 고정시키지 않아도 가능하다.')
        ssd_cap_img3 = Image.open('data/images/ssd_capture3.PNG')
        ssd_cap_img3 = ssd_cap_img3.resize((600,400))
        st.image(ssd_cap_img3)

        st.write('SSD 역시 그리드셀을 사용하게 되는데, 다양한 크기의 객체 검출을 위해서 다양한 크기의 feature map을 사용하게 된다.')
        st.write('feature map크기에 따라 사이즈가 큰 객체, 사이즈가 작은 객체를 검출할 확률이 다르기 때문에 높은 정확성을 위하여 이런 방식을 사용한다.')
        ssd_cap_img4 = Image.open('data/images/ssd_capture4.PNG')
        ssd_cap_img4 = ssd_cap_img4.resize((600,400))
        st.image(ssd_cap_img4)

        st.write('이러한 일련의 과정을 통하여 나온 결과는 같은 객체임에도 많은 Bounding box를 가지게 된다.')
        st.write('이를 해결하기 위해, NMS를 적용하여 정답과 가장 유사하다고 하는 값을 가지는 Bounding box를 선택하여 객체로 검출한다.')
        ssd_cap_img5 = Image.open('data/images/ssd_capture5.PNG')
        ssd_cap_img5 = ssd_cap_img5.resize((600,400))
        st.image(ssd_cap_img5)

        



    elif select == 'Play SSD' :
    
        sel_ssd = st.radio('Select', ['Image', 'Video'] )  #Input_Image 뺌

        if sel_ssd == 'Image' :
            
            image_btn = st.selectbox('select image', ['image_1', 'image_2'] )
            
            if image_btn == 'image_1' : 
                
                img = Image.open('data/images/image1.jpg')
                img = img.resize( ( 800,600 ) )
                st.image(img)

                btn = st.button('Object Detection')

                if btn :
                    # EC2 문제로 결과 이미지만 가져오기로 함
                    # image_path = pathlib.Path('data\\images\\image1.jpg')
                    # st.subheader('Objecct Detection Image result')
                    # ssd_img(image_path)

                    img = Image.open('data/images/ch_image1.jpg')
                    img = img.resize( (800,600))
                    st.image(img)

            elif image_btn == 'image_2' :
                img = Image.open('data/images/image2.jpg')
                img = img.resize( ( 800,600 ) )
                st.image(img)

                btn = st.button('Object Detection')

                if btn :
                    # EC2 문제로 결과 이미지만 가져오기로 함
                    # image_path = pathlib.Path('data\\images\\image2.jpg')
                    # st.subheader('Objecct Detection Image result')
                    # ssd_img(image_path)

                    img = Image.open('data/images/ch_image2.jpg')
                    img = img.resize( (800,600))
                    st.image(img)

        # EC2 문제로 없애기    
        # if sel_ssd == 'Input Image' : 
        #     input_image()
            
        
        
        
        
        if sel_ssd == 'Video' :

            st.subheader('Object Detection 처리 영상')
            st.info('AWS EC2의 프리티어 사용으로 실시간 처리가 힘들어 Local에서의 작업 후 결과 영상')
     
            video_file = open('data/videos/output_ssd.mp4', 'rb').read()
            # video_file = cv2.cvtColor(video_file, cv2.COLOR_BGR2RGB)
            st.video(video_file)
            st.write('(Local에서의 Object Detection 처리 영상)')
            
            re_video_file = open('data/videos/record_ssd.mp4','rb').read()
            st.video(re_video_file)
    


