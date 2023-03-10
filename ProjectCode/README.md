# ๐ฆ Logistics Packge Realtime Detection ๐ฆ
<img src="https://www.dailylog.co.kr/news/photo/201204/3888_1733_4612.jpg" width="700" height="370" div align="center">

---

# ๐ฅ Team 
[๊น์ฌํ](http://https://github.com/jh941213) | [์ด์ฑ์ฐ](https://github.com/deepshadow25)
------|------|
Team Leader|Team Member|
<img src="https://user-images.githubusercontent.com/112835087/214769736-c6880568-a4f9-42f7-b5d9-3ef466b6a997.jpeg" width="100" height="100">|<img src="https://user-images.githubusercontent.com/112835087/214769769-f12d45ae-6b09-4567-b142-591c73ccffdb.png" width="100" height="100">

# ๐ฅ๏ธ Team Preferences  
<img width="1252" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฅแซ 11 05 07" src="https://user-images.githubusercontent.com/112835087/219992649-746bb69d-0220-49d5-9882-300110dce746.png" width='100' height='300'>  

---

[๐Procedures(Time Stamp)](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)

>**[2023.01.02 ~ 2023.01.06]**
>- ํ๋ก์ ํธ ์ฃผ์  ํ์ ๋ฐ ์ ์ 
>- ํ๋ก์ ํธ ๊ณํ ๊ตฌ์
><br>
>
>**[2023.01.06 ~ 2023.01.18]**
>- ๋ฐ์ดํฐ ์์ง ๋ฐ ์ ์ฒ๋ฆฌ
>   - Anomaly Detection ํน์ฑ์ ๋ถ๋๋ฐ์ดํฐ๋ฅผ ๊ตฌํ๊ธฐ ์ด๋ ค์ ์ผ๋ฏ๋ก ์ด๋ฅผ ์ง์  ๋ง๋ค์ด๋.
>   - ๊ฐ์ฅ ๋ณดํธ์ ์ธ ํ๋ฐฐ ์์(๊ฐ์ ํ์ง ์์)์ ๋ฐ์ดํฐ๋ง์ ๊ณ ๋ ค
><br>
>
>**[2023.01.14 ~ 2023.01.16]**
>- 1์ฐจ Model training and testing
>   - Real Time & Anomaly Detection
>   - Train, valid dataset split
>   - Data Augmentation
><br>
>
>**[2023.01.17 ~ 2023.01.24]**
>- 1์ฐจ Anomaly Detection model result ๋ถ์, ํ๊ฐ
>   - Annotating ๋ํญ ์์  
>- OCR / Model serving Reference Searching ์์
>   - App service ๊ณํ์ด ์์์ผ๋ ์ฐจํ๋ก ๋ฏธ๋ฃธ.
><br>
>
>**[2023.01.25 ~ 2023.01.27]**  
>- 2์ฐจ Detection Model training and testing
>   - ์์ ๋ Annotating ์ ์ฉ
>   - Resolution ์กฐ์  (640*640 -> 1280*1280)
>   - ๊ฒฐ๊ณผ ๋ถ์, ํ๊ฐ ํ 3์ฐจ๋ก ๋์ด๊ฐ
>- Github repository ๊ฒฐ๊ณผ๋ฌผ ์ ๋ฆฌ
>   - Readme ์์ฑ ์์
><br>
>
>**[2023.01.28 ~ 2023.02.06]**  
>- OCR model ์ค๋น
>   - ํ๋ฐฐ ์ด์ก์ฅ ๋ฐ์ดํฐ ์ค๋น (์์์ ์ฃผ์๋ฐ์ดํฐ ์์ฑ, ์ก์ฅ ์ธ์)
>   - OCR API test (Google Cloud Vision, Naver Clova)
>   - OCR model searching (EazyOCR, Tesseract ๋ฑ)
>- 3์ฐจ Detection model training and testing
>   - use EfficientDet models. (D0, D1)
>   - also used Yolo models : Yolo๊ฐ Eff.Det๋ณด๋ค ๋์ ํ์ธ
>- App ๊ตฌํ ๊ณํ์ Web Serving์ผ๋ก ์์ . (Insight ๋ค์๋ณด๊ธฐ)
>   - ๊ณ ๊ฐ์๊ฒ ์๋ฆผ์ ๋ฐ์กํ๋ ๊ธฐ๋ฅ์ด ํ์์์.
>   - ๋ฌผ๋ฅํ์ฌ(๊ณต์ฅ) ๋ด๋ถ์์๋ง ์ฌ์ฉํ๋ ํ๋ก๊ทธ๋จ์ผ๋ก ์ฌ์ฉ : ์น์ผ๋ก๋ง ๊ตฌํํด๋ ๋จ.
><br>
>
>**[2023.02.07 ~ 2023.02.13]**
>- Web Serving ๊ตฌ์ถ (Flask)
>  - ์ค์๊ฐ ๊ตฌ์ถ ์น ์ฌ์ดํธ ๊ตฌํ
>  - ์น UI ์ ์ (๋ถ๋๊ฒ์ถ : ๊ฒ์ถํ๋ ๊ฒ ๋ณด์ฌ์ฃผ๊ธฐ / ์ก์ฅ์ธ์ : OCR bbox ์ ์ฅ+crop)
>- OCR Data train + inference ์์
>  - Tesseract, Naver Clova API, EazyOCR ๋ฑ ์ฌ์ฉ
>  - ์ก์ฅ ์ฌ์ง 100์ฌ ์ฅ์์ ๊ฐ ์ซ์ + "์ด์ก์ฅ๋ฒํธ" ๊ธ์์ bounding box ์ง์ , inference
>    - Yolo v8 ๊ธฐ๋ฐ์ผ๋ก ๋ชจ๋ธ ๋ง๋ค๊ธฐ ๋์ . 20,000 Epoch ์๋.
><br>
>
>**[2023.02.13 ~ 2023.02.16]**
>- Presentation ์ค๋น
>   - Data, Model, OCR, Git, any other process ์ ๋ฆฌ
>   - ๋ฐํ ๋๋ณธ ์ ์, ๋์์ธ ๊ตฌ์
>- DB ๊ตฌ์ถ
>
>- OCR ์์ 
>
><br>
>
>**[2023.02.17]**
>- ์ค๊ฐ๋ฐํ ๋ฐ ์ ๊ฒ.
---

# Index
- [๐ Project Summary](#project-summary)
- [๐ฆ Data Set](#Data-set)
- [๐ Model Serving](#Model-Serving)
- [๐Procedures(Time Stamp)](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)
- [๐ฅ Roles](#-roles)
- [๐ง Feature](#-feature)
- [๐ Result](#-result)
- [๐ท Show Result](-Show-Result)
- [๐ป Requirements](#-requirements)
- [๐ง Folder Structure](#-folder-structure)
- [๐ Reference](#-Reference)

---

# ๐Project Summary
> - ์ฃผ์   
> ๋ฌผ๋ฅ์ผํฐ(HUB, CAMP) ๋ฑ ์ปจํ์ด๋ ๋ฒจํธ ๊ณผ์ ์์ ๋ฐ์ค ํจํค์ง์ ์ฐข์ด์ง๊ฑฐ๋ ์ ์๊ณผ ๊ฐ์ ๊ฒฐํจ์ RealTime Detection ํ์ฌ ๊ฐ ๋ ์ผ์ ์์น์ ์๋ ์ธ์ ์์์ AI ๋ก ๋์ฒดํด ์๋ํ์์คํ์ ๊ตฌ์ถ  

> - ์ธ์ฌ์ดํธ  
> ์ฟ ํก๊ณผ ๊ฐ์ ๋ํ๋ฌผ๋ฅ ์ผํฐ์์๋ ์คํ ์ํฐ์ ๊ฐ์ ์ก์ฅ์ ๋ณด๋ฅผ ์ธ์ํ๋ ๋ฐ์ฝ๋๊ธฐ๋ฐ์ ๋ํ์ผ์ ์ฅ๋น๊ฐ ๊ตฌ๋น๋์ด ํ์ฌ ์๋ํ ์์คํ์ ๊ตฌ์ถํ๊ณ  ์๋ค๊ณ  ํ๋ค. ๊ทผ๋ฐ ๊ทธ ๊ณผ์ ์์ ๊ธฐ์กด ๋ ์ผ์ ์ฒ ์ ๋ฐ ์ฌ ์ ๋น ์ค์น ๊ณผ์ ์์ ๋ง๋ํ ๋น์ฉ๊ณผ ์คํ ์ํฐ ์์ฒด์ ํฐ ๋น์ฉ์ผ๋ก ์ธํด ์ฐ๋ฆฌ์ AI ๋ชจ๋ธ์ ์ฌ์ฉํ๋ค๋ฉด ์ ๋น์ฉ ๊ณ ํจ์จ์ด๋ ํจ๊ณผ๋ฅผ ๋ผ ์ ์์ง ์์๊น๋ ์๊ฐ. ๊ณ ๊ฐ๊ฒฝํ์ด ์ข์์ง๊ณ , ์ค์์ฐจ ์ค๋ฐฐ์ก์ ๋ํ ๋ฐ์ดํฐ ์ถ์ ์ผ๋ก ๋ด๋ถ ํ๋ก์ธ์ค ํ๊ฐ ๋ฐ์ ๊ฐ๋ฅ ๋ฑ B2B, B2C ๊ด์ ์์ ๋ค์ํ ๋ถ๋ถ์ผ๋ก ์ธ์ , ๊ฒฝ์ ์ ์ธ ์ด๋์ด ๊ฐ๋ฅํ๋ค.  

---

# ๐ฆ Data Set  
## Data Set Annotation  
 ๋ผ๋ฒจ : Hole(๊ตฌ๋ฉ, ์ฐข์ด์ง), Wet(์ ์)  
 Annotation ์ ์ํ์ฌ Hole, Wet์ ์ผ์  ํจํด์ ํ์ํ์ฌ ๋ฐ๋ณต ํ์ต ํ  ์ ์๋๋ก Annotation ์์ ์งํ (Key Point)๐   
 Hole ๊ฐ์ ๊ฒฝ์ฐ ํฝ์์์ฒด๊ฐ ๊ฒ์ ์ ๋ถ๋ถ์ด ๋ง์ด ๋์ค๊ธฐ ๋๋ฌธ์ ๊ฒ์ ์์ด๋ผ๋์ง , ๊ตฌ๋ฉ์ด ๋ซ๋ ค์์ ๋์ ํน์ง์ ์๊ฐ ํ์ฌ Annotation์ ํ์๋ค.  
 Wet ๊ฐ์ ๊ฒฝ์ฐ ๋๋ฌด ๊ฒฝ์ฐ์ ๋ณ์๊ฐ ๋ง์์ ๊ธฐ์ค์ ์ก๊ณ  ์ ์ฒด์ ์ผ๋ก ์ ์๋ฐ์ค ์ ์ด์ง ์ ๋๋ผ๋ ์ด๊ฑด ๋ถ๋์ด๋ค ์ถ์ ๋ฐ์ค๋ง ํ์ตํ์๋ค. ์ด์ ๋ ์ด์ง๋ฌป์ ๋ฌผ์๋ ๋ํ์์ ํด๋ฒ๋ฆฌ๋ฉด ๋ชจ๋ธ์์ฒด๊ฐ ์๋ฏธ๊ฐ ์๊ธฐ ๋๋ฌธ์ ์ ์๊ฐํ๊ณ  ํ๋จํ์ฌ annotation์์์ ํ์๋ค. 

## Data Set ๊ตฌ์ฑ

### 1๋จ๊ณ : ์น ํฌ๋กค๋ง ์ ํตํ์ฌ ๋ฐ์ดํฐ ์์ง (987์ฅ)  
<img width="612" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 4 39 12" src="https://user-images.githubusercontent.com/112835087/220042612-52484d5e-66b8-4cf8-8e41-ec2dcde76775.png">  

### 2๋จ๊ณ : ์น ํฌ๋กค๋ง ์์ฒด์ ์ธ ๊ธธ๊ฑฐ๋ฆฌ ํ์ ๋ฐ์ดํฐ ์์ง (1684์ฅ)  
<img width="612" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 4 39 12" src="https://user-images.githubusercontent.com/112835087/220042773-d6daa80c-1758-40d5-8247-dbfa3cf6bb05.png">  

### 3๋จ๊ณ : ๊ฐ์๋ฐ์ค ์์ ๊ตฌ๋งคํ ์์ฒด์ ์ธ ๋ฐ์ดํฐ์ ์ ์ (3287์ฅ)   
<img width="607" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 4 40 45" src="https://user-images.githubusercontent.com/112835087/220042859-f769a323-bf14-4b64-b198-412931588292.png">  

โTotal Data Set ๊ตฌ์ฑ  
image : 3287์ฅ, ๊ฐ์ฒด ์ : 4,837๊ฐ, Hole(๊ตฌ๋ฉ,์ฐข์ด์ง) : 2,226๊ฐ , Wet(์ ์) : 2,611๊ฐ  


๋ฐ์ดํฐ ์ข๋ฅ| ์ผ์ | ์ฌ์ฉ๊ธฐ์  | ๋งํฌ
 ------------|------|-------|-----|
Box data | 2023 | YOLOv8 | [Box data](https://universe.roboflow.com/jaehyun-kim/finalbox)
Tracking data | 2023 | YOLOv8 | [Tracking data](https://universe.roboflow.com/deeple/trackingnumberod)

<img width="747" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 4 46 36" src="https://user-images.githubusercontent.com/112835087/220043929-748afad6-e9f6-4e15-8fa9-b606af1c46f8.png">

 - image size & resize  
 640 x 640 -> 1280 x 1280 -> 2048 x 2048  
 --> yolov7 ๋ผ๋ฌธ ์ฐธ์กฐ์ ๋ฐ์ดํฐ์ 640 x 640 ํ์ต ์ถํ ๋ฐ์ดํฐ ํธ๋ค๋ง์ ํตํ์ฌ resize ์์ ์งํ

 - Augmentation  
 crop 10ยฐ -> ๋ฐ์ดํฐ ์ฆ๊ฐ์ ์ํ Agumentation  
 yolov7, yolov8 hyper param ๊ธฐ๋ฅ agumentation: True  
 (Mosaic : 1.0, fliplr : 0.5, scale : 0.5, translate : 0.1, hsv_h : 0.015, hsv_s = 0.7, hsv_v = 0.4)

---

# ๐๏ธ Image Processing
## open-CV ๋ฅผ ํ์ฉํ ์ด๋ฏธ์ง ์ ์ฒ๋ฆฌ  

- ์ ์ฉ ๋ฐ์ดํฐ : ๐ Tracking number Detection Data!  

1๏ธโฃ Zero-Padding  
์ง์  ์ง  zero-padding ์ฝ๋๋ฅผ ์ด์ฉํ์ฌ, ์ด๋ฏธ์ง๋ฅผ ๋ชจ๋ธ input size ๋ฅผ ๋ง์ถ๊ธฐ์ํด ์ ์ฒ๋ฆฌ๋ฅผ ํด์ค๋ค.  
<img width="900" src="https://user-images.githubusercontent.com/112835087/220052065-ad5ed28f-9487-434b-8f0d-5be4db838b26.jpg">

2๏ธโฃ GrayScale  
์ํ ํ Text Recognize ๋ฅผ ์ํ GrayScale ๋ฅผ ์งํํด์ค๋ค.  
<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 5 21 25" src="https://user-images.githubusercontent.com/112835087/220053078-c2ea2385-3a2b-4929-8a86-bb5cf09785a0.png">  

3๏ธโฃ Binary   
GrayScale์ด ๋ Data๋ฅผ Binary ํ๋ฅผ ์งํํด์ค๋ค.  
<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 5 21 31" src="https://user-images.githubusercontent.com/112835087/220053336-7742bc3a-c5f4-4356-85c3-c349285bca91.png">  

4๏ธโฃ Remove Noise   
noise ์ ๊ฑฐ๋ฅผ ํตํ recognize ์ค๋น  
<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 5 21 37" src="https://user-images.githubusercontent.com/112835087/220053671-d4821360-fc71-485a-be47-38cffbf6af7d.png">  

---
# ๐ Model Serving

> - Model serving  
> Flask ๋ฅผ ํ์ฉํ์ฌ local host ์น ์๋ฒ ๊ตฌ์ถ (์ฌ์ฉ์ local์ ์์ญ์ ๋ฐ๋๋ค.  
> Box Detect page, Tracking number page(OCR) ์ ๊ตฌ๋ถํ์ฌ ๋ ํ์ด์ง ์์ญ ๊ตฌ์ฑ  
> mySQL ์ ์ด์ฉํ์ฌ detection ๊ฒ์ถ๋ ๋ด์ฉ DB ์ ์ฅ, 
>
### Main Page  
<img width="2045" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 3 49 26" src="https://user-images.githubusercontent.com/112835087/220034085-9130524a-f85d-4859-ad28-4bc98470fe63.png">  

### Box Detection Page  
<img width="1390" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 4 00 36" src="https://user-images.githubusercontent.com/112835087/220035726-7b73c749-a29f-4aa8-bba9-14de7cda6744.png">  

### Tracking number Page   
<img width="1389" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฎ 4 00 51" src="https://user-images.githubusercontent.com/112835087/220036983-1b3a7d94-17e4-45ee-ba6c-3c18363c46be.png">



---

# [๐Procedures(Time Stamp)](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)

---

# ๐ฅ Roles
> - ๊น์ฌํ : modeling by yolov7, yolov8(Train, Valid, Test), OCR Modeling, Flask Serving Coding, mySQL build
> - ์ด์ฑ์ฐ : Data Process, YOLO model thesis reference serch, YOLOV4 Modeling

---

# ๐ง Feature
> - Detection ์ต์ ์ ๋ชจ๋ธ์ ์ฐพ๊ธฐ ์ํ YOLO, efficientDet, CoreML๋ฑ ๊ฐ์ฒด๋ชจ๋ธ ํ์ต ๋ฐ ํ์คํธ  
> - Make Data Set ๊ตฌ์ถ์ ์ํ ํ์ค์์์ ๋ฐ์ดํฐ ์ Searh & Make  
> - EasyOCR, Tesseract, MMOCR ๋ฑ ์คํ์์ค๊ธฐ๋ฐ์ OCR ๋ชจ๋ธ ์ฌ์  ํ์คํธ ๋ฐ fine tune  
> - NAVER Clova AI, KAKAO ๋ฑ ๊ตญ๋ด ๊ธฐ์์ OCR API ์ฌ์ฉ 

---
# ๐ Result

<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฅแซ 11 37 41" src="https://user-images.githubusercontent.com/112835087/219996877-26ea1b7a-0ae9-4607-adb2-3ced414ba8e6.png">

<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-17 แแฉแแฎ 5 24 48" src="https://user-images.githubusercontent.com/112835087/219592154-6165df04-bad7-4c72-bc9a-3a1802e81278.png"> 
<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฅแซ 11 34 45" src="https://user-images.githubusercontent.com/112835087/219996520-81a91314-011e-4cdb-ad3a-8fea6d395f57.png">

### ๋ชจ๋ธ๋ณ ์ฑ๋ฅ ์์ฝ  
- YOLOv8 > YOLOv5  
- ์ธํผ๋ฐ์ค์ mAP ์์ฒด test ๊ฒฐ๊ณผ YOLOv8 ์ด ์ ํฉํ๋ค ํ๋จํ์ฌ YOLOv8๋ก ๊ธฐ๋ณธ ๋ชจ๋ธ ์ ์   
- YOLOv5 model์ reference๋ฅผ ๋ณด๋ฉฐ YOLOv8์ ๋ชจ๋ธ ์๋น ์งํ

<img width="1289" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฅแซ 10 17 47" src="https://user-images.githubusercontent.com/112835087/219988314-ff48836f-de19-4478-816b-dbd4322bef9c.png">  

### ๋ชจ๋ธ์ ์    
YOLOv8.pt ํ์ผ์ ๊ฐ์ค์น ์ฉ๋์ด๋ค.  
- ๊ฐ์ค์น ํ์ผ์ ์ฉ๋์ ๋ณด๋ฉด ์จ์ดํธ์๊ฐ ๋ง์ ๋ชจ๋ธ์ด ์ญ์ ๋ชจ๋ธ ํฌ๊ธฐ๊ฐ ํผ  
-> ํ๊ท  0.83 ์ด์์ mAP ๊ฒฐ๊ณผ๋ฅผ ๋์ถํด์ฃผ์๊ธฐ ๋๋ฌธ์ n(nano) ๋ชจ๋ธ๋ก ์ ์ .  
- test ์์ ๊ตฌ์ฑํด์, ํฌ๊ธฐ๋ณ๋ก ์์ฒด ํ์คํธ ๋์ํด๋ณด์์ผ๋ ์ธํผ๋ฐ์คํ์ ์ฐจ์ด๊ฐ ์ปธ๋ค.  
-> ์ธํผ๋ฐ์ค ํ์์ด ๋น ๋ฅธ n(nano) ๋ชจ๋ธ๋ก ์น ์๋น ๋ชจ๋ธ์ 2๊ฐ๋ฅผ ์๋น  

---

# ๐ท Show Result  

<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฅแซ 11 39 24" src="https://user-images.githubusercontent.com/112835087/219997121-f5de5fcd-4494-4a93-8b31-ef6b887be0fb.png">
<img width="900" alt="แแณแแณแแตแซแแฃแบ 2023-02-20 แแฉแแฅแซ 11 39 31" src="https://user-images.githubusercontent.com/112835087/219997128-da967a9a-8451-4218-b571-fb55fece6d5e.png">


---


# ๐ Conclusion 
### Positive point๐
1.  ํ์ค์ด๋ ํ์์๋ ์ฐ๋ฆฌ๊ฐ ์ํ๋ ๋ฐ์ดํฐ์์ด ์์ ๊ฐ๋ฅ์ฑ์ด ๋๋ค! ๊ทธ๋์ ์ฐ๋ฆฌ๊ฐ ์ง์ ๋ฐ์ดํฐ๋ฅผ ๋ง๋ค์ ์ง์  ๋ฐ์ดํฐ ์ ์, ์์ง, ๊ฐ๊ณต ์ฒ๋ฆฌ  
๐ Hand Made Data Set ๊ตฌ์ฑ! 

2. ๋ชจ๋ธ์์ ํ์ดํผ ํ๋ผ๋ฏธํฐ๋ฅผ ํ์ฉ (ํ๋ก์ ํธ๋ฅผ ์งํํ๋ฉด์ ๋ฐ์ดํฐ์์ฒด๊ฐ ๊ฐ์ ๊ตฌ๋์์๋ง ์ดฌ์์ด๋์ด, Small Detection์ ํ์ต์ด ํ์)   
-> perspective์ ๊ฐ์ ์ฃผ์ด, Train ์์ agumentationํจ๊ณผ๋ฅผ ์ฃผ์ด ์ฑ๋ฅ๊ฐ์ ์ด ๊ฐ๋ฅํ๋ค.  

3. ์๋ก์ด๋ชจ๋ธ, ๋ค์ํ ๊ด์ ์์ ๋ชจ๋ธ๋ง Task ๋ณ๊ฒฝ ์๋ (ํ์ฌ ์์ฐจ์ ์ธ ๋ฐ์ดํฐ, OCR ๋ชจ๋ธ๋ง ์ ์์ค)  
-> ํ๊ฐ์ง ๊ด์ ์ผ๋ก๋ง ๋ฐ๋ผ๋ณด์ง ๋ง ๊ฒ.  
-> ๊ธฐ์กด OCR ์ทจ์ฝ์ ์ ๊ฐ์ ํ๊ธฐ ์ํด ์์ฒด ๋ชจ๋ธ๋ง ๊ตฌ์์ค์ด๋ค.  

### Lesson learned๐ค  
1.  Cv ๋ถ์ผ์์ ์ค์ํ ๋ฐ์ดํฐ์ ๋ํ ์ดํด๋์ Task ์ดํด๋ ๋ฅ๋ ฅ ํฅ์  
-> image classfication , Object Detection ์์ ์ค์ํ Annotation ์ ํจํด, ์์๋ฅผ ๋ถ์ํ์ฌ ์์ , Hyper Params ๋ฅผ ์ ๊ทน์ ์ผ๋ก ์ดํดํ๊ณ  ํ์ฉํ์. 

2.  ๋ชจ๋ธ์ ์ฝ๋๋ฅผ ์ด์ด๋ณด๋ฉฐ ๋ฆฌ๋ฉํ๋ฉฐ ์ฝ๋ฉ์ ๋ํ ์ดํด๋  
-> detect, predict, train, valid ๋ฑ file ์ฝ๋๋ฅผ ์ฝ์ด๋ณด๊ธฐ.  

3.  ํ๋ก์ ํธ์์ ์ค์ํ๊ฑด ํ์๊ณผ์ ์ํต ๋ฐ ๊บพ์ด์ง ์๋ ๋ง์  
-> ๊ฒฐ๊ตญ์ ํํ๋ก์ ํธ์์ ์ค์ํ๊ฒ์ ์ํต๊ณผ ํํฉ์ด๋ค.



---

# ๐ป Requirements  
โ๏ธYOLOv5
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

โ๏ธYOLOv7
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

โ๏ธYOLOv8
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

# ๐ง Folder Structure

<img width="420" alt="แแณแแณแแตแซแแฃแบ 2023-02-21 แแฉแแฎ 1 06 15" src="https://user-images.githubusercontent.com/112835087/220245141-956c6505-1953-4621-a676-909062a02215.png">



# ๐ Reference  
- [YOLOv5](https://github.com/ultralytics/yolov5)  
- [YOLOv8](https://github.com/ultralytics/yolov8)
- [YOLOv7](https://github.com/WongKinYiu/yolov7)
  
---


