import os
from Tkinter import Tk, StringVar, Label, Entry, Menu
import ttk
import shutil
import hashlib
import qrcode
from PIL import Image, ImageTk

class SpecFrame(object):

    def __init__ (self, name, parent):
        self.name = name
        self.frame = ttk.Frame(parent, padding='3 3 12 12')
        self.frame.grid(row=0, column=0, sticky=("nesw"))  # @UndefinedVariable
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.createStrVars()
        self.createLabels()
        self.createEntries()
        self.createButtons()
        self.createMenus()
        self.alignAll()
        self.focusOn()
        self.padding()

    def createStrVars(self):
        pass

    def createLabels(self):
        pass

    def createEntries(self):
        pass

    def createButtons(self):
        pass
    
    def createMenus(self):
        pass

    def alignAll(self):
        pass

    def submitPassword(self):
        pass

    def focusOn(self):
        pass

    def binding(self):
        pass

    def onTop(self):
        self.frame.lift()
        self.binding()
        self.focusOn()

    def onBottom(self):
        self.frame.lower()

    def padding(self):
        for child in self.frame.winfo_children(): child.grid_configure(padx=5, pady=5)
