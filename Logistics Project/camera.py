import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image
import pymysql
from datetime import datetime

model = YOLO("result/yolov8n.pt")

'''
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', db='logistics', password='1234', charset='utf8')
cursor = conn.cursor()
# 데이터베이스 만들기
#sql = """ CREATE DATABASE logistics"""
# 표 만들기
#sql = """ CREATE TABLE detect (count int(11), class varchar(20), datetime varchar(100))"""

#sql = "INSERT INTO detect (count, class, datetime) VALUES (%d, '%s', '%s')"
cursor.execute(sql)
cursor = conn.commit()
conn.close()'''




class VideoCamera(object):
    nowtime = datetime.now().strftime('%Y%m%d %H:%M:%S')
    dbtime = str(nowtime)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
                                        db='log_schema', password='kim3672', charset='utf8')
    most_x_max = 0 
    flag = 0

    def __init__(self):
        self.video = cv2.VideoCapture(2)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        print("image:", len(image),len(image[0]))
        
        result = model.predict(source=image, save=True)
        
        boxes = result[0].boxes
        
        # hole = 0, wet = 1

        if len(boxes) > 0 :
            
            

            for i in range(len(boxes)):
                print(i+1,"번째 박스")
                box = boxes[i]  
                xmin = int(box.xyxy[0][0]) # xmin값
                xmax = int(box.xyxy[0][2]) # xmax값
                xbox = (xmin+xmax)/2   # x 중심좌표
                box_class = int(boxes.cls.tolist()[i])
                print(f"flag : {VideoCamera.flag}")
                # 넓이 1920 , 높이 1080 960
                class_data = []
                class_data.append(str(box_class))
                if len(class_data)>0:
                    hole_cnt= class_data.count('0')
                    wet_cnt = class_data.count('1')

                if VideoCamera.most_x_max < xbox: # 박스들을 순회하면서 가장 큰 x 센터 좌표를 뽑아내기 위함
                    VideoCamera.most_x_max = xbox
            print("가장큰 x좌표", VideoCamera.most_x_max)

            #======================================================================
            if VideoCamera.most_x_max <=340 and len(boxes) is not None:  # 0 ~ 240, len(boxse)가 값이 비어있지 않다면,  플래그가
                VideoCamera.flag = 0
            
                    
            #elif VideoCamera.most_x_max>= 340 and VideoCamera.most_x_max < 1580: #660 ~ 1260 flag
            #    VideoCamera.flag = 1
            #    VideoCamera.most_x_max = 0 
            
            elif VideoCamera.most_x_max>= 1580 and VideoCamera.most_x_max <1920 and VideoCamera.flag != 1: # 1680 ~ 1920        
                cv2.imwrite(f"./detect_result/{VideoCamera.nowtime}.jpg", image) # 뒤에 image 넣을 것.
                    
                cursor = VideoCamera.conn.cursor()
                print("",VideoCamera.most_x_max)
                sql = f"""INSERT INTO detect (hole, wet, class, datetime) VALUES ('{hole_cnt}','{wet_cnt}', {box_class}, '{VideoCamera.dbtime}')"""
                cursor.execute(sql)
                VideoCamera.conn.commit()
                VideoCamera.flag = 1
                VideoCamera.most_x_max = 0 
            
            #pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'hole갯수:0,wet갯수:1, 1, 20230216)' at line 1"
        ret, jpeg = cv2.imencode('.jpg', image)
        
        return jpeg.tobytes()