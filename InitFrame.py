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

class InitFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)  # @UndefinedVariable
        self.createDirs()

    def createDirs(self):
        if (os.path.exists('user')) == False:
            os.makedirs('user')
        else:
            if (os.path.isfile('user/pass.txt')):
                self.onBottom()

    def createStrVars(self):
        self.password_var = StringVar()

    def createLabels(self):
        self.password_label = ttk.Label(self.frame, text="Password")

    def createEntries(self):
        self.password_entry = ttk.Entry(self.frame, textvariable=self.password_var, show="*")

    def createButtons(self):
        self.submit = ttk.Button(self.frame, text="Submit", command=self.submitPassword)

    def alignAll(self):
        self.password_label.grid(column=2, row=2, sticky=("wens"))
        self.password_entry.grid(column=2, row=3, sticky=("wens"))
        self.submit.grid(column=2, row=4, sticky=("wens"))

    def submitPassword(self):
        self.password_var = self.password_entry.get()
        self.encryptPass()

    def encryptPass(self):
        m = hashlib.md5()
        m.update(self.password_var)
        self.encryptedPass = m.hexdigest()
        self.storePass()

    def storePass(self):
        my_file_name = 'user/pass.txt'
        my_file = open(my_file_name, 'w')
        my_file.write(self.encryptedPass)
        my_file.close()
        self.onBottom()

    def focusOn(self):
        self.password_entry.focus()

    def binding(self):
        self.frame.bind("<Return>", self.submitPassword)
