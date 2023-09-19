# AI-Driven Cervical Cancer Cytological Diagnosis Solution based on Large Scale Data Collections and Annotations: A Multi-centre Clinical Validation
A novel AI diagnostic system called CCA-DIAG was developed for cervical cancer screening based on a hybrid machine learning framework, which is capable of efficient WSI-level classification for cervical cancer screening.

![image](https://github.com/jydada/CCA-DIAG/blob/main/doc/fig1.png)

This repository is the official PyTorch implementation of CCA-DIAG, which can be used for fast deploying CCA-DIAG and processing WSI-level classification for various sedimentations. Considering the huge size of the data, personal information protection, patient privacy regulation, and medical institutional data regulatory policies, we prepare a subset of the data for verification and validation. 

## Links to the data and code

- [CCA-DIAG](https://drive.google.com/drive/folders/1a1LjZ779uyJx3gs7OJ4K1DCrwaoeACWy?usp=drive_link)

## Operating environment
- Ubuntu 16.04 server or higher
- GPU graphics memory of at least 7GB, recommended RTX 2080ti or higher graphics card

1. Set Up Environment

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

2. Running the Inference Code 

```bash
conda activate infer
cd TCT_infer
python TCT_Det.py -d "tif folder path"
or python TCT_Det.py -f "single tif file path"
```
## Contact information
If you have any questions, feel free to contact us. 

Bingxian CHEN, Ningbo KonFoong Bioinformation Tech Co. Ltd, Ningbo, Zhejiang, China. Email: bingxian.chen@kfbio.cn

Haoda Lu, Computational Digital Pathology Lab (CDPL), Bioinformatics Institute, A*STAR, Singapore. Email: lu_haoda@bii.a-star.edu.sg
