import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png"), ("All File", "*.*")))
    img = Image.open(fln)
    img.thumbnail((350,350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl= Label(root)
lbl.pack()

btn = Button(frm, text="browser image",command=showimage)
btn.pack(side=tk.LEFT)

btn = Button(frm, text="Exit",command=lambda: exit())
btn.pack(side=tk.LEFT, padx=10)

root.title("image Browser")
root.geometry("300x500")
root.mainloop()

img=cv2.imread("image.jpg")
window_name='imagine RGB'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,img)

image_Gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
window_name='imagine Gray'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,image_Gray)

image_XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)
window_name='Imagine XYZ'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,image_XYZ)

image_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
window_name='Imagine_HSV'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,image_HSV)

cv2.waitKey(0)
cv2.destroyAllWindows()

