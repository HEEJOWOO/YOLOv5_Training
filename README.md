# YOLOv5_Training
  * Pytroch, RTX 3090 24G, Ubuntu 18.04 LTS
  * [YOLOv5](github.com/ultralytics/yolov5) 파일 이용

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
  * 5) data.yaml 파일의 데이터 셋 경로 변경
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


|Drawing(custom dataset)|Bus & People|Car|
|-------|---|---|
|![592](https://user-images.githubusercontent.com/61686244/132509503-cb0be8f5-f149-4654-ad01-990469c95df1.png)|![bus](https://user-images.githubusercontent.com/61686244/132508744-9ccaf69a-4e50-406d-9a3c-c85009780c53.jpg)|![0000353_05500_d_0000199](https://user-images.githubusercontent.com/61686244/132508757-900d6942-ad0c-4002-8a4f-4aaa02196153.jpg)|




