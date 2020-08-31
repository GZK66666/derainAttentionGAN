    # encoding: utf-8
# import tensorflow as tf
# import matplotlib.pyplot as plt
# import cv2
# import os

# image = cv2.imread('54_7.jpg')
# img_new = cv2.resize(image, (256,256), interpolation = cv2.INTER_CUBIC)
# cv2.imwrite('54_7_resize.jpg' , img_new)

import os
import cv2

''' 设置图片路径，该路径下包含了14张jpg格式的照片，名字依次为0.jpg, 1.jpg, 2.jpg,...,14.jpg'''
DATADIR="D:\\derain\\datasets\\rain_heavy_and_light\\trainB"
'''设置目标像素大小，此处设为300'''
IMG_SIZE=256
'''使用os.path模块的join方法生成路径'''
path=os.path.join(DATADIR)
'''使用os.listdir(path)函数，返回path路径下所有文件的名字，以及文件夹的名字，
例如，执行下行代码后，img_list是一个list，值为['0.jpg','1.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg',
'2.jpg','3.jpg','4.jg', '5.jpg', '6.jpg', '7.jpg', 
'8.jpg', '9.jpg']，注意这个顺序并没有按照从小到大的顺序排列'''
img_list=os.listdir(path)
for j in range(100, 123):
    for i in img_list:
        index = 'norain-{0}.png'.format(j)
        if(i == index):
            print(i)
            '''调用cv2.imread读入图片，读入格式为IMREAD_COLOR'''
            img_array=cv2.imread(os.path.join(path,i),cv2.IMREAD_COLOR)
            '''调用cv2.resize函数resize图片'''
            new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
            img_name=i
            '''生成图片存储的目标路径'''
            save_path='D:\\derain\\contrast\\after7.1\\multiscale interfeat recperceptualloss_heavyandlightdataset\\multiscale+interfeat+recperceptualloss_heavyandlightdataset\\test_latest\\'+img_name
            '''调用cv.2的imwrite函数保存图片'''
            cv2.imwrite(save_path,new_array)
