1.Install

```bash
conda create -n infer python=3.8
conda activate infer
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.2 -c pytorch
pip install cupy-cuda102==8.5.0
pip install mmcv-full==1.4.0 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.7.0/index.html
cd TCT_infer/modules/mmdetection
pip install cython==0.29.33
pip install -r requirements.txt
python setup.py develop
cd TCT_infer
sudo apt install python-openslide
pip install -r requirements.txt
```

2.How to run

```bash
conda activate infer
cd TCT_infer
python TCT_Det.py -d "tif folder path"
or python TCT_Det.py -f "single tif file path"
```

3.运行环境

Ubuntu16.04server或更高版本

GPU显存至少7G，推荐2080ti或更高的显卡
