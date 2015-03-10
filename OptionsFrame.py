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

#personal classes
from SpecFrame import *

class OptionsFrame(SpecFrame):
    
    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)  # @UndefinedVariable
        
    def clean(self):
        if (os.path.exists('user') == True):
            shutil.rmtree('user')
            
        if (os.path.exists('applicants') == True):
            shutil.rmtree('applicants')
        
    def createStrVars(self):
        pass

    def createLabels(self):
        self.cleanUp_label = ttk.Label(self.frame, text="Clear all data!")

    def createEntries(self):
        pass

    def createButtons(self):
        self.cleanUp = ttk.Button(self.frame, text="Clear All", command=self.clean)

    def alignAll(self):
        self.cleanUp.grid(column=3, row=3, sticky=("wens"))
        self.cleanUp_label.grid(column=3, row=4, sticky=("wens"))

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
