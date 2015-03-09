"""

    Title: QR Ticket Generator
    Description: Creates 'unique' QR images and files used for
        rapid verification of authenticity. It accomplishes this
        to the best of (my) ability and given effort.
    Copyright (C) 2015  Jacob Sanders
    
    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""

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
