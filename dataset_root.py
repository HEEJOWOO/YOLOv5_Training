import yaml

#/datsetroot : 경로 설정 필요
with open('/datasetroot/data.yaml', 'r') as f:
	data = yaml.load(f)

data['train'] = '/datasetroot/dataset/train.txt'
data['valid'] = './dataset/valid.txt'
 
with open('/datasetroot/data.yaml', 'w') as f:
	yaml.dump(data, f)
