from pycocotools.coco import COCO

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


coco = COCO('/temp/coco.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

cat = "person" # set person so all categories can be found
catIds = coco.getCatIds(catNms=[cat])
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)
print("imgIds: ", len(imgIds))
print("images: ", len(images))

# Create a subfolder in this directory called "labels". This is where the annotations will be saved in YOLO format
for im in images:
    dw = 1. / im['width']
    dh = 1. / im['height']
    
    annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
    anns = coco.loadAnns(annIds)
    
    filename = im['file_name'].replace(".jpg", ".txt")
    print(filename)

    with open("labels/" + filename, "a") as json_file:
        for i in range(len(anns)):
            xmin = anns[i]["bbox"][0]
            ymin = anns[i]["bbox"][1]
            xmax = anns[i]["bbox"][2] + anns[i]["bbox"][0]
            ymax = anns[i]["bbox"][3] + anns[i]["bbox"][1]
            
            x, y = (xmin + xmax)/2, (ymin + ymax)/2
            
            w, h = (xmax - xmin), (ymax-ymin)
            
            x, w, y, h = x * dw, w * dw, y * dh, h * dh
            # one class
            anno = "0 " + str(truncate(x, 7)) + " " + str(truncate(y, 7)) + " " + str(truncate(w, 7)) + " " + str(truncate(h, 7))
            json_file.write(anno)
            json_file.write("\n")
