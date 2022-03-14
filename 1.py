import os
import shutil

DirSs = "D:\\labelImg-master\\0105\\";
NewDirs = "D:\\labelImg-master\\0106";


def file_name(file_dir):
    for o in range(10):
        for root, dirs, files in os.walk(file_dir):
            print(files)  # 当前路径下所有非目录子文件
        for i in files:
            DldDir = str(DirSs) + str(i)
            shutil.copy(DldDir, NewDirs)
            os.rename(str(NewDirs) + "\\" + str(i), str(NewDirs) + "\\"+str(o) + str(i))


if __name__ == '__main__':
    file_name(DirSs)
