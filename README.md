# Deep Feature Rotation for Multimodal Image Style Transfer

This repository contains the **official implementation** of paper:

***Deep Feature Rotation for Multimodal Image Style Transfer***

[**Son Truong Nguyen**](https://github.com/sonnguyen129), Nguyen Quang Tuyen, Nguyen Hong Phuc

In Proceedings of NICS 2021.

## Table of Content

1. [Overview](#overview)
1. [Getting Started](#getting-started)
    - [Dependency](#dependency)
    - [Installation](#installation)
3. [Results](#results)
4. [Contact](#contact)

## Overview
We propose a simple method for representing style features in many ways called ***Deep Feature Rotation***, while still achieving effective stylization compared to more complex methods in style transfer. Our approach is a representative of the many ways of augmentation for intermediate feature embedding without consuming too much computational expense.

![image2](./doc/model.png)

## Getting started
### Dependency
- Tensorflow 2.x
- Check the requirements.txt

```
pip install -r requirements.txt
```

### Installation
* Clone this repository:
    ```
    git clone https://github.com/sonnguyen129/style-transfer-rotation
    cd style-transfer-rotation
    ```
* Inference:
    * Prepare your content image and style image. I provide some in the ```data/content``` and ```data/style``` and you can try to use them easily.
    * Simply run: 
    
    ```
    cd style-transfer
    python train.py --content-path <CONTENT_PATH> --style-path <STYLE_PATH>
    ```
    
    The test results will be saved to ```./results``` by default.
    
 * <p align="center">
    <a href="https://colab.research.google.com/drive/1nmf4_YnUBq5dGGTgWeN1fYNYOSOKeQ-1?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg"/>
    </a>
        <br>
    Try out in Google Colab
  </p>

## Results
*Experimental result in different rotation weight*

![image3](./doc/rotation_weight.png)
--------------
*Comparison with other methods*

![image4](./doc/SOTA.png)

## Contact
Feel free to open new issue or contact me if there is any question (Son Truong Nguyen ```sonhai12092000@gmail.com```).

