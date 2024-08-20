
# 1 Environment Setup
```
git clone https://github.com/ultralytics/yolov3.git 
```

In your corresponding conda environment, cd to the yolov3 folder, and install the required packages
```
pip3 install -U -r requirements.txt
```
- conda install numpy opencv matplotlib tqdm pillow && conda install pytorch torchvision -c pytorch
- numpy
- opencv-python
- torch >= 2.0.0
- matplotlib
- pycocotools
- tqdm

# 2 Dataset Construction
## Construction of VOC Format Data

```py
import os
import random

trainval_percent = 0.8
train_percent = 0.8
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
```
In the Main folder, there are 4 txt files. Clicking on train.txt corresponds to the images required for the training set after the division.

```py
"""
1. Replace "sets" with your own dataset.
2. Replace "classes" with your own categories.
3. Run this script outside the VOCdevkit2007 folder (the generated 5 txt files are also outside the VOCdevkit2007 folder, which is not important; the important thing is to obtain the txt files).
4. Start running directly.
"""

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["car", "person"]


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    in_file = open('VOCdevkit2007/VOC%s/Annotations/%s.xml'%(year, image_id))
    out_file = open('VOCdevkit2007/VOC%s/labels/%s.txt'%(year, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for year, image_set in sets:
    if not os.path.exists('VOCdevkit2007/VOC%s/labels/'%(year)):
        os.makedirs('VOCdevkit2007/VOC%s/labels/'%(year))
    image_ids = open('VOCdevkit2007/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit2007/VOC%s/JPEGImages/%s.jpg\n'%(wd, year, image_id))
        convert_annotation(year, image_id)
    list_file.close()

os.system("cat 2007_train.txt 2007_val.txt  > train.txt")
os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt  > train.all.txt")
```

# 3. Detection
Place the images to be detected in the "samples" folder under the "data" directory and run:

```
python3 detect.py --weights weights/latest.pt
```

Final results:

![](https://img-blog.csdnimg.cn/2019052814200963.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTY1OTIw,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20190528141816335.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTY1OTIw,size_16,color_FFFFFF,t_70)

