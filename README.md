# Deep Feature Rotation for Multimodal Image Style Transfer
Run [this notebook](https://github.com/sonnguyen129/style-transfer-rotation/blob/main/Style_transfer_rotation.ipynb) or [Colab](https://colab.research.google.com/drive/1nmf4_YnUBq5dGGTgWeN1fYNYOSOKeQ-1?usp=sharing) to see results
## Overview
We propose a simple method for representing style features in many ways called Deep Feature Rotation, while still achieving effective stylization compared to more complex methods in style transfer. Our approach is a representative of the many ways of augmentation for intermediate feature embedding without consuming too much computational expense.

![image1](./doc/rotate_mechanism.png)

Our method differs from [Gatys' method](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf) in that we can generate multiple outputs, and is a simple approach compared to many other methods. After encoding the content and style image, we will get a set of feature maps. We can rotate to many different angles

![image2](./doc/model.png)

## Result
Experimental Result in different rotation weight

![image3](./doc/rotation_weight.png)

Comparison with other methods

![image4](./doc/SOTA.png)

## References
- [Huage001's AdaAttn Implementation](https://github.com/Huage001/AdaAttN)
- [irasin's AdaIN Implementation](https://github.com/irasin/Pytorch_AdaIN)
- [sunshineatnoon's LST Implementation](https://github.com/sunshineatnoon/LinearStyleTransfer)
- [Aaditya Singh's SAFIN Implementation](https://github.com/Aaditya-Singh/SAFIN)
