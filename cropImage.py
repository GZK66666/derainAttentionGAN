"""
split zed camera image to left image and right image.
eg: img[0:h, 0:w, : ] --> leftimg[0:h, 0:int(w/2), : ] and rightimg[0:h, int(w/2+1):w, : ].
"""

import cv2
import os

if __name__ == "__main__":
    path = "D:\\derain\\datasets\\DID-MDN-datasets_2_Rain1200\\DID-MDN-training\\Rain_Medium\\train2018new"  # change this dirpath.

    listdir = os.listdir(path)


    # newdir = os.path.join(path, 'split')  # make a new dir in dirpath.
    # if (os.path.exists(newdir) == False):
    #     os.mkdir(newdir)

    for i in listdir:
        if i.split('.')[1] == "jpg":  # the format of zed img.
            filepath = os.path.join(path, i)
            filename = i
            # leftpath = os.path.join(newdir, filename) + "_left.png"
            # rightpath = os.path.join(newdir, filename) + "_right.png"

            img = cv2.imread(filepath)
            [h, w] = img.shape[:2]
            limg = img[:, :int(w / 2), :]
            rimg = img[:, int(w / 2 + 1):, :]

            save_pathA = "D:\\derain\\datasets\\DID-MDN-datasets_2_Rain1200\\DID-MDN-training\\Rain_Medium\\trainA\\" + i
            save_pathB = "D:\\derain\\datasets\\DID-MDN-datasets_2_Rain1200\\DID-MDN-training\\Rain_Medium\\trainB\\" + i

            cv2.imwrite(save_pathA, limg)
            cv2.imwrite(save_pathB, rimg)

# img = cv2.imread("datasets/1.jpg")
# [h, w] = img.shape[:2]
# # print(filepath, (h, w))
# limg = img[:, :int(w / 2), :]
# rimg = img[:, int(w / 2 + 1):, :]
# cv2.imshow("left", limg)
# cv2.imshow("right", rimg)
# cv2.waitKey(0)
