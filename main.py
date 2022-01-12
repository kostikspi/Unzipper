import glob
from os.path import isdir
import zipfile


def unzip_all(directory):
    if isdir(directory):
        file_list = glob.glob(directory + '\\*')
        for file in file_list:
            if isdir(file):
                unzip_all(file)
            else:
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall('TextsRaw')

import sys
sys.setrecursionlimit(2500)
print(sys.getrecursionlimit())

filename_zip = 'zipped'
filename_raw = 'D:\\UnzipScript\\TextsRaw'
unzip_all(filename_zip)