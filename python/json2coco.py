# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import json
import argparse
from easydict import EasyDict as edict

parser = argparse.ArgumentParser(description='Train model')
parser.add_argument('json_file', default=None, metavar='JSON_FILE', type=str,
                    help="Path to the json txt")
parser.add_argument('save_json', default=None, metavar='SAVE_JSON', type=str,
                    help="Path to the saved json")


def add_image(coco, cfg, filename, image_id):
    image_item = dict()
    file_name = os.path.basename(filename)[:-5]
    image_item['file_name'] = file_name + ".jpg"
    image_item['height'] = cfg.imageShape.get('height')
    image_item['width'] = cfg.imageShape.get('width')
    image_item['id'] = image_id
    coco['images'].append(image_item)
  

def add_category(coco, name, category_id):
    category_item = dict()
    category_item['supercategory'] = 'none'
    category_item['id'] = category_id
    category_item['name'] = name
    category_item['keypoints'] = [
                "seventh_cervical_vertebra",
                "right_costophrenic_angle",
                "left_costophrenic_angle"]
    category_item['skeleton'] = [[2, 3], [1, 2], [1, 3]]
    coco['categories'].append(category_item)


def add_anno(coco, cfg, value, box, image_id, category_id, annotation_id):
    annotation_item = dict()
    annotation_item['num_keypoints'] = 3
    annotation_item['keypoints'] = value
    annotation_item['image_id'] = image_id
    annotation_item['bbox'] = box
    annotation_item['area'] = get_area(box)
    annotation_item['iscrowd'] =  0
    annotation_item['category_id'] = category_id
    annotation_item['id'] = annotation_id
    coco['annotations'].append(annotation_item)


def get_points(key_point):
    x = key_point.get('points').get('X')
    y = key_point.get('points').get('Y')
    return float(x), float(y)


def get_value(cfg):
    value = [0] * 9 # x, y ,v v=0 point missing v=1 point invisible v=2 point visible
    keep_index = []
    for key_point in cfg.keyPoints:
        if key_point.get('objectLabels')[0] == 'seventh_cervical_vertebra':
            x, y = get_points(key_point)
            value[0:3] = x,y,2
            keep_index.append(0)
        if key_point.get('objectLabels')[0] == 'right_costophrenic_angle':
            x, y = get_points(key_point)
            value[3:6] = x,y,2
            keep_index.append(1)
        if key_point.get('objectLabels')[0] == 'left_costophrenic_angle':
            x, y = get_points(key_point)
            value[6:9] = x,y,2
            keep_index.append(2)
    
    if value[3] > value[6] and (2 in keep_index): # swap left and right(left should > right)
        value[3:6], value[6:9] = value[6:9], value[3:6]
        assert value[3] <= value[6]

    return value, keep_index


def get_box(value, keep_index, cfg):
    # x, y(left top) && width height
    assert(len(value) == 9)
    value_refined = get_refined(value, keep_index, cfg)

    assert value_refined[3] <= value_refined[6]

    box = [0] * 4
    box[0] = min(value_refined[::3])
    box[1] = min(value_refined[1::3])
    box[2] = max(value_refined[::3]) - box[0]
    box[3] = max(value[1::3]) - box[1]
    return box


def get_refined(value, keep_index, cfg):
    if len(keep_index) == 3:
        return value
    elif keep_index == [1,2] or keep_index == [2,1]: # missing top
        value_new = value.copy()
        value_new[0] = value[3] # change x
        return value_new
    elif keep_index == [0,1] or keep_index == [1,0]: # missing right
        value_new = value.copy()
        value_new[6] = cfg.imageShape.get('width') # change x
        value_new[7] = value[1] # change y
        return value_new
    elif keep_index == [0,2] or keep_index == [2,0]: # mising left
        value_new = value.copy()
        value_new[4] = value[1] # change y
        return value_new
    elif keep_index == [0]: # mising left and right
        value_new = value.copy()
        value_new[4] = cfg.imageShape.get('height') # change y
        value_new[6] = cfg.imageShape.get('width') # change x
        value_new[7] = cfg.imageShape.get('height') # change y
        return value_new
    elif keep_index == [1]: # mising top and left
        value_new = value.copy()
        value_new[0] = value[3] # change x
        value_new[6] = cfg.imageShape.get('width') # change x
        return value_new
    elif keep_index == [2]: # mising right and top
        return value
    else:
        raise Exception("Unexpected index: {}".format(*keep_index))


def get_area(box):
    assert(len(box) == 4)
    return (box[3] - box[1]) * (box[2] - box[0])


def run(args):
    coco = dict()
    coco['info'] = {
        "description": "COCO 2017 Dataset",
        "url": "http://cocodataset.org",
        "version": "1.0",
        "year": 2017,
        "contributor": "COCO Consortium",
        "date_created": "2017/09/01"
    }
    coco['licenses'] = [
        {
            "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
            "id": 1,
            "name": "Attribution-NonCommercial-ShareAlike License"
        }
    ]
    coco['images'] = []
    coco['categories'] = []
    coco['annotations'] = []

    category_id = 0
    image_id = 0
    annotation_id = 0
    add_category(coco, 'chest', category_id)
    
    with open(args.json_file) as json_file:
        for filename in json_file:
            filename = filename.strip('\n')
            print("Converting -----> ", filename)
            with open(filename) as f:
                cfg = edict(json.load(f))
                value, keep_index = get_value(cfg)
                if len(keep_index) == 0:
                    continue
                box = get_box(value, keep_index, cfg)
                add_image(coco, cfg, filename, image_id)
                add_anno(coco, cfg, value, box, image_id, category_id, annotation_id)
                image_id += 1
                annotation_id += 1

    with open(args.save_json, 'w') as f:
        json.dump(coco, f, indent=1)


def main():
    args = parser.parse_args()

    run(args)


if __name__ == '__main__':
    main()
