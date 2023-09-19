
A novel AI diagnostic system called CCA-DIAG was developed for cervical cancer screening based on a hybrid machine learning framework, which is capable of efficient WSI-level classification for various sedimentations.

Operating environment: 
Ubuntu 16.04 server or higher, 
GPU graphics memory of at least 7GB, recommended 2080ti or higher graphics card.

1. Download
```bash
Download the code at "https://drive.google.com/drive/folders/1a1LjZ779uyJx3gs7OJ4K1DCrwaoeACWy?usp=drive_link"
```
2. Install

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

3. How to run

```bash
conda activate infer
cd TCT_infer
python TCT_Det.py -d "tif folder path"
or python TCT_Det.py -f "single tif file path"
```
