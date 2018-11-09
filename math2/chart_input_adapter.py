import tkinter
# Lots of tutorials have from tkinter import *, but that is pretty much always a bad idea
from tkinter import ttk
import abc

from math2 import bar_chart


class Window(ttk.Frame):
    """Abstract base class for a popup window"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, parent):
        """ Constructor """
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False)  # Disallows window resizing

        # Creates Tcl wrapper for python function. %P = new contents of field after the edit.
        self.validate_notEmpty = (self.register(self.not_empty), '%P')

    @abc.abstractmethod
    def do_something(self):
        """Does something that all popup windows need to do"""
        pass

    @staticmethod
    def not_empty(P):
        """Validates Entry fields to ensure they aren't empty"""
        if P.strip():
            valid = True
        else:
            print("Error: Field must not be empty.")  # Prints to console
            valid = False
        return valid

    def close_win(self):
        """Closes window"""
        self.parent.destroy()


class OpenNewWindow(Window):
    """ New popup window """

    def __init__(self, parent):
        super().__init__(parent)
        self.parent.title("Enter Details")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=1)

        # Create Widgets
        self.contentFrame = ttk.Frame(self.parent, relief="sunken")
        self.label_title = ttk.Label(self.parent, text="Enter 9 y values (In form a,b,c...)")
        self.cancelButton = ttk.Button(self.parent, text='Cancel', command=self.close_win)
        self.runButton = ttk.Button(self.parent, text='Run', command=self.do_something)
        self.heightInputTest = ttk.Entry(self.contentFrame, width=30, validate='focusout',
                                         validatecommand=self.validate_notEmpty)
        self.heightInputLabel = ttk.Label(self.contentFrame, text='Input:')

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.contentFrame.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.heightInputLabel.grid(row=0, column=0)
        self.heightInputTest.grid(row=0, column=1, sticky='w')

        self.runButton.grid(row=3, column=0, sticky='e')
        self.cancelButton.grid(row=3, column=1, sticky='e')

        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentFrame.winfo_children():
            child.grid_configure(padx=5, pady=2)

    def do_something(self):
        """Does something"""
        height = str(self.heightInputTest.get().strip())
        print(height)
        height = height.split(',')
        print(height)
        for i in range(len(height)):
            height[i] = float(height[i])

        bar_chart.run(height)
        # self.close_win()


def run():
    root2 = tkinter.Tk()
    OpenNewWindow(root2)
    root2.mainloop()


run()
