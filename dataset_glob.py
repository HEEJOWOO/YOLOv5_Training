from glob import glob
 
# dataset_root : 경로 설정 필요
train_img_list = glob('dataset_root/train/images/*.jpg')
valid_img_list = glob('dataset_root/valid/images/*.jpg')
 
with open('dataset_root/train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open('dataset_root/valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')
