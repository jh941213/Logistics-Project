# π¦ Logistics Packge Realtime Detection π¦
<img src="https://www.dailylog.co.kr/news/photo/201204/3888_1733_4612.jpg" width="700" height="370" div align="center">

---

# π₯ Team 
[κΉμ¬ν](http://https://github.com/jh941213) | [μ΄μ±μ°](https://github.com/deepshadow25)
------|------|
Team Leader|Team Member|
<img src="https://user-images.githubusercontent.com/112835087/214769736-c6880568-a4f9-42f7-b5d9-3ef466b6a997.jpeg" width="100" height="100">|<img src="https://user-images.githubusercontent.com/112835087/214769769-f12d45ae-6b09-4567-b142-591c73ccffdb.png" width="100" height="100">

# π₯οΈ Team Preferences  
λΉκ³ |local(κΉμ¬ν)|local(μ΄μ±μ°) | AWS Server | Google Colab
-----|-------|-------|-------|-------|
CPU | Apple M1(10core)|i7-8565U| i7 4core|Xeon(R)cpu 2.3GHz|
RAM |32GB|16GB|16GB|13~52GB|  
Storage |512GB|512GB|250GB|166GB|
OS |macOS ventura|Window 10|-|-|
MOBILE |Iphone 13 Mini|Galaxy S10|-|-|  

# Index
- [π Project Summary](#project-summary)
- [π Schedule(Time Stamp)](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)
- [π₯ Roles](#-roles)
- [π§ Feature](#-feature)
- [π¦ Data Set](#-Data-set)
- [ποΈ Image Processing](#-image-Processing)
- [π Model Serving](#-model-serving)
- [βοΈ Coding](#-coding)
- [π Result](#-result)
- [π· Show Result](-show-result)
- [π Conclusion](#-conclusion)
- [π» Requirements](#-requirements)
- [π§ Folder Structure](#-folder-structure)
- [π Reference](#-Reference)

---

# πProject Summary
> - μ£Όμ   
> λ¬Όλ₯μΌν°(HUB, CAMP) λ± μ»¨νμ΄λ λ²¨νΈ κ³Όμ μμ λ°μ€ ν¨ν€μ§μ μ°’μ΄μ§κ±°λ μ μκ³Ό κ°μ κ²°ν¨μ RealTime Detection νμ¬ κ° λ μΌμ μμΉμ μλ μΈμ μμμ AI λ‘ λμ²΄ν΄ μλνμμ€νμ κ΅¬μΆ  

> - μΈμ¬μ΄νΈ  
> μΏ ν‘κ³Ό κ°μ λνλ¬Όλ₯ μΌν°μμλ μ€ν μν°μ κ°μ μ‘μ₯μ λ³΄λ₯Ό μΈμνλ λ°μ½λκΈ°λ°μ λνμΌμ μ₯λΉκ° κ΅¬λΉλμ΄ νμ¬ μλν μμ€νμ κ΅¬μΆνκ³  μλ€κ³  νλ€. κ·Όλ° κ·Έ κ³Όμ μμ κΈ°μ‘΄ λ μΌμ μ² μ λ° μ¬ μ λΉ μ€μΉ κ³Όμ μμ λ§λν λΉμ©κ³Ό μ€ν μν° μμ²΄μ ν° λΉμ©μΌλ‘ μΈν΄ μ°λ¦¬μ AI λͺ¨λΈμ μ¬μ©νλ€λ©΄ μ λΉμ© κ³ ν¨μ¨μ΄λ ν¨κ³Όλ₯Ό λΌ μ μμ§ μμκΉλ μκ°. κ³ κ°κ²½νμ΄ μ’μμ§κ³ , μ€μμ°¨ μ€λ°°μ‘μ λν λ°μ΄ν° μΆμ μΌλ‘ λ΄λΆ νλ‘μΈμ€ νκ° λ°μ κ°λ₯ λ± B2B, B2C κ΄μ μμ λ€μν λΆλΆμΌλ‘ μΈμ , κ²½μ μ μΈ μ΄λμ΄ κ°λ₯νλ€.  


---

# [π Schedule(Time Stamp)](https://timetreeapp.com/calendars/Bs7yrwhD6Q5H)

>**[2023.01.02 ~ 2023.01.06]**
>- νλ‘μ νΈ μ£Όμ  νμ λ° μ μ 
>- νλ‘μ νΈ κ³ν κ΅¬μ
><br>
>
>**[2023.01.06 ~ 2023.01.18]**
>- λ°μ΄ν° μμ§ λ° μ μ²λ¦¬
>   - RealTime Detection νΉμ±μ λΆλλ°μ΄ν°λ₯Ό κ΅¬νκΈ° μ΄λ €μ μΌλ―λ‘ μ΄λ₯Ό μ§μ  λ§λ€μ΄λ.
>   - κ°μ₯ λ³΄νΈμ μΈ νλ°° μμ(κ°μ νμ§ μμ)μ λ°μ΄ν°λ§μ κ³ λ €
><br>
>
>**[2023.01.14 ~ 2023.01.16]**
>- 1μ°¨ Model training and testing
>   - Real Time Detection
>   - Train, valid dataset split
>   - Data Augmentation
><br>
>
>**[2023.01.17 ~ 2023.01.24]**
>- 1μ°¨ Real Detection model result λΆμ, νκ°
>   - Annotating λν­ μμ  
>- OCR / Model serving Reference Searching μμ
>   - App service κ³νμ΄ μμμΌλ μ°¨νλ‘ λ―Έλ£Έ.
><br>
>
>**[2023.01.25 ~ 2023.01.27]**  
>- 2μ°¨ Detection Model training and testing
>   - μμ λ Annotating μ μ©
>   - Resolution μ‘°μ  (640*640 -> 1280*1280)
>   - κ²°κ³Ό λΆμ, νκ° ν 3μ°¨λ‘ λμ΄κ°
>- Github repository κ²°κ³Όλ¬Ό μ λ¦¬
>   - Readme μμ± μμ
><br>
>
>**[2023.01.28 ~ 2023.02.06]**  
>- OCR model μ€λΉ
>   - νλ°° μ΄μ‘μ₯ λ°μ΄ν° μ€λΉ (μμμ μ£Όμλ°μ΄ν° μμ±, μ‘μ₯ μΈμ)
>   - OCR API test (Google Cloud Vision, Naver Clova)
>   - OCR model searching (EazyOCR, Tesseract λ±)
>- 3μ°¨ Detection model training and testing
>   - use EfficientDet models. (D0, D1)
>   - also used Yolo models : Yoloκ° Eff.Detλ³΄λ€ λμ νμΈ
>- App κ΅¬ν κ³νμ Web ServingμΌλ‘ μμ . (Insight λ€μλ³΄κΈ°)
>   - κ³ κ°μκ² μλ¦Όμ λ°μ‘νλ κΈ°λ₯μ΄ νμμμ.
>   - λ¬Όλ₯νμ¬(κ³΅μ₯) λ΄λΆμμλ§ μ¬μ©νλ νλ‘κ·Έλ¨μΌλ‘ μ¬μ© : μΉμΌλ‘λ§ κ΅¬νν΄λ λ¨.
><br>
>
>**[2023.02.07 ~ 2023.02.13]**
>- Web Serving κ΅¬μΆ (Flask)
>  - μ€μκ° κ΅¬μΆ μΉ μ¬μ΄νΈ κ΅¬ν
>  - μΉ UI μ μ (λΆλκ²μΆ : κ²μΆνλ κ² λ³΄μ¬μ£ΌκΈ° / μ‘μ₯μΈμ : OCR bbox μ μ₯+crop)
>- OCR Data train + inference μμ
>  - Tesseract, Naver Clova API, EazyOCR λ± μ¬μ©
>  - μ‘μ₯ μ¬μ§ 100μ¬ μ₯μμ κ° μ«μ + "μ΄μ‘μ₯λ²νΈ" κΈμμ bounding box μ§μ , inference
>    - Yolo v8 κΈ°λ°μΌλ‘ λͺ¨λΈ λ§λ€κΈ° λμ . 20,000 Epoch μλ.
><br>
>
>**[2023.02.13 ~ 2023.02.16]**
>- Presentation μ€λΉ
>   - Data, Model, OCR, Git, any other process μ λ¦¬
>   - λ°ν λλ³Έ μ μ, λμμΈ κ΅¬μ
>- DB κ΅¬μΆ
>
>- OCR μμ 
>
><br>
>
>**[2023.02.17]**
>- μ€κ°λ°ν λ° μ κ².
---

# π₯ Roles
> - κΉμ¬ν : modeling by yolov7, yolov8(Train, Valid, Test), OCR Modeling, Flask Serving Coding, mySQL build
> - μ΄μ±μ° : Data Process, YOLO model thesis reference serch, YOLOV4 Modeling

---

# π§ Feature
> - Detection μ΅μ μ λͺ¨λΈμ μ°ΎκΈ° μν YOLO, efficientDet, CoreMLλ± κ°μ²΄λͺ¨λΈ νμ΅ λ° νμ€νΈ  
> - Make Data Set κ΅¬μΆμ μν νμ€μμμ λ°μ΄ν° μ Searh & Make  
> - EasyOCR, Tesseract, MMOCR λ± μ€νμμ€κΈ°λ°μ OCR λͺ¨λΈ μ¬μ  νμ€νΈ λ° fine tune  
> - NAVER Clova AI, KAKAO λ± κ΅­λ΄ κΈ°μμ OCR API μ¬μ© 

---

# π¦ Data Set  

## Box Data Set Annotation  
 λΌλ²¨ : Hole(κ΅¬λ©, μ°’μ΄μ§), Wet(μ μ)  
 Annotation μ μνμ¬ Hole, Wetμ μΌμ  ν¨ν΄μ νμνμ¬ λ°λ³΅ νμ΅ ν  μ μλλ‘ Annotation μμ μ§ν (Key Point)π   
 Hole κ°μ κ²½μ° ν½μμμ²΄κ° κ²μ μ λΆλΆμ΄ λ§μ΄ λμ€κΈ° λλ¬Έμ κ²μ μμ΄λΌλμ§ , κ΅¬λ©μ΄ λ«λ €μμ λμ νΉμ§μ μκ° νμ¬ Annotationμ νμλ€.  
 Wet κ°μ κ²½μ° λλ¬΄ κ²½μ°μ λ³μκ° λ§μμ κΈ°μ€μ μ‘κ³  μ μ²΄μ μΌλ‘ μ μλ°μ€ μ μ΄μ§ μ λλΌλ μ΄κ±΄ λΆλμ΄λ€ μΆμ λ°μ€λ§ νμ΅νμλ€. μ΄μ λ μ΄μ§λ¬»μ λ¬Όμλ λνμμ ν΄λ²λ¦¬λ©΄ λͺ¨λΈμμ²΄κ° μλ―Έκ° μκΈ° λλ¬Έμ μ μκ°νκ³  νλ¨νμ¬ annotationμμμ νμλ€.  
 
## Tracking Number Data Set Annotation  
 λΌλ²¨ : trackingnumber  
1λ¨κ³ : μ‘μ₯μ μ²΄λ₯Ό νμ΅  -> mAP 0.995 
2λ¨κ³ : μ΄μ‘μ₯λ²νΈκ° μλ μμΉκ°μ νμ΅ -> mAP 0.995  
polygon μ μ΄μ©νμ¬, λ€μν κ°λμμλ μ λνμ ν μ μλλ‘ annotation μμμ ν΄μ£Όμλ€.  

## πBox data set flow

### 1λ¨κ³ : μΉ ν¬λ‘€λ§ μ ν΅νμ¬ λ°μ΄ν° μμ§ (987μ₯)  
<img width="600" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 4 39 12" src="https://user-images.githubusercontent.com/112835087/220042612-52484d5e-66b8-4cf8-8e41-ec2dcde76775.png">  

### 2λ¨κ³ : μΉ ν¬λ‘€λ§ μμ²΄μ μΈ κΈΈκ±°λ¦¬ νμ λ°μ΄ν° μμ§ (1684μ₯)  
<img width="600" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 4 39 12" src="https://user-images.githubusercontent.com/112835087/220042773-d6daa80c-1758-40d5-8247-dbfa3cf6bb05.png">  

### 3λ¨κ³ : κ°μλ°μ€ μμ κ΅¬λ§€ν μμ²΄μ μΈ λ°μ΄ν°μ μ μ (3287μ₯)   
<img width="600" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 4 40 45" src="https://user-images.githubusercontent.com/112835087/220042859-f769a323-bf14-4b64-b198-412931588292.png">  

## πtracking number data set flow

### 1λ¨κ³ : μ‘μ₯ μ μ²΄λ₯Ό Annotation  
<img width="600" height="300" alt="αα³αα³αα΅α«αα£αΊ 2023-02-21 αα©αα? 3 35 41" src="https://user-images.githubusercontent.com/112835087/220266165-738a6e19-0852-447d-8801-dbe6b48c1c72.png">  

### 2λ¨κ³ : μ΄μ‘μ₯λ²νΈ μμΉ κ° Annotation  
<img width="275" alt="αα³αα³αα΅α«αα£αΊ 2023-02-21 αα©αα? 3 21 49" src="https://user-images.githubusercontent.com/112835087/220266264-51fb689e-0618-4570-a824-7416f64dad24.png">

## Total Data Set κ΅¬μ±  
Box DataSet  
image : 3287μ₯, κ°μ²΄ μ : 4,837κ°, Hole(κ΅¬λ©,μ°’μ΄μ§) : 2,226κ° , Wet(μ μ) : 2,611κ°  
Tracking DataSet  
image : 250μ₯ , κ°μ²΄ μ : 250κ°, trackingnumber : 250κ°


λ°μ΄ν° μ’λ₯| μΌμ | μ¬μ©κΈ°μ  | λ§ν¬
 ------------|------|-------|-----|
Box data | 2023 | YOLOv8 | [Box data](https://universe.roboflow.com/jaehyun-kim/finalbox)
Tracking data | 2023 | YOLOv8 | [Tracking data](https://universe.roboflow.com/deeple/trackingnumberod)

<img width="600" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 4 46 36" src="https://user-images.githubusercontent.com/112835087/220043929-748afad6-e9f6-4e15-8fa9-b606af1c46f8.png">
<img width="600" alt="αα³αα³αα΅α«αα£αΊ 2023-02-21 αα©αα? 3 21 44" src="https://user-images.githubusercontent.com/112835087/220263968-ccf9e9b3-34bb-4d11-8971-d06969568954.png">

 ## image size & resize  
 640 x 640 -> 1280 x 1280 -> 2048 x 2048  
 --> yolov7 λΌλ¬Έ μ°Έμ‘°μ λ°μ΄ν°μ 640 x 640 νμ΅ μΆν λ°μ΄ν° νΈλ€λ§μ ν΅νμ¬ resize μμ μ§ν

 ## Augmentation  
 crop 10Β° -> λ°μ΄ν° μ¦κ°μ μν Agumentation  
 yolov7, yolov8 hyper param κΈ°λ₯ agumentation: True  
 (Mosaic : 1.0, fliplr : 0.5, scale : 0.5, translate : 0.1, hsv_h : 0.015, hsv_s = 0.7, hsv_v = 0.4)

---

# ποΈ Image Processing
## open-CV λ₯Ό νμ©ν μ΄λ―Έμ§ μ μ²λ¦¬  

- μ μ© λ°μ΄ν° : π Tracking number Detection Data!  

1οΈβ£ Zero-Padding  
μ§μ  μ§  zero-padding μ½λλ₯Ό μ΄μ©νμ¬, μ΄λ―Έμ§λ₯Ό λͺ¨λΈ input size λ₯Ό λ§μΆκΈ°μν΄ μ μ²λ¦¬λ₯Ό ν΄μ€λ€.  
<img width="900" src="https://user-images.githubusercontent.com/112835087/220052065-ad5ed28f-9487-434b-8f0d-5be4db838b26.jpg">

2οΈβ£ GrayScale  
μν ν Text Recognize λ₯Ό μν GrayScale λ₯Ό μ§νν΄μ€λ€.  
<img width="900" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 5 21 25" src="https://user-images.githubusercontent.com/112835087/220053078-c2ea2385-3a2b-4929-8a86-bb5cf09785a0.png">  

3οΈβ£ Binary   
GrayScaleμ΄ λ Dataλ₯Ό Binary νλ₯Ό μ§νν΄μ€λ€.  
<img width="900" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 5 21 31" src="https://user-images.githubusercontent.com/112835087/220053336-7742bc3a-c5f4-4356-85c3-c349285bca91.png">  

4οΈβ£ Remove Noise   
noise μ κ±°λ₯Ό ν΅ν recognize μ€λΉ  
<img width="900" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 5 21 37" src="https://user-images.githubusercontent.com/112835087/220053671-d4821360-fc71-485a-be47-38cffbf6af7d.png">  

---
# π Model Serving
### WEB(Design)
- [figma](https://www.figma.com/file/y45ZcUjbMDzBwqxLcEm0Ly/%EC%88%9C%EC%96%91%ED%83%9D%EB%B0%B0?node-id=4%3A7074&t=OHy4rcxMU1MTGC3U-4)  

### Flask(freamework)
- Flask λ₯Ό νμ©νμ¬ local host μΉ μλ² κ΅¬μΆ (μ¬μ©μ localμ μμ­μ λ°λλ€.  
- Box Detect page, Tracking number page(OCR) μ κ΅¬λΆνμ¬ λ νμ΄μ§ μμ­ κ΅¬μ±  
- mySQL μ μ΄μ©νμ¬ detection κ²μΆλ λ΄μ© DB μ μ₯

### Main Page  
<img width="2045" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 3 49 26" src="https://user-images.githubusercontent.com/112835087/220034085-9130524a-f85d-4859-ad28-4bc98470fe63.png">  

### Box Detection Page  
<img width="1390" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 4 00 36" src="https://user-images.githubusercontent.com/112835087/220035726-7b73c749-a29f-4aa8-bba9-14de7cda6744.png">  

### Tracking number Page   
<img width="1389" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα? 4 00 51" src="https://user-images.githubusercontent.com/112835087/220036983-1b3a7d94-17e4-45ee-ba6c-3c18363c46be.png">  

---

# βοΈ Coding  
μν ν Processλ₯Ό μ΄λ£¨κΈ° μν΄μ νλμ½λ© μμμ μ€ννλ€.  
1. κ°μ²΄κ° μ€κ°μ κ²μΆλμ΄ μ¬μ§μ μ μ₯νλ λ‘μ§    
-> img size λ₯Ό κ³ λ €νμ¬ , bbox κ°μ maxμΌλ μ¬μ§μ μ μ₯νλ€.  

2. κ²μΆλ κ°μ²΄λ₯Ό μΉ΄μ΄ννμ¬ DBλ₯Ό μ μ₯νλ λ‘μ§  
-> bbox return κ°μ classes λ³λ‘ counting νλ μμ  

3. flagλ₯Ό νμ©νμ¬ 1, 2λ²μ μ€ννλ λ‘μ§  
-> img xμ’νλ₯Ό κΈ°μ€μΌλ‘ flag μμ­μ λ§λ€μ΄μ 0, 1 λ‘ μ‘°κ±΄λ¬Έμ λ§λ€μ΄ λ λ‘μ§μ μ€ννλ μμ 

4. image process μ μ²λ¦¬ λ‘μ§
-> open Cv λ₯Ό ν΅ν grayscale, binary, remove noise ν¨μν νμ¬ μμ

5. OCR API λ‘μ§
-> NAVER, KAKAO API λ₯Ό κ°μ Έμ OCR μ²λ¦¬λ₯Ό ν΄μ£Όλ μμ
--- 
# π Result
## Train Result  

MODEL|CoreML|YOLOv4|YOLOv5|YOLOv7|YOLOv8|EfficientDet
-----|-------|-------|-------|-------|-------|-------|
imgsize|1280x1280|640x640|640x640,1280x1280|640x640,1280x1280|640x640,1280x1280|1280x1280
epochs(best)| 3200|6000|100(78)|100(83)|100(87)|10000(9752)
data|3λ¨κ³|2λ¨κ³|3λ¨κ³|3λ¨κ³|3λ¨κ³ |3λ¨κ³
mAP| 0.78| 0.57| 0.81, 0.85| 0.45| 0.81,0.86| 0.79
agumentation| crop 10| crop10| crop10, hyper params | crop10, hyper params | crop10, hyper params | crop10


<img width="900" alt="αα³αα³αα΅α«αα£αΊ 2023-02-17 αα©αα? 5 24 48" src="https://user-images.githubusercontent.com/112835087/219592154-6165df04-bad7-4c72-bc9a-3a1802e81278.png"> 
<img width="900" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα₯α« 11 34 45" src="https://user-images.githubusercontent.com/112835087/219996520-81a91314-011e-4cdb-ad3a-8fea6d395f57.png">

### λͺ¨λΈλ³ μ±λ₯ μμ½  
- YOLOv8 > YOLOv5  
- μΈνΌλ°μ€μ mAP μμ²΄ test κ²°κ³Ό YOLOv8 μ΄ μ ν©νλ€ νλ¨νμ¬ YOLOv8λ‘ κΈ°λ³Έ λͺ¨λΈ μ μ   
- YOLOv5 modelμ referenceλ₯Ό λ³΄λ©° YOLOv8μ λͺ¨λΈ μλΉ μ§ν

<img width="1289" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα₯α« 10 17 47" src="https://user-images.githubusercontent.com/112835087/219988314-ff48836f-de19-4478-816b-dbd4322bef9c.png">  

### λͺ¨λΈμ μ    
YOLOv8.pt νμΌμ κ°μ€μΉ μ©λμ΄λ€.  
- κ°μ€μΉ νμΌμ μ©λμ λ³΄λ©΄ μ¨μ΄νΈμκ° λ§μ λͺ¨λΈμ΄ μ­μ λͺ¨λΈ ν¬κΈ°κ° νΌ  
-> νκ·  0.83 μ΄μμ mAP κ²°κ³Όλ₯Ό λμΆν΄μ£ΌμκΈ° λλ¬Έμ n(nano) λͺ¨λΈλ‘ μ μ .  
- test μμ κ΅¬μ±ν΄μ, ν¬κΈ°λ³λ‘ μμ²΄ νμ€νΈ λμν΄λ³΄μμΌλ μΈνΌλ°μ€νμ μ°¨μ΄κ° μ»Έλ€.  
-> μΈνΌλ°μ€ νμμ΄ λΉ λ₯Έ n(nano) λͺ¨λΈλ‘ μΉ μλΉ λͺ¨λΈμ 2κ°λ₯Ό μλΉ  

---

# π· Show Result  

<img width="900" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα₯α« 11 39 24" src="https://user-images.githubusercontent.com/112835087/219997121-f5de5fcd-4494-4a93-8b31-ef6b887be0fb.png">
<img width="900" alt="αα³αα³αα΅α«αα£αΊ 2023-02-20 αα©αα₯α« 11 39 31" src="https://user-images.githubusercontent.com/112835087/219997128-da967a9a-8451-4218-b571-fb55fece6d5e.png">


---


# π Conclusion 
### Positive point
1.  νμ€μ΄λ νμμλ μ°λ¦¬κ° μνλ λ°μ΄ν°μμ΄ μμ κ°λ₯μ±μ΄ λλ€! κ·Έλμ μ°λ¦¬κ° μ§μ λ°μ΄ν°λ₯Ό λ§λ€μ μ§μ  λ°μ΄ν° μ μ, μμ§, κ°κ³΅ μ²λ¦¬  
π Hand Made Data Set κ΅¬μ±! 

2. λͺ¨λΈμμ νμ΄νΌ νλΌλ―Έν°λ₯Ό νμ© (νλ‘μ νΈλ₯Ό μ§ννλ©΄μ λ°μ΄ν°μμ²΄κ° κ°μ κ΅¬λμμλ§ μ΄¬μμ΄λμ΄, Small Detectionμ νμ΅μ΄ νμ)   
-> perspectiveμ κ°μ μ£Όμ΄, Train μμ agumentationν¨κ³Όλ₯Ό μ£Όμ΄ μ±λ₯κ°μ μ΄ κ°λ₯νλ€.  

3. μλ‘μ΄λͺ¨λΈ, λ€μν κ΄μ μμ λͺ¨λΈλ§ Task λ³κ²½ μλ (νμ¬ μμ°¨μ μΈ λ°μ΄ν°, OCR λͺ¨λΈλ§ μ μμ€)  
-> νκ°μ§ κ΄μ μΌλ‘λ§ λ°λΌλ³΄μ§ λ§ κ².  
-> κΈ°μ‘΄ OCR μ·¨μ½μ μ κ°μ νκΈ° μν΄ μμ²΄ λͺ¨λΈλ§ κ΅¬μμ€μ΄λ€.  

### Lesson learned 
1.  Cv λΆμΌμμ μ€μν λ°μ΄ν°μ λν μ΄ν΄λμ Task μ΄ν΄λ λ₯λ ₯ ν₯μ  
-> image classfication , Object Detection μμ μ€μν Annotation μ ν¨ν΄, μμλ₯Ό λΆμνμ¬ μμ , Hyper Params λ₯Ό μ κ·Ήμ μΌλ‘ μ΄ν΄νκ³  νμ©νμ. 

2.  λͺ¨λΈμ μ½λλ₯Ό μ΄μ΄λ³΄λ©° λ¦¬λ©νλ©° μ½λ©μ λν μ΄ν΄λ  
-> detect, predict, train, valid λ± file μ½λλ₯Ό μ½μ΄λ³΄κΈ°.  

3.  νλ‘μ νΈμμ μ€μνκ±΄ νμκ³Όμ μν΅ λ° κΊΎμ΄μ§ μλ λ§μ  
-> κ²°κ΅­μ ννλ‘μ νΈμμ μ€μνκ²μ μν΅κ³Ό νν©μ΄λ€.



--- 

# π» Requirements  
βοΈYOLOv5
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

βοΈYOLOv7
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

βοΈYOLOv8
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

# π§ Project Structure

<img width="420" alt="αα³αα³αα΅α«αα£αΊ 2023-02-21 αα©αα? 1 06 15" src="https://user-images.githubusercontent.com/112835087/220245141-956c6505-1953-4621-a676-909062a02215.png">



# π Reference  
- [YOLOv5](https://github.com/ultralytics/yolov5)  
- [YOLOv8](https://github.com/ultralytics/yolov8)
- [YOLOv7](https://github.com/WongKinYiu/yolov7)
  
---
