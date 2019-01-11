import os
train_file=open('/home/ubtu/VOC_GJ/ImageSets/Main/train.txt','w')#修改自己的路径并创建train.txt
test_file=open('/home/ubtu/VOC_GJ/ImageSets/Main/test.txt','w')#修改自己的路径并创建test.txt
for _,_,train_files in os.walk('/home/ubtu/VOC_GJ/train_dataset'):
    continue
for _,_,test_files in os.walk('/home/ubtu/VOC_GJ/test_dataset'):
    continue
for file in train_files:
    train_file.write(file.split('.')[0]+'\n')
 
for file in test_files:
    test_file.write(file.split('.')[0]+'\n')
