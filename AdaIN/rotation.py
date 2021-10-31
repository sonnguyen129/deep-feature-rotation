import torch 
import torchvision.transforms.functional as TF

# class MyRotationTransform:
#     """Rotate by one of the given angles."""

#     def __init__(self, angles):
#         self.angles = angles

#     def __call__(self, x):
#         return TF.rotate(x, self.angles, expand = False)