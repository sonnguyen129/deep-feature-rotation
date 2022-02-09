# Deep Feature Rotation for Multimodal Image Style Transfer

![Python 3.6](https://img.shields.io/badge/python-3.6.13-green.svg)
![Packagist](https://img.shields.io/badge/Tensorflow-2.7-red.svg)
![Last Commit](https://img.shields.io/github/last-commit/sonnguyen129/deep-feature-rotation)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-blue.svg)]((https://github.com/sonnguyen129/deep-feature-rotation/graphs/commit-activity))
![Contributing](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)

![image1](./doc/DFR-demo.gif)

--------------------------------

This repository contains the **official implementation** of paper: <br>
[***Deep Feature Rotation for Multimodal Image Style Transfer***](https://drive.google.com/file/d/10PlfQGgqGja60zWoXHrU-9obZCac0IEK/view?usp=sharing) <br>
[**Son Truong Nguyen**](https://sonnguyen129.github.io/), Nguyen Quang Tuyen, Nguyen Hong Phuc <br>
In [**NICS 2021**](http://nafosted-nics.org/) **Oral**.<br>

| [Paper (arXiv version)](https://drive.google.com/file/d/10PlfQGgqGja60zWoXHrU-9obZCac0IEK/view?usp=sharing) | [Paper (IEEE version)](https://ieeexplore.ieee.org/document/9701465) | [Presentation](https://docs.google.com/presentation/d/1QmEaNGX28uZUJ_Gy-NqIWW0nPcdlqrAA/edit?usp=sharing&ouid=103577362269285208414&rtpof=true&sd=true) | [Colab Demo](#demo) | [Bibtex](#citation) |
| :---:     |  :----: | :---: |  :---: | :---: |
    
## Table of Content

1. [Overview](#overview)
1. [Getting Started](#getting-started)
    - [Demo](#demo)
    - [Installation](#installation)
3. [Results](#results)
4. [Extensive results](#extensive-results)
5. [Citation](#citation)
6. [Contact](#contact)

## Overview
We propose a simple method for representing style features in many ways called ***Deep Feature Rotation (DFR)***, while still achieving effective stylization compared to more complex methods in style transfer. Our approach is a representative of the many ways of augmentation for intermediate feature embedding without consuming too much computational expense.

<br>

<p align="center">
  <img src="doc/model.png" alt="Model architecture" width="800">  
</p>

<p align="center">
    <sub><em>Model architecture.</em></sub>
</p>

## Getting started
### Demo
<p align="center">
    <a href="https://colab.research.google.com/drive/1nmf4_YnUBq5dGGTgWeN1fYNYOSOKeQ-1?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg"/>
    </a>
        <br>
    Try out in Google Colab
</p>

### Installation
* Clone this repository and check the ```requirements.txt```:
    ```shell
    git clone https://github.com/sonnguyen129/deep-feature-rotation
    cd deep-feature-rotation
    pip install -r requirements.txt
    ```
* Inference:
    * Prepare your content image and style image. I provide some in the ```data/content``` and ```data/style``` and you can try to use them easily.
    * Simply run: 
    
    ```shell
    python train.py --content-path <CONTENT_PATH> --style-path <STYLE_PATH>
    ```
    
    The test results will be saved to ```./results``` by default.

## Results

<p align="center">
  <img src="doc/rotation_weight.png">  
</p>

<p align="center">
    <sub><em>Experimental result in different rotation weight.</em></sub>
</p>

<br>

![image4](./doc/SOTA.png)

<p align="center">
    <sub><em>Comparison with other methods.</em></sub>
</p>

## Extensive results
We provide a visual comparison between other rotation angles that do not appear in the paper. The rotation angles will produce a very diverse number of outputs. This has proven the effectiveness of our method with other methods.

![image4](./doc/extensive-results.png)

<p align="center">
    <sub><em>Visual comparison in different rotation angles.</em></sub>
</p>

## Citation
If you find this work useful for your research, please cite:
```bibtex
@INPROCEEDINGS{9701465,  
    author={Nguyen, Son Truong and Tuyen, Nguyen Quang and Phuc, Nguyen Hong},  
    booktitle={2021 8th NAFOSTED Conference on Information and Computer Science (NICS)},   
    title={Deep Feature Rotation for Multimodal Image Style Transfer},   
    year={2021},  
    pages={260-265},  
    doi={10.1109/NICS54270.2021.9701465}
}
```
## Contact
If you have any questions/comments/bug reports, feel free to open a github issue or pull a request or mail to the author [Son Truong Nguyen](https://sonnguyen129.github.io/).

