
#Yassine SABIR

import cv2
import numpy as np
import math

def file2img(file_path):

    f=open(file_path,"r")

    content = f.read()

    if content == "":
        print("file is empty")
        return

    len_file = len(content)

    img_dim = math.ceil(len_file/3)
    img_width = math.ceil(math.sqrt(img_dim))

    img_height = img_width

    img=np.zeros((img_width,img_height,3),np.uint8)
    x,y=0,0

    for i in range(0,len_file,3):

        if y >= img_width:
            x+=1
            y=0

        if i == len_file-1:
            img[x][y]=(ord(content[i]),0,0)
        elif i == len_file-2:
            img[x][y]=(ord(content[i]),ord(content[i+1]),0)
        else:
            img[x][y]=(ord(content[i]),ord(content[i+1]),ord(content[i+2]))

        y+=1

    f.close()
    return img  #returns images that can be seen using cv2.imshow




def img2file(img,file_path): #this function turns an image into a file and store it in file_path
    #use this function to decrypt the result of the first function
    file=open(file_path,"w")

    n,m,_=img.shape

    content=""

    for i in range(n):
        for j in range(m):
            content+=(chr(img[i][j][0])+chr(img[i][j][1])+chr(img[i][j][2]))
    file.write(content)
    file.close()


