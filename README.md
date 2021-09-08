# YOLOv5_Training
  * Pytroch, RTX 3090 24G, Ubuntu 18.04 LTS
  * [YOLOv5](github.com/ultralytics/yolov5) 파일 이용

![image](https://user-images.githubusercontent.com/61686244/132514416-5ea0fea6-95c8-4c06-bfcb-c35cbc903537.png)

 * s,m,l,x 모델 제공 

Train
-----
 * 1) 가상환경 생성
 * 2) 
<pre>
<code>
$ git clone https://github.com/ultralytics/yolov5.git
</code>
</pre>
  * 3) train(img, label), valid(img, label) 다운로드 ex) MS COCO, Visdrone 등, [다운로드 사이트](https://roboflow.com/)
  * 4) 다운로드한 데이터 셋에 관하여 주소들을 txt 파일로 합친 뒤 경로 재설정 : dataset_glob.py
  * 5) data.yaml 파일의 데이터 셋 경로 변경 : dataset_root.py
  * 6)
<pre>
<code>
$ python3 train.py --img 640 --batch 16 --epochs "학습 횟수" --data "data.yaml 파일 경로"/data.yaml --cfg "모델 크기 경로"/yolov5s.yaml --weights "사전 학습된 가중치 파일 사용시 이용"yolov5s.pt --name "학습된 가중치 및 중간결과 확인 dir 이름"
</code>
</pre>

Test
----
<pre>
<code>
$ python3 detect.py --weights "학습된 가중치 경로"/weights/best.pt --img 640 --conf 0.5 --source "test 영상 경로"/valid/images/test.jpg
</code>
</pre>


||Drawing(custom dataset)|-|-|
||-----------------------|-|-|
|![99](https://user-images.githubusercontent.com/61686244/132516012-19659e4e-dc43-4cb6-aae9-c7c43b803c45.png)|![592](https://user-images.githubusercontent.com/61686244/132516030-937404ee-09ca-46ad-8b47-f8ec2ef592eb.png)|

|VisDrone2019|
||




