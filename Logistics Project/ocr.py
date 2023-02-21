import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image
import os
import matplotlib.pyplot as plt
import easyocr
from PIL import Image
import re
import pymysql
from datetime import datetime
import json
import requests
import sys
 #===========================================================================================
LIMIT_PX = 1024
LIMIT_BYTE = 1024*1024  # 1MB
LIMIT_BOX = 40

rest_api_key = 'cf39a8cb0080c80f06a0092d548e4a07'
#===========================================================================================
def kakao_ocr(image_path: str, appkey: str):
    """
    OCR api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'
 
    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}
 
    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()
 
 
    return requests.post(API_URL, headers=headers, files={"image": data})

def ocr():
#     if len(sys.argv) != 3:
#         print("Please run with args: $ python example.py /path/to/image appkey")
#     image_path, appkey = sys.argv[1], sys.argv[2]
    
    image_path = '/Users/kdb/Desktop/yolov8Serving 2/ocr_result/cropimage.jpg'
    rest_api_key = 'cf39a8cb0080c80f06a0092d548e4a07'
    output = kakao_ocr(image_path, rest_api_key).json()

    print(output)

    try:
        return output['result'][1]['recognition_words'][0]
    except:
        print("length가 잘못 잡혔습니다.")
#===========================================================================================
model = YOLO("result/order_number.pt")

class OCRDetect(object):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
                                        db='log_schema', password='kim3672', charset='utf8')
    flag = False

    def __init__(self):
        self.video = cv2.VideoCapture(2)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, frame = self.video.read()
        
        result = model.predict(source=frame, save=True)

        boxes = result[0].boxes
        
        if len(boxes) > 0 :
            for i in range(len(boxes)):
                print(i+1,"번째 박스")
                box = boxes[i]
                x1 = box.xyxy[0][0]
                y1 = box.xyxy[0][1]
                x2 = box.xyxy[0][2]
                y2 = box.xyxy[0][3]
                x1 = x1.item()
                y1 = y1.item()
                x2 = x2.item()
                y2 = y2.item()
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                print(x1,y1,x2,y2,type(x1))
                
                img = cv2.imread("/Users/kdb/Desktop/yolov8Serving 2/runs/detect/predict/image0.jpg")
                    
                path = "/Users/kdb/Desktop/yolov8Serving 2/ocr_result/cropimage.jpg"
                img = img[y1:y2, x1:x2]

                cv2.imwrite(path,img)
#=====================================================================================================================
                
                post_number= ocr()
                print(post_number)
                
                try:
                    post_number = post_number.replace("-","")

                    if '운송장번호' != post_number and len(post_number) == 12 and int(post_number):
                        try:
                            cursor = OCRDetect.conn.cursor()
                            sql = f"""INSERT INTO ocr (trackingnumber, date) VALUES ('{post_number}', '{datetime.now().strftime("%Y-%m-%d %X")}')"""
                            cursor.execute(sql)
                            OCRDetect.conn.commit()
                        except:
                            print("이미 있는 운송장 번호입니다.")
                except:
                    print("이상한 문자입니다.")

        dst = cv2.imread("/Users/kdb/Desktop/yolov8Serving 2/runs/detect/predict/image0.jpg")
        ret, jpeg = cv2.imencode('.jpg', frame)
        
        return jpeg.tobytes()
#===========================================================================================
