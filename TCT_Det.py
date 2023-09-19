# -*- encoding: utf-8 -*-
'''
@File    :   TCT_Det.py
@License :   (C)Copyright 2019-2025, KFBIO

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
9/19/2020 3:43 PM   KFBIO      1.0         None
'''
import sys, os, os.path as osp
try:
    os.chdir(osp.dirname(osp.abspath(__file__)))
except:
    os.chdir(osp.abspath(os.getcwd()))
sys.path.insert(0, osp.abspath('./lib'))

import os
import multiprocessing
from optparse import OptionParser
from tqdm import tqdm
from modules.RunDet import RunDet

def main():
    usage = "#############TCT识别程序###########"
    parser = OptionParser(usage)
    parser.add_option('-f', '--kfb', dest='file', default=None,
                      help="单个kfb文件路径")
    parser.add_option('-d', '--kfbs', dest='dir_path',
                      default=None,
                      help="多个kfb文件的根路径")
    parser.add_option('-s', '--start', dest='start_num',
                      default=0,
                      help="多个kfb文件的根路径")
    parser.add_option('-t', '--slice_type', dest='slice_type',
                      default='auto',
                      help="制片方式")
    (options, args) = parser.parse_args()
    rundet = RunDet()

    # 搜索生成kfb文件列表
    kfb_file_list = []
    if options.file is not None:
        kfb_file_list.append(options.file)
    if options.dir_path is not None:
        for kfb_dir, _, kfb_name in os.walk(options.dir_path):
            for file in kfb_name:
                if rundet.if_fusion == 0:
                    if file[-3:] in ['kfb', 'tif']:
                        kfb_file_list.append(os.path.join(kfb_dir, file))
                elif rundet.if_fusion == 1:
                    if file.find('.fusion.kfb') != -1:
                        kfb_file_list.append(os.path.join(kfb_dir, file))
    pbar = tqdm(kfb_file_list[int(options.start_num):])
    for i, file_path in enumerate(pbar):
        image_type = os.path.splitext(file_path)[1]
        rundet.run(file_path, image_type, options.slice_type)
    rundet.kill_precess()


if __name__ == '__main__':
    if sys.platform == 'linux':
        multiprocessing.set_start_method('spawn')
    else:
        multiprocessing.freeze_support()
    main()

