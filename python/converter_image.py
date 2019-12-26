import os
import argparse
import multiprocessing
import logging
import time
import glob
import pydicom
from pydicom.multival import MultiValue
import SimpleITK as sitk
import numpy as np
import cv2
import traceback
from vtk import *


parser = argparse.ArgumentParser(description='Convert dicom to jpg')
parser.add_argument('dcm_path', default=None, metavar='DCM_PATH',
                    type=str, help="Path to the input dcm files")
parser.add_argument('jpg_path', default=None, metavar='JPG_PATH',
                    type=str, help="Path to the output jpg files")
parser.add_argument('--num_workers', default=1, type=int, help='num_workers')
parser.add_argument('--window', default=5160, type=int, help='Lower'
                    ' bound of the pixel percentile')
parser.add_argument('--level', default=2513, type=int, help='Upper'
                    ' bound of the pixel percentile')


def dcm2jpg(dcm_file, jpg_file, window=1, level=99):
    logging.info('{}, Converting {}...'.format(
        time.strftime("%Y-%m-%d %H:%M:%S"), dcm_file))
   
    dcm = pydicom.dcmread(dcm_file, force=True)
    if hasattr(dcm, 'WindowWidth'):
        window = dcm.WindowWidth
        if type(window) is MultiValue: 
            window = window[0]
    else:
        window = (np.max(dcm.pixel_array) - np.min(dcm.pixel_array)) / 2
    
    if hasattr(dcm, 'WindowCenter'):
        level = dcm.WindowCenter
        if type(level) is MultiValue: 
            level = level[0]
    else:
        level = (np.max(dcm.pixel_array) + np.min(dcm.pixel_array)) / 2
    if hasattr(dcm, 'PhotometricInterpretation'):
        if dcm.PhotometricInterpretation == 'MONOCHROME1':
            dcm_temp = './temp.dcm'
            value = 2**(dcm.BitsStored - 1)
            if level > value or window > value:
                value = 2 * value
            pixel_array = (value - dcm.pixel_array).astype(np.uint16)
            dcm.PixelData = pixel_array.tobytes()
            dcm.PhotometricInterpretation = 'MONOCHROME2'
            dcm.save_as(dcm_temp)
            level = value - level
            dcm_file = dcm_temp

    if hasattr(dcm, 'IconImageSequence'):
        dcm_temp = './temp.dcm'
        dcm.IconImageSequence=''
        dcm.save_as(dcm_temp)
        dcm_file = dcm_temp

    reader = vtkDICOMImageReader()
    reader.SetFileName(dcm_file)
    reader.Update()
    image = reader.GetOutput()

    windowlevel = vtkImageMapToWindowLevelColors()
    windowlevel.SetInputData(reader.GetOutput())

    windowlevel.SetWindow(window)
    windowlevel.SetLevel(level)
    windowlevel.Update()

    shiftScaleFilter = vtkImageShiftScale()
    shiftScaleFilter.SetOutputScalarTypeToUnsignedChar()
    shiftScaleFilter.SetInputConnection(windowlevel.GetOutputPort())

    shiftScaleFilter.SetShift(-1.0*windowlevel.GetOutput().GetScalarRange()[0])
    oldRange = windowlevel.GetOutput().GetScalarRange()[1] - windowlevel.GetOutput().GetScalarRange()[0]
    newRange = 255

    shiftScaleFilter.SetScale(newRange/oldRange)
    shiftScaleFilter.Update()

    writer = vtkPNGWriter()
    writer.SetFileName(jpg_file)
    writer.SetInputConnection(windowlevel.GetOutputPort())
    writer.Write()

def dcm_alloc(opts):
    dcm_file, args = opts
    file_name = os.path.basename(dcm_file)[:-4]
    jpg_file = os.path.join(args.jpg_path, file_name + '.jpg')
    try:
        dcm2jpg(dcm_file, jpg_file,
                window=args.window,
                level=args.level)
    except Exception:
        traceback.print_exc()


def run(args):
    CPU_NUM = multiprocessing.cpu_count()
    assert args.num_workers <= CPU_NUM,\
        'num_workers:{} exceeds cpu_count:{}'.format(args.num_workers,
                                                     CPU_NUM)
    if not os.path.exists(args.jpg_path):
        os.mkdir(args.jpg_path)
    dcm_files = glob.glob(os.path.join(args.dcm_path, '*.dcm'))
    exist_jpg = glob.glob(os.path.join(args.jpg_path, '*.jpg'))
    filenames_exists = set(map(lambda x: x.split('/')[-1], exist_jpg))
    dcm_files_ = []
    for dcm_file in dcm_files:
        if dcm_file.split('/')[-1].replace('.dcm', '.jpg') not in \
           filenames_exists:
            dcm_files_.append(dcm_file)
    opts = [(dcm_file, args) for dcm_file in dcm_files_]
    pool = multiprocessing.Pool(processes=args.num_workers)
    pool.map(dcm_alloc, opts)


def main():
    logging.basicConfig(level=logging.INFO)
    args = parser.parse_args()
    run(args)


if __name__ == '__main__':
    main()
