#https://matplotlib.org/gallery/misc/fill_spiral.html
import os
from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image

def close_this_sht():
    plt.gcf()
    plt.clf()
    #plt.close()


def run(a,b):
    theta = np.arange(0, 8 * np.pi, 0.1)
    for dt in np.arange(0, 2 * np.pi, np.pi / 2.0):
        x = a * np.cos(theta + dt) * np.exp(b * theta)
        y = a * np.sin(theta + dt) * np.exp(b * theta)

        dt = dt + np.pi / 4.0

        x2 = a * np.cos(theta + dt) * np.exp(b * theta)
        y2 = a * np.sin(theta + dt) * np.exp(b * theta)

        xf = np.concatenate((x, x2[::-1]))
        yf = np.concatenate((y, y2[::-1]))

        p1 = plt.fill(xf, yf)

    plt.savefig("Fermat's Spiral.png")
    imgx = 600; imgy = 600

    root = Tk()
    root.geometry('{}x{}'.format(imgx, imgy))

    exitb = Button(root, text="Exit", bd=12, relief="raised", command=lambda: [close_this_sht(), root.destroy()], width=15)
    exitb.configure(bg="gray", fg="white", font="Calibri 9 bold")
    exitb.pack(padx=10, pady=30)


    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()

    imgName = "Fermat's Spiral.png"
    root.title("Fermat Spiral")
    canvas = Canvas(root, width = imgx, height = imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName), master=root)
    canvas.create_image(0, 0, anchor=NW, image=img)


    for event in root.event.get():
        if event.type == root.QUIT:
            plt.gcf()
            plt.close()
            #root.destroy()

    root.mainloop()


#parameter 2 numbers
a = 1
b = .5
run(a,b)


