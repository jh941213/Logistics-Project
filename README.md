# 📦 Logistics Packge Realtime Detection 📦
<img src="https://www.dailylog.co.kr/news/photo/201204/3888_1733_4612.jpg" width="700" height="370" div align="center">

---

# 🔥 Team 
[김재현](http://https://github.com/jh941213) | [이성연](https://github.com/deepshadow25)
------|------|
Team Leader|Team Member|
<img src="https://user-images.githubusercontent.com/112835087/214769736-c6880568-a4f9-42f7-b5d9-3ef466b6a997.jpeg" width="100" height="100">|<img src="https://user-images.githubusercontent.com/112835087/214769769-f12d45ae-6b09-4567-b142-591c73ccffdb.png" width="100" height="100">

# 🖥️ Team Preferences  
비고|local(김재현)|(local(이성연) | AWS Server | Google Colab
-----|-------|-------|-------|-------|
CPU | Apple M1(10core)|i7-8565U| i7 4core|Xeon(R)cpu 2.3GHz|
-----|-------|-------|-------|-------|
RAM |32GB|16GB|16GB|13~52GB|  
-----|-------|-------|-------|-------|
Storage |512GB|512GB|250GB|166GB|
-----|-------|-------|-------|-------|
OS |macOS ventura|Window 10| linux |linux|
-----|-------|-------|-------|-------|
MOBILE |iphone 13 mini|Galaxy S10|------|------|  

# Index
- [🔑 Project Summary](#project-summary)
- [📆Procedures(Time Stamp)](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)
- [👥 Roles](#-roles)
- [🧘 Feature](#-feature)
- [📦 Data Set](#Data-set)
- [🏞️ Image Processing](#Image-Processing)
- [🚀 Model Serving](#Model-Serving)
- [📊 Result](#-result)
- [📷 Show Result](-Show-Result)
- [💻 Requirements](#-requirements)
- [🔧 Folder Structure](#-folder-structure)
- [📜 Reference](#-Reference)

---

# 🔑Project Summary
> - 주제  
> 물류센터(HUB, CAMP) 등 컨테이너 벨트 과정에서 박스 패키징의 찢어지거나 젖음과 같은 결함을 RealTime Detection 하여 각 레일에 위치에 있는 인적자원을 AI 로 대체해 자동화시스템을 구축  

> - 인사이트  
> 쿠팡과 같은 대형물류 센터에서는 오토소터와 같은 송장정보를 인식하는 바코드기반의 대형센서 장비가 구비되어 현재 자동화 시스템을 구축하고 있다고 한다. 근데 그 과정에서 기존 레일의 철수 및 재 정비 설치 과정에서 막대한 비용과 오토소터 자체의 큰 비용으로 인해 우리의 AI 모델을 사용한다면 저비용 고효율이란 효과를 낼 수 있지 않을까란 생각. 고객경험이 좋아지고, 오상차 오배송에 대한 데이터 축적으로 내부 프로세스 평가 반영 가능 등 B2B, B2C 관점에서 다양한 부분으로 인적, 경제적인 이득이 가능하다.  


---

# [📆Procedures(Time Stamp)](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)

>**[2023.01.02 ~ 2023.01.06]**
>- 프로젝트 주제 탐색 및 선정
>- 프로젝트 계획 구상
><br>
>
>**[2023.01.06 ~ 2023.01.18]**
>- 데이터 수집 및 전처리
>   - Anomaly Detection 특성상 불량데이터를 구하기 어려웠으므로 이를 직접 만들어냄.
>   - 가장 보편적인 택배 상자(갈색 판지 상자)의 데이터만을 고려
><br>
>
>**[2023.01.14 ~ 2023.01.16]**
>- 1차 Model training and testing
>   - Real Time & Anomaly Detection
>   - Train, valid dataset split
>   - Data Augmentation
><br>
>
>**[2023.01.17 ~ 2023.01.24]**
>- 1차 Anomaly Detection model result 분석, 평가
>   - Annotating 대폭 수정 
>- OCR / Model serving Reference Searching 시작
>   - App service 계획이 있었으나 차후로 미룸.
><br>
>
>**[2023.01.25 ~ 2023.01.27]**  
>- 2차 Detection Model training and testing
>   - 수정된 Annotating 적용
>   - Resolution 조정 (640*640 -> 1280*1280)
>   - 결과 분석, 평가 후 3차로 넘어감
>- Github repository 결과물 정리
>   - Readme 작성 시작
><br>
>
>**[2023.01.28 ~ 2023.02.06]**  
>- OCR model 준비
>   - 택배 운송장 데이터 준비 (임의의 주소데이터 생성, 송장 인쇄)
>   - OCR API test (Google Cloud Vision, Naver Clova)
>   - OCR model searching (EazyOCR, Tesseract 등)
>- 3차 Detection model training and testing
>   - use EfficientDet models. (D0, D1)
>   - also used Yolo models : Yolo가 Eff.Det보다 나음 확인
>- App 구현 계획을 Web Serving으로 수정. (Insight 다시보기)
>   - 고객에게 알림을 발송하는 기능이 필요없음.
>   - 물류회사(공장) 내부에서만 사용하는 프로그램으로 사용 : 웹으로만 구현해도 됨.
><br>
>
>**[2023.02.07 ~ 2023.02.13]**
>- Web Serving 구축 (Flask)
>  - 실시간 구축 웹 사이트 구현
>  - 웹 UI 제작 (불량검출 : 검출하는 것 보여주기 / 송장인식 : OCR bbox 저장+crop)
>- OCR Data train + inference 시작
>  - Tesseract, Naver Clova API, EazyOCR 등 사용
>  - 송장 사진 100여 장에서 각 숫자 + "운송장번호" 글자에 bounding box 지정, inference
>    - Yolo v8 기반으로 모델 만들기 도전. 20,000 Epoch 시도.
><br>
>
>**[2023.02.13 ~ 2023.02.16]**
>- Presentation 준비
>   - Data, Model, OCR, Git, any other process 정리
>   - 발표 대본 제작, 디자인 구상
>- DB 구축
>
>- OCR 수정
>
><br>
>
>**[2023.02.17]**
>- 중간발표 및 점검.
---

# 👥 Roles
> - 김재현 : modeling by yolov7, yolov8(Train, Valid, Test), OCR Modeling, Flask Serving Coding, mySQL build
> - 이성연 : Data Process, YOLO model thesis reference serch, YOLOV4 Modeling

---

# 🧘 Feature
> - Detection 최적의 모델을 찾기 위한 YOLO, efficientDet, CoreML등 객체모델 학습 및 테스트  
> - Make Data Set 구축을 위한 현실에서의 데이터 셋 Searh & Make  
> - EasyOCR, Tesseract, MMOCR 등 오픈소스기반의 OCR 모델 사전 테스트 및 fine tune  
> - NAVER Clova AI, KAKAO 등 국내 기업의 OCR API 사용 

---

# 📦 Data Set  

## Box Data Set Annotation  
 라벨 : Hole(구멍, 찢어짐), Wet(젖음)  
 Annotation 을 위하여 Hole, Wet의 일정 패턴을 파악하여 반복 학습 할 수 있도록 Annotation 작업 진행 (Key Point)🔑   
 Hole 같은 경우 픽셀자체가 검정색 부분이 많이 나오기 때문에 검정색이라던지 , 구멍이 뚫려있을 때의 특징을 생각 하여 Annotation을 하였다.  
 Wet 같은 경우 너무 경우의 변수가 많아서 기준을 잡고 전체적으로 젖은박스 와 살짝 젖더라도 이건 불량이다 싶은 박스만 학습하였다. 이유는 살짝묻은 물에도 디텍션을 해버리면 모델자체가 의미가 없기 때문에 잘 생각하고 판단하여 annotation작업을 하였다.  
 
## Tracking Number Data Set Annotation  
 라벨 : trackingnumber  
1단계 : 송장전체를 학습  -> mAP 0.995 
2단계 : 운송장번호가 있는 위치값을 학습 -> mAP 0.995  
polygon 을 이용하여, 다양한 각도에서도 잘 디텍션 할수 있도록 annotation 작업을 해주었다.  

## 🌊Box data set flow

### 1단계 : 웹 크롤링 을 통하여 데이터 수집 (987장)  
<img width="600" alt="스크린샷 2023-02-20 오후 4 39 12" src="https://user-images.githubusercontent.com/112835087/220042612-52484d5e-66b8-4cf8-8e41-ec2dcde76775.png">  

### 2단계 : 웹 크롤링 자체적인 길거리 탐색 데이터 수집 (1684장)  
<img width="600" alt="스크린샷 2023-02-20 오후 4 39 12" src="https://user-images.githubusercontent.com/112835087/220042773-d6daa80c-1758-40d5-8247-dbfa3cf6bb05.png">  

### 3단계 : 갈색박스 상자 구매후 자체적인 데이터셋 제작 (3287장)   
<img width="600" alt="스크린샷 2023-02-20 오후 4 40 45" src="https://user-images.githubusercontent.com/112835087/220042859-f769a323-bf14-4b64-b198-412931588292.png">  

## 🌊tracking number data set flow

### 1단계 : 송장 전체를 Annotation  
<img width="600" height="300" alt="스크린샷 2023-02-21 오후 3 35 41" src="https://user-images.githubusercontent.com/112835087/220266165-738a6e19-0852-447d-8801-dbe6b48c1c72.png">  

### 2단계 : 운송장번호 위치 값 Annotation  
<img width="275" alt="스크린샷 2023-02-21 오후 3 21 49" src="https://user-images.githubusercontent.com/112835087/220266264-51fb689e-0618-4570-a824-7416f64dad24.png">

## Total Data Set 구성  
Box DataSet  
image : 3287장, 객체 수 : 4,837개, Hole(구멍,찢어짐) : 2,226개 , Wet(젖음) : 2,611개  
Tracking DataSet  
image : 250장 , 객체 수 : 250개, trackingnumber : 250개


데이터 종류| 일자 | 사용기술 | 링크
 ------------|------|-------|-----|
Box data | 2023 | YOLOv8 | [Box data](https://universe.roboflow.com/jaehyun-kim/finalbox)
Tracking data | 2023 | YOLOv8 | [Tracking data](https://universe.roboflow.com/deeple/trackingnumberod)

<img width="600" alt="스크린샷 2023-02-20 오후 4 46 36" src="https://user-images.githubusercontent.com/112835087/220043929-748afad6-e9f6-4e15-8fa9-b606af1c46f8.png">
<img width="600" alt="스크린샷 2023-02-21 오후 3 21 44" src="https://user-images.githubusercontent.com/112835087/220263968-ccf9e9b3-34bb-4d11-8971-d06969568954.png">

 ## image size & resize  
 640 x 640 -> 1280 x 1280 -> 2048 x 2048  
 --> yolov7 논문 참조시 데이터셋 640 x 640 학습 추후 데이터 핸들링을 통하여 resize 작업 진행

 ## Augmentation  
 crop 10° -> 데이터 증강을 위한 Agumentation  
 yolov7, yolov8 hyper param 기능 agumentation: True  
 (Mosaic : 1.0, fliplr : 0.5, scale : 0.5, translate : 0.1, hsv_h : 0.015, hsv_s = 0.7, hsv_v = 0.4)

---

# 🏞️ Image Processing
## open-CV 를 활용한 이미지 전처리  

- 적용 데이터 : 📁 Tracking number Detection Data!  

1️⃣ Zero-Padding  
직접 짠 zero-padding 코드를 이용하여, 이미지를 모델 input size 를 맞추기위해 전처리를 해준다.  
<img width="900" src="https://user-images.githubusercontent.com/112835087/220052065-ad5ed28f-9487-434b-8f0d-5be4db838b26.jpg">

2️⃣ GrayScale  
원할한 Text Recognize 를 위한 GrayScale 를 진행해준다.  
<img width="900" alt="스크린샷 2023-02-20 오후 5 21 25" src="https://user-images.githubusercontent.com/112835087/220053078-c2ea2385-3a2b-4929-8a86-bb5cf09785a0.png">  

3️⃣ Binary   
GrayScale이 된 Data를 Binary 화를 진행해준다.  
<img width="900" alt="스크린샷 2023-02-20 오후 5 21 31" src="https://user-images.githubusercontent.com/112835087/220053336-7742bc3a-c5f4-4356-85c3-c349285bca91.png">  

4️⃣ Remove Noise   
noise 제거를 통한 recognize 준비  
<img width="900" alt="스크린샷 2023-02-20 오후 5 21 37" src="https://user-images.githubusercontent.com/112835087/220053671-d4821360-fc71-485a-be47-38cffbf6af7d.png">  

---
# 🚀 Model Serving

> - Model serving  
> Flask 를 활용하여 local host 웹 서버 구축 (사용자 local에 영역을 받는다.  
> Box Detect page, Tracking number page(OCR) 을 구분하여 두 페이지 영역 구성  
> mySQL 을 이용하여 detection 검출된 내용 DB 저장, 
>
### Main Page  
<img width="2045" alt="스크린샷 2023-02-20 오후 3 49 26" src="https://user-images.githubusercontent.com/112835087/220034085-9130524a-f85d-4859-ad28-4bc98470fe63.png">  

### Box Detection Page  
<img width="1390" alt="스크린샷 2023-02-20 오후 4 00 36" src="https://user-images.githubusercontent.com/112835087/220035726-7b73c749-a29f-4aa8-bba9-14de7cda6744.png">  

### Tracking number Page   
<img width="1389" alt="스크린샷 2023-02-20 오후 4 00 51" src="https://user-images.githubusercontent.com/112835087/220036983-1b3a7d94-17e4-45ee-ba6c-3c18363c46be.png">  

--- 
# 📊 Result

<img width="900" alt="스크린샷 2023-02-20 오전 11 37 41" src="https://user-images.githubusercontent.com/112835087/219996877-26ea1b7a-0ae9-4607-adb2-3ced414ba8e6.png">

<img width="900" alt="스크린샷 2023-02-17 오후 5 24 48" src="https://user-images.githubusercontent.com/112835087/219592154-6165df04-bad7-4c72-bc9a-3a1802e81278.png"> 
<img width="900" alt="스크린샷 2023-02-20 오전 11 34 45" src="https://user-images.githubusercontent.com/112835087/219996520-81a91314-011e-4cdb-ad3a-8fea6d395f57.png">

### 모델별 성능 요약  
- YOLOv8 > YOLOv5  
- 인퍼런스와 mAP 자체 test 결과 YOLOv8 이 적합하다 판단하여 YOLOv8로 기본 모델 선정  
- YOLOv5 model의 reference를 보며 YOLOv8의 모델 서빙 진행

<img width="1289" alt="스크린샷 2023-02-20 오전 10 17 47" src="https://user-images.githubusercontent.com/112835087/219988314-ff48836f-de19-4478-816b-dbd4322bef9c.png">  

### 모델선정   
YOLOv8.pt 파일의 가중치 용량이다.  
- 가중치 파일의 용량을 보면 웨이트수가 많은 모델이 역시 모델 크기가 큼  
-> 평균 0.83 이상의 mAP 결과를 도출해주었기 때문에 n(nano) 모델로 선정.  
- test 셋을 구성해서, 크기별로 자체 테스트 도입해보았으나 인퍼런스타임 차이가 컸다.  
-> 인퍼런스 타임이 빠른 n(nano) 모델로 웹 서빙 모델을 2개를 서빙  

---

# 📷 Show Result  

<img width="900" alt="스크린샷 2023-02-20 오전 11 39 24" src="https://user-images.githubusercontent.com/112835087/219997121-f5de5fcd-4494-4a93-8b31-ef6b887be0fb.png">
<img width="900" alt="스크린샷 2023-02-20 오전 11 39 31" src="https://user-images.githubusercontent.com/112835087/219997128-da967a9a-8451-4218-b571-fb55fece6d5e.png">


---


# 🙆 Conclusion 
### Positive point
1.  현실이나 현업에는 우리가 원하는 데이터셋이 없을 가능성이 높다! 그래서 우리가 직접데이터를 만들자 직접 데이터 제작, 수집, 가공 처리  
😀 Hand Made Data Set 구성! 

2. 모델안의 하이퍼 파라미터를 활용 (프로젝트를 진행하면서 데이터자체가 같은 구도에서만 촬영이되어, Small Detection을 학습이 필요)   
-> perspective의 값을 주어, Train 에서 agumentation효과를 주어 성능개선이 가능했다.  

3. 새로운모델, 다양한 관점에서 모델링 Task 변경 시도 (현재 순차적인 데이터, OCR 모델링 제작중)  
-> 한가지 관점으로만 바라보지 말 것.  
-> 기존 OCR 취약점의 개선하기 위해 자체 모델링 구상중이다.  

### Lesson learned 
1.  Cv 분야에서 중요한 데이터에 대한 이해도와 Task 이해도 능력 향상  
-> image classfication , Object Detection 에서 중요한 Annotation 의 패턴, 요소를 분석하여 작업 , Hyper Params 를 적극적으로 이해하고 활용하자. 

2.  모델의 코드를 열어보며 리딩하며 코딩에 대한 이해도  
-> detect, predict, train, valid 등 file 코드를 읽어보기.  

3.  프로젝트에서 중요한건 팀원과의 소통 및 꺾이지 않는 마음  
-> 결국은 팀프로젝트에서 중요한것은 소통과 화합이다.



---

# 💻 Requirements  
❗️YOLOv5
```python
# pip install -r requrements.txt
gitpython
ipython  # interactive notebook
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.1
Pillow>=7.1.2
psutil  # system resources
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
thop>=0.1.1  # FLOPs computation
torch>=1.7.0  # see https://pytorch.org/get-started/locally (recommended)
torchvision>=0.8.1
tqdm>=4.64.0
# protobuf<=3.20.1  # https://github.com/ultralytics/yolov5/issues/8012
```

❗️YOLOv7
```python
# pip install -r requrements.txt
matplotlib>=3.2.2
numpy>=1.18.5,<1.24.0
opencv-python>=4.1.1
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch>=1.7.0,!=1.12.0
torchvision>=0.8.1,!=0.13.0
tqdm>=4.41.0
protobuf<4.21.3
```
---

❗️YOLOv8
```python
# pip install Ultralytics
pip install -r requrements.txt
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.6.0
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.64.0
```
---

# 🔧 Project Structure

<img width="420" alt="스크린샷 2023-02-21 오후 1 06 15" src="https://user-images.githubusercontent.com/112835087/220245141-956c6505-1953-4621-a676-909062a02215.png">



# 📜 Reference  
- [YOLOv5](https://github.com/ultralytics/yolov5)  
- [YOLOv8](https://github.com/ultralytics/yolov8)
- [YOLOv7](https://github.com/WongKinYiu/yolov7)
  
---
