import os

from pycocotools.coco import COCO
from skimage import io
from matplotlib import pyplot as plt

json_file = '/nas/user/yaojin/temp/yunce/biaozhu.json'
dataset_dir = '/nas/user/yaojin/temp/yunce/imgs/'
coco = COCO(json_file)
catIds = coco.getCatIds(catNms=['person']) # catIds=1 表示人这一类
imgIds = coco.getImgIds(catIds=catIds ) # 图片id，许多值

print(len(imgIds))

for i in range(len(imgIds)):
    img = coco.loadImgs(imgIds[i])[0]
    I = io.imread(dataset_dir + img['file_name'])
    plt.axis('off')
    plt.imshow(I) #绘制图像，显示交给plt.show()处理
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
    anns = coco.loadAnns(annIds)
    coco.showAnns(anns, True)
    plt.show() #显示图像
