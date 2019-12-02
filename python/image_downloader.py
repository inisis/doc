# -*- coding: utf-8 -*-
import sys
import multiprocessing
from easydict import EasyDict as edict
import os
import glob
import json

from urllib.request import urlretrieve
import time
import traceback
import socket
socket.setdefaulttimeout(5)

start = time.time()


def get_urls():
    """
    Returns a list of urls by reading the txt file supplied as argument in terminal
    """
    try:
        json_path = sys.argv[1]
        dcm_path = sys.argv[2]
    except IndexError:
        print('ERROR: Please run like this\n\n$python image_downloader.py json_path dcm_path num_process \n\n')
        sys.exit()
    
    if not os.path.exists(dcm_path):
        os.mkdir(dcm_path)

    filenames_exists = glob.glob(os.path.join(dcm_path, '*.dcm'))
    filenames_exists = set(map(lambda x: x.split('/')[-1], filenames_exists))

    json_files = glob.glob(os.path.join(json_path, '*.json'))
    images_url = []
    for json_file in json_files:
        filename =  os.path.basename(json_file)[:-5] + ".dcm"
        if filename in filenames_exists:
            continue
        images_url.append(json_file)

    print('{} Images detected'.format(len(images_url)))
    return images_url


def image_downloader(img_url: str):
    """
    Input:
    param: img_url  str (Image url)
    Tries to download the image url and use name provided in headers. Else it randomly picks a name
    """
    print(f'Downloading: {img_url}')
    with open(img_url) as f:
        json_dict = edict(json.load(f))
        wado_dict = json_dict.wado
        studyUid = '&studyUID=' + wado_dict.studyUid
        seriesUid = '&seriesUID=' + wado_dict.seriesUid
        imageUid = '&objectUID=' + wado_dict.imageUid
        filename = wado_dict.imageUid + '.dcm'
        url = wado_dict.wadoUrl + studyUid + seriesUid + imageUid
    try:
        urlretrieve(url, os.path.join(sys.argv[2], filename))
    except Exception:
        traceback.print_exc()
        pass

    # return f'Download complete: {img_url}'


def run_downloader(process: int, images_url: list):
    """
    Inputs:
        process: (int) number of process to run
        images_url:(list) list of images url
    """
    print(f'MESSAGE: Running {process} process')
    # results = ThreadPool(process).imap_unordered(image_downloader, images_url)
    pool = multiprocessing.Pool(process)
    pool.map(image_downloader, images_url)


try:
    num_process = int(sys.argv[3])
except:
    num_process = 10

images_url = get_urls()
run_downloader(num_process, images_url)


end = time.time()
print('Time taken to download {}'.format(len(get_urls())))
print(end - start)
