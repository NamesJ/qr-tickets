import os
from Tkinter import *
import ttk
from ttk import *
import hashlib
#I'm not sure if `import PIL as PilImage` is still necessary?
import PIL as PilImage
from PIL import Image, ImageTk
import qrcode

class SpecFrame(object):

    def __init__ (self, name, parent):
        self.name = name
        self.frame = ttk.Frame(parent, padding='3 3 12 12')
        self.frame.grid(row=0, column=0, sticky=(N+W+E+S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.createStrVars()
        self.createLabels()
        self.createEntrys()
        self.createButtons()
        self.alignAll()
        self.focusOn()
        self.padding()

    def createStrVars(self):
        pass

    def createLabels(self):
        pass

    def createEntrys(self):
        pass

    def createButtons(self):
        pass

    def alignAll(self):
        pass

    def submitPassword(self):
        pass

    def printPassword(self):
        pass

    def focusOn(self):
        pass

    def binding(self):
        pass

    def onTop(self):
        self.frame.lift()

    def onBottom(self):
        self.frame.lower()

    def padding(self):
        for child in self.frame.winfo_children(): child.grid_configure(padx=5, pady=5)


class InitFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)
        self.createDirs()

    def createDirs(self):
        if (os.path.exists('user')) == False:
            os.makedirs('user')

    def createStrVars(self):
        self.passwordVar = StringVar()

    def createLabels(self):
        self.passwordLabel = ttk.Label(self.frame, text="Password")

    def createEntrys(self):
        self.passwordVar_entry = ttk.Entry(self.frame, textvariable=self.passwordVar)

    def createButtons(self):
        self.submit = ttk.Button(self.frame, text="Submit", command=self.submitPassword)

    def alignAll(self):
        self.passwordLabel.grid(column=2, row=2, sticky=(W+E))
        self.passwordVar_entry.grid(column=2, row=3, sticky=(W+E))
        self.submit.grid(column=2, row=4, sticky=(W+E))

    def submitPassword(self):
        self.passwordVar = self.passwordVar_entry.get()
        self.encryptPass()

    def encryptPass(self):
        m = hashlib.md5()
        m.update(self.passwordVar)
        self.encryptedPass = m.hexdigest()
        self.storePass()

    def storePass(self):
        my_file_name = 'user/pass.txt'
        my_file = open(my_file_name, 'w')
        my_file.write(self.encryptedPass)
        my_file.close()
        self.onBottom()

    def printPassword(self):
        print self.passwordVar

    def focusOn(self):
        self.passwordVar_entry.focus()

    def binding(self):
        self.submit("<Return>", self.submitPassword)
        

class MainFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)

    def createStrVars(self):
        self.nameVar = StringVar()
        self.eventVar = StringVar()
        self.passwordVar = StringVar()
        self.dataVar = StringVar()

    def createLabels(self):
        self.nameLabel = ttk.Label(self.frame, text="name")
        self.eventLabel = ttk.Label(self.frame, text="Event Name")
        self.passwordLabel = ttk.Label(self.frame, text="Password")
        self.defaultQRCode()

    def createEntrys(self):
        self.nameVar_entry = ttk.Entry(self.frame, textvariable=self.nameVar)
        self.eventVar_entry = ttk.Entry(self.frame, textvariable=self.eventVar)
        self.passwordVar_entry = ttk.Entry(self.frame, textvariable=self.passwordVar)
        self.dataVar_entry = ttk.Entry(self.frame, textvariable=self.dataVar)

    def createButtons(self):
        self.encrypt = ttk.Button(self.frame, text="Encrypt", command=self.encryptData)

    def alignAll(self):
        #Column 1
        self.nameLabel.grid(column=1, row=2, sticky=(W+E))
        self.nameVar_entry.grid(column=1, row=3, sticky=(W+E))
        self.dataVar_entry.grid(column=1, row=4, sticky=(W+E))
        
        #Column 2
        self.eventLabel.grid(column=2, row=2, sticky=(W+E))
        self.eventVar_entry.grid(column=2, row=3, sticky=(W+E))
        self.qr_label.grid(column=2, row=4, sticky=(W+E))
        
        #Column 3
        self.passwordLabel.grid(column=3, row=2, sticky=(W+E))
        self.passwordVar_entry.grid(column=3, row=3, sticky=(W+E))
        self.encrypt.grid(column=3, row=4, sticky=(W+E))

    def encryptData(self):

        #Pull or "get" the data from entry
        name = self.nameVar.get()
        event = self.eventVar.get()
        password = self.passwordVar.get()
        my_file_name = 'user/pass.txt'
        my_file = open(my_file_name, 'r')
        passTest = my_file.read()
        my_file.close()
        #This creates our container to make a qr code
        qr = qrcode.QRCode (
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 2
        )

        #Create our encryption container
        m = hashlib.md5()
        #Create our password encryption container (mentioned above)
        entered_pass = hashlib.md5()
        #Plug-in our password to the container
        entered_pass.update(password)
        #Digest it (create it)... yum
        entered_pass.hexdigest()
        #Add our entered information to an array for convenience
        data = [name, event, password]

        #Create the folder for applicants if it doesn't already exist
        if (os.path.exists('applicants')) == False:
            os.makedirs('applicants')

        #Verify that the correct password was entered
        if (str(entered_pass.hexdigest()) == passTest) or True:
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

            #This will display the image on the label... after I fix it
            #FIXED IT!
            qr_img = Image.open('applicants/' + name + '/' + name + '.png')
            qr_image = ImageTk.PhotoImage(qr_img)
            self.qr_label.configure(image=qr_image)
            self.qr_label.image = qr_image
                    
            encrypted_data = encrypted
            #need to del encrypted_data_entry
            self.dataVar_entry.insert(0, encrypted_data)


    def printPassword(self):
        print self.passwordVar

    def focusOn(self):
        self.passwordVar_entry.focus()

    def binding(self):
        self.encrypt("<Return>", self.submitPassword)

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
        #label gets special self permission
        self.qr_label = Label(self.frame, image=default_image)
        self.qr_label.image = default_image

        
def Main():
        
    root = Tk()
    root.title('Event Encrypted QR Ticket Generator')

    mainFrame = MainFrame("Main", root)
    initFrame = InitFrame("Init", root)
    initFrame.frame.lift()

    root.mainloop()


Main()
