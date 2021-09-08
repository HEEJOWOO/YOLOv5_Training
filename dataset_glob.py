from glob import glob
 
#/datasetroot : 경로 설정 필요
train_img_list = glob('/datasetroot/train/images/*.jpg')
valid_img_list = glob('/datasetroot/valid/images/*.jpg')
 
with open('/dataset_root/train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open('/dataset_root/valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')
