import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
from PIL import Image, ImageFont, ImageDraw

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range ( 0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png"), ("All File", "*.*")))
    img = Image.open(fln)
    img.thumbnail((350,350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img



    img=cv2.imread(fln)
    img = cv2.resize(img, (500, 500), None, None, None)
    kernel = np.ones((5,5),np.uint8)
    print(kernel)
    image_Gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    image_XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)
    image_LAB = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    image_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    image_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    image_HLS = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    image_YUL = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)

    StackedImages = stackImages(0.6,([img,image_Gray,image_XYZ,image_LAB],[image_YUL,image_BGR,image_HLS,image_HSV]))
    cv2.imshow("Tipuri de spatiu de culoare", StackedImages)
    img = Image.open("",image_Gray)
    title_font = ImageFont.truetype('arial', 24)

    draw = ImageDraw.Draw(image_Gray)
    draw.text((0, 0),"Hello world",(255,255,255),font=font)
    image_Gray.save("result.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()

root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl= Label(root)
lbl.pack()

btn = Button(frm, text="Cauta imagine",command=showimage)
btn.pack(side=tk.LEFT)

btn = Button(frm, text="Exit",command=lambda: exit())
btn.pack(side=tk.LEFT, padx=10)



root.title("Imagine RGB")
root.geometry("300x500")
root.mainloop()
