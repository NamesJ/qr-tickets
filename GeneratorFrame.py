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

class GeneratorFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)  # @UndefinedVariable

    def createStrVars(self):
        self.name_var = StringVar()
        self.event_var = StringVar()
        self.data_var = StringVar()

    def createLabels(self):
        self.name_label = ttk.Label(self.frame, text="Name")
        self.event_label = ttk.Label(self.frame, text="Event Name")
        #password is now stored in a file
        #self.password_label = ttk.Label(self.frame, text="Password")
        self.defaultQRCode()

    def createEntries(self):
        self.name_entry = ttk.Entry(self.frame, textvariable=self.name_var)
        self.event_entry = ttk.Entry(self.frame, textvariable=self.event_var)
        """
        password is now stored in a file
        self.password_entry = ttk.Entry(self.frame, textvariable=self.passwordVar, show="*")
        """
        self.data_entry = ttk.Entry(self.frame, textvariable=self.data_var)

    def createButtons(self):
        self.encrypt = ttk.Button(self.frame, text="Generate", command=self.encryptData)

    def alignAll(self):
        
        #Column 1
        self.name_label.grid(column=1, row=2, sticky=("wens"))
        self.name_entry.grid(column=1, row=3, sticky=("wens"))
        self.data_entry.grid(column=1, columnspan=2, row=4, sticky=("wens"))
        
        #Column 2
        self.event_label.grid(column=2, row=2, sticky=("wens"))
        self.event_entry.grid(column=2, row=3, sticky=("wens"))
        
        #Column 3
        self.encrypt.grid(column=3, row=3, sticky=("wens"))
        self.qr_label.grid(column=3, row=4, sticky=("wens"))
        
    def encryptData(self):

        #Pull or "get" the data from entry
        name = self.nameVar.get()
        event = self.eventVar.get()

        #read stored password from file
        my_file_name = 'user/pass.txt'
        my_file = open(my_file_name, 'r')

        #passTest = my_file.read()
        password = my_file.read()

        my_file.close()
        #This creates our container to make a qr code
        qr = qrcode.QRCode (
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 2
        )

        #m 
        m = hashlib.md5()
        """
        Add our entered information to an array for convenience
        password is encrypted twice, I may change this
        """
        data = [name, event, password]

        #Create the folder for applicants if it doesn't already exist
        if (os.path.exists('applicants')) == False:
            os.makedirs('applicants')

        #Verify that the correct password was entered
        if (os.path.isfile('user/pass.txt')):
            if (os.path.exists('applicants/' + name)) == False:
                os.makedirs('applicants/' + name)

            #Update contact encryption
            for x in data:
                m.update(x)

            #Digest it (create it)... yum once more
            encrypted = m.hexdigest()

            #Add date to our qr code
            qr.add_data('Name: ' + name)
            qr.add_data('\r\nEvent name: ' + event)
            qr.add_data('\r\nEncrypted data: ' + encrypted)
            #Fit it properly (The fit is true sounds medieval)
            qr.make(fit=True)
            #Create a variable for our created qr code
            img = qr.make_image()
            #Save it as a png file
            img.save('applicants/' + name + '/' + name + '.png')

            #This writes the entered and encrypted information to a txt file
            my_file_name = 'applicants/' + name + '/' + name + '.txt'
            my_file = open(my_file_name, 'w')
            my_file.write('Name: ' + name)
            my_file.write('\n\nEvent name: ' + event)
            my_file.write('\n\nEncrypted data: ' + encrypted)
            my_file.close()

            #This displays the image to the screen
            qr_img = Image.open('applicants/' + name + '/' + name + '.png')
            qr_image = ImageTk.PhotoImage(qr_img)
            self.qr_label.configure(image=qr_image)
            self.qr_label.image = qr_image

            #need to load encrypted_data_entry
            self.data_entry.insert(0, encrypted)
            

    def focusOn(self):
        self.name_entry.focus()

    def binding(self):
        self.frame.bind("<Return>", self.encryptData)

    def defaultQRCode(self):
        qr_default = qrcode.QRCode (
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 2
        )
        qr_default.add_data('https://github.com/NamesJ/qr-tickets')
        qr_default.make(fit=True)
        qr_img_default = qr_default.make_image()
        qr_img_default.save('default.png')
        default_img = Image.open('default.png')
        default_image = ImageTk.PhotoImage(default_img)
        #label gets special self permission to be stored
        self.qr_label = Label(self.frame, image=default_image)
        self.qr_label.image = default_image
        #there is no reason to keep this image around
        os.remove('default.png')

