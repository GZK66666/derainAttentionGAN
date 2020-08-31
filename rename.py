import os

REALDATADIR = "D:\\derain\\datasets\\raindrop\\testB"
path_real = os.path.join(REALDATADIR)
os.chdir(path_real)#切换工作路径,path为需要处理的数据所在的目录
files = os.listdir(path_real)
for f in files:
    x = os.path.splitext(f)
    # 判断jpg文件
    if x[1] == ".jpg":
        # 重命名
        print(f)
        name = x[0] + ".png"
        os.rename(f, name)