import numpy
import numpy as np
import math
import cv2
import torch
import pytorch_ssim
from torch.autograd import Variable
import os


def psnr(img1, img2):
    mse = numpy.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def ssim(img1, img2):
    img1 = torch.from_numpy(np.rollaxis(img1, 2)).float().unsqueeze(0) / 255.0
    img2 = torch.from_numpy(np.rollaxis(img2, 2)).float().unsqueeze(0) / 255.0
    img1 = Variable(img1, requires_grad=False)  # torch.Size([256, 256, 3])
    img2 = Variable(img2, requires_grad=False)
    ssim_value = pytorch_ssim.ssim(img1, img2).item()
    return ssim_value


# #Rain100L
# DATADIR = "D:\\derain\\contrast\\after7.1\\multiscale+interfeat+recperceptual_Rain100L\\test_latest\\images"
# REALDATADIR = "D:\\derain\\datasets\\JORDER_dataset\\Rain100L\\testB"
# path=os.path.join(DATADIR)
# path_real = os.path.join(REALDATADIR)
# img_list=os.listdir(path) + os.listdir(path_real)
#
# count = 0
# psnr_sum = 0
# ssim_sum = 0
#
# for j in range(1, 201):
#     real_name = 'norain-{0}.png'.format(j)
#     fake_name = 'norain-{0}x2_fake_B.png'.format(j)
#     real = None
#     fake = None
#     for i in img_list:
#         if (i == real_name):
#             real = cv2.imread(os.path.join(path_real, i))
#             real = cv2.resize(real, (256, 256))
#         elif (i == fake_name):
#             fake = cv2.imread(os.path.join(path, i))
#     count += 1
#     psnr_sum += psnr(real, fake)
#     ssim_sum += ssim(real, fake)
#
# print("Rain100L")
# print(psnr_sum / count)
# print(ssim_sum / count)
#
#
# #Rain800
# DATADIR = "D:\\derain\\contrast\\after7.1\\multiscale+interfeat+recperceptual_Rain800\\test_latest\\images"
# REALDATADIR = "D:\\derain\\datasets\\rain800\\testB"
# path=os.path.join(DATADIR)
# path_real = os.path.join(REALDATADIR)
# img_list=os.listdir(path) + os.listdir(path_real)
#
# count = 0
# psnr_sum = 0
# ssim_sum = 0
#
# for j in range(1, 101):
#     real_name = '{0}.jpg'.format(j)
#     fake_name = '{0}_fake_B.png'.format(j)
#     real = None
#     fake = None
#     for i in img_list:
#         if (i == real_name):
#             real = cv2.imread(os.path.join(path_real, i))
#             real = cv2.resize(real, (256, 256))
#         elif (i == fake_name):
#             fake = cv2.imread(os.path.join(path, i))
#     # cv2.imshow("real", real)
#     # cv2.imshow("fake", fake)
#     # cv2.waitKey()
#     # print(psnr(real, fake))
#     # print(ssim(real, fake))
#     count += 1
#     psnr_sum += psnr(real, fake)
#     ssim_sum += ssim(real, fake)
#
# print("Rain800")
# print(psnr_sum / count)
# print(ssim_sum / count)
#
# #Rain100H
# DATADIR = "D:\\derain\\contrast\\after7.1\\multiscale+interfeat+recperceptual_Rain100H\\test_latest\\images"
# REALDATADIR = "D:\\derain\\datasets\\JORDER_dataset\\Rain100H\\testB"
# path=os.path.join(DATADIR)
# path_real = os.path.join(REALDATADIR)
# img_list=os.listdir(path) + os.listdir(path_real)
#
# count = 0
# psnr_sum = 0
# ssim_sum = 0
#
# for j in range(1, 201):
#     real_name = 'norain-{0}.png'.format(j)
#     fake_name = 'norain-{0}x2_fake_B.png'.format(j)
#     real = None
#     fake = None
#     for i in img_list:
#         if (i == real_name):
#             real = cv2.imread(os.path.join(path_real, i))
#             real = cv2.resize(real, (256, 256))
#         elif (i == fake_name):
#             fake = cv2.imread(os.path.join(path, i))
#     count += 1
#     psnr_sum += psnr(real, fake)
#     ssim_sum += ssim(real, fake)
#
# print("Rain100H")
# print(psnr_sum / count)
# print(ssim_sum / count)

#Raindrop
DATADIR = "D:\\derain\\contrast\\after7.1\\multiscale+interfeat+recperceptual_raindrop\\test_latest\\images"
REALDATADIR = "D:\\derain\\datasets\\raindrop\\testB"
path=os.path.join(DATADIR)
path_real = os.path.join(REALDATADIR)
img_list=os.listdir(path) + os.listdir(path_real)

count = 0
psnr_sum = 0
ssim_sum = 0

for j in range(0, 249):
    real_name = '{0}_clean.png'.format(j)
    fake_name = '{0}_rain_fake_B.png'.format(j)
    real = None
    fake = None
    for i in img_list:
        if (i == real_name):
            real = cv2.imread(os.path.join(path_real, i))
            real = cv2.resize(real, (256, 256))
        elif (i == fake_name):
            fake = cv2.imread(os.path.join(path, i))
    # print(real_name)
    # print(fake_name)
    # cv2.imshow("real", real)
    # cv2.imshow("fake", fake)
    # cv2.waitKey(0)
    # print(psnr(real, fake))
    # print(ssim(real, fake))
    count += 1
    psnr_sum += psnr(real, fake)
    ssim_sum += ssim(real, fake)

print("Raindrop")
print(psnr_sum / count)
print(ssim_sum / count)