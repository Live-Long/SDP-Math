# https://ryancheunggit.gitbooks.io/calculus-with-python/content/05Limits.html
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x
from tkinter import *
from PIL import ImageTk, Image

<<<<<<< HEAD
f = x ** 3 - 2 * x - 6
=======
def close_this_sht():
    plt.gcf()
    plt.clf()
    #plt.close()

f = x**3-2*x-6
>>>>>>> 38ff9e01c38b13866ff5b2166f4ebe8f4b823882


def init():
    d1 = np.linspace(2, 10, 1000)
    d2 = np.linspace(4, 8, 1000)
    d3 = np.linspace(5, 7, 1000)
    d4 = np.linspace(5.8, 6.2, 100)
    domains = [d1, d2, d3, d4]
    return domains


def makeplot(f, l, d):
    plt.plot(d, [f.evalf(subs={x: xval}) for xval in d], 'b',
             d, [l.evalf(subs={x: xval}) for xval in d], 'r')


def run(f):
    line = 106 * x - 438
    dom = init()
    imgx = 600
    imgy = 600

    root = Tk()
    root.title("Derivatives")
    root.geometry('{}x{}'.format(imgx, imgy))

    exitb = Button(root, text="Exit", bd=12, relief="raised", command=lambda: [close_this_sht(),root.destroy()],
                   width=15)
    exitb.configure(bg="gray", fg="white", font="Calibri 9 bold")
    exitb.pack(padx=10, pady=30)

    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()

    for i in range(len(dom)):
        plt.subplot(2, 2, i + 1)
        makeplot(f, line, dom[i])
        plt.savefig("Derivatives.png")

    imgName = "Derivatives.png"
    canvas = Canvas(root, width=imgx, height=imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName), master=root)
    canvas.create_image(0, 0, anchor=NW, image=img)
    # os.remove(imgName)

    for event in root.event.get():
        if event.type == root.QUIT:
            root.destroy()

    root.mainloop()


run(f)
