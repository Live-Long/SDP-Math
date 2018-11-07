# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import

import copy
from tkinter import *
import random

class raindrop(object):
    def clone(self):
        pass

class red_drop(raindrop):
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.cv = None
        self.r = 0
        self.a = random.randint(1, 4) * 1.
        self.v = 1
        self.color = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 0), random.randint(0, 0))
    def clone(self):
        return copy.copy(self)
    def set_x(self):
        self.x = random.randint(0, 1280)
        return self

    def set_y(self):
        self.y = random.randint(0, 720)
        return self

    def set_color(self):
        self.color = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 0), random.randint(0, 0))
        return self

class green_drop(raindrop):
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.cv = None
        self.r = 0
        self.a = random.randint(1, 4) * 1.
        self.v = 1
        self.color = '#%02x%02x%02x' % (random.randint(0, 0), random.randint(0, 255), random.randint(0, 0))
    def clone(self):
        return copy.copy(self)
    def set_x(self):
        self.x = random.randint(0, 1280)
        return self
    def set_y(self):
        self.y = random.randint(0, 720)
        return self
    def set_color(self):
        self.color = '#%02x%02x%02x' % (random.randint(0, 0), random.randint(0, 255), random.randint(0, 0))
        return self

class blue_drop(raindrop):
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.cv = None
        self.r = 0
        self.a = random.randint(1, 4) * 1.
        self.v = 1
        self.color = '#%02x%02x%02x' % (random.randint(0, 0), random.randint(0, 0), random.randint(0, 255))
    def clone(self):
        return copy.copy(self)
    def set_x(self):
        self.x = random.randint(0, 1280)
        return self
    def set_y(self):
        self.y = random.randint(0, 720)
        return self
    def set_color(self):
        self.color = '#%02x%02x%02x' % (random.randint(0, 0), random.randint(0, 0), random.randint(0, 255))
        return self


class MyApp(Tk):
    def __init__(self):
        self.red_drop_object = red_drop(1280,720)
        self.green_drop_object = green_drop(1280, 720)
        self.blue_drop_object = blue_drop(1280, 720)

        self.nbi = 0
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.canvas = Canvas(fr, height=720, width=1280, bg='black')
        self.canvas.pack()
        self.drops = []
        return

    def update_drops(self, ):
        self.drops.append(self.red_drop_object.clone().set_x().set_y().set_color())
        self.drops.append(self.green_drop_object.clone().set_x().set_y().set_color())
        self.drops.append(self.blue_drop_object.clone().set_x().set_y().set_color())

        toremove = []
        for idx, drop_ in enumerate(self.drops):
            self.drops[idx].r += self.drops[idx].v
            self.drops[idx].a -= 0.05
            if self.drops[idx].a <= 0.:
                toremove.append(idx)
            else:
                if self.drops[idx].cv:
                    self.canvas.delete(self.drops[idx].cv)
                self.drops[idx].cv = self.canvas.create_oval(self.drops[idx].x - self.drops[idx].r,
                                                             self.drops[idx].y - self.drops[idx].r,
                                                             self.drops[idx].x + self.drops[idx].r,
                                                             self.drops[idx].y + self.drops[idx].r)
                self.canvas.itemconfig(self.drops[idx].cv, outline=self.drops[idx].color)
                self.canvas.itemconfig(self.drops[idx].cv, width=self.drops[idx].a)
        for i in toremove:
            self.canvas.delete(self.drops[i].cv)
            self.drops.pop(i)
        self.canvas.update()

        return


def run():
    root = MyApp()
    i = 0
    while 1:
        try:
            root.update_drops()
            root.after(1)
        except Exception:
            print("Terminating")
            exit()


run()
