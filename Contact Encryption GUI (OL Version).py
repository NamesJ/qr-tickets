"""

Author: Jacob Sanders
_____________________

"""

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
        self.createEntries()
        self.createButtons()
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

    def createEntries(self):
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
        """
        doesn't work..
        mainFrame.onTop()
        """
        self.onBottom()

    def focusOn(self):
        self.passwordVar_entry.focus()

    def binding(self):
        self.submit("<Return>", self.submitPassword)


class ChangePassFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)

    def createStrVars(self):
        self.oldPasswordVar = StringVar()
        self.passwordOneVar = StringVar()
        self.passwordTwoVar = StringVar()

    def createEntries(self):
        self.oldPasswordVar_entry = ttk.Entry(self.frame, textvariable=self.oldPasswordVar, show="*")
        self.passwordOneVar_entry = ttk.Entry(self.frame, textvariable=self.passwordOneVar, show="*")
        self.passwordTwoVar_entry = ttk.Entry(self.frame, textvariable=self.passwordTwoVar, show="*")      

    def createLabels(self):
        self.validCheckLabel = ttk.Label(self.frame, text="")
        self.oldPasswordLabel = ttk.Label(self.frame, text="Old Password")
        self.passwordOneLabel = ttk.Label(self.frame, text="Password")
        self.passwordTwoLabel = ttk.Label(self.frame, text="Re-enter")

    def createButtons(self):
        self.submit = ttk.Button(self.frame, text="Submit", command=self.submitPassword)

    def alignAll(self):
        self.validCheckLabel.grid(column=4, row=2, sticky=(W+E))
        
        self.oldPasswordLabel.grid(column=1, row=2, sticky=(W+E))
        self.oldPasswordVar_entry.grid(column=2, row=2, sticky=(W+E))
        
        self.passwordOneLabel.grid(column=1, row=3, sticky=(W+E))
        self.passwordOneVar_entry.grid(column=2, row=3, sticky=(W+E))

        self.passwordTwoLabel.grid(column=1, row=4, sticky=(W+E))
        self.passwordTwoVar_entry.grid(column=2, row=4, sticky=(W+E))
        
        self.submit.grid(column=4, row=4, sticky=(W+E))

    def submitPassword(self):
        self.passwordTwoVar = self.passwordTwoVar_entry.get()
        self.encryptPass()

    def encryptPass(self):
        m = hashlib.md5()
        m.update(self.passwordTwoVar)
        self.encryptedPass = m.hexdigest()
        self.removeOldPass()

    def storePass(self):
        my_file_name = 'user/pass.txt'
        my_file = open(my_file_name, 'w')
        my_file.write(self.encryptedPass)
        my_file.close()
        """
        doesn't work..
        mainFrame.onTop()
        """
        self.onBottom()

    def focusOn(self):
        self.oldPasswordVar_entry.focus()

    def binding(self):
        self.submit("<Return>", self.submitPassword)

    def removeOldPass(self):
        if(os.path.exists('user')):
            if(os.path.isfile('user/pass.txt')):
                os.remove('user/pass.txt')
        self.storePass()
    

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

    def createEntries(self):
        self.passwordVar_entry = ttk.Entry(self.frame, textvariable=self.passwordVar, show="*")

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
        """
        Doesn't work..
        mainFrame.onTop()
        """
        self.onBottom()

    def focusOn(self):
        self.passwordVar_entry.focus()

    def binding(self):
        self.frame.bind("<Return>", self.submitPassword)


class MainFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)

    def createStrVars(self):
        self.nameVar = StringVar()
        self.eventVar = StringVar()
        self.dataVar = StringVar()

    def createLabels(self):
        self.nameLabel = ttk.Label(self.frame, text="Name")
        self.eventLabel = ttk.Label(self.frame, text="Event Name")
        #password is now stored in a file
        #self.passwordLabel = ttk.Label(self.frame, text="Password")
        self.defaultQRCode()

    def createEntries(self):
        self.nameVar_entry = ttk.Entry(self.frame, textvariable=self.nameVar)
        self.eventVar_entry = ttk.Entry(self.frame, textvariable=self.eventVar)
        """
        password is now stored in a file
        self.passwordVar_entry = ttk.Entry(self.frame, textvariable=self.passwordVar, show="*")
        """
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
        """
        password is now stored in a file
        self.passwordLabel.grid(column=3, row=2, sticky=(W+E))
        self.passwordVar_entry.grid(column=3, row=3, sticky=(W+E))
        """
        self.encrypt.grid(column=3, row=4, sticky=(W+E))

    def encryptData(self):

        #Pull or "get" the data from entry
        name = self.nameVar.get()
        event = self.eventVar.get()
        """
        password is instead pulled from a file for convenience
        password = self.passwordVar.get()
        """

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
        "entered_pass" is so unecessary now
        entered_pass = hashlib.md5()
        entered_pass.update(password)
        entered_pass.hexdigest()
        
        Add our entered information to an array for convenience
        password is encryped twice, I may change this
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
                    
            """
            Why was this here?
            encrypted_data = encrypted
            """
            #need to del encrypted_data_entry
            self.dataVar_entry.insert(0, encrypted)


    def printPassword(self):
        print self.passwordVar

    def focusOn(self):
        self.nameVar_entry.focus()

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
        
        
def Main():
        
    root = Tk()
    root.title('Encrypted QR Ticket Generator')

    mainStyle = Style()
    mainStyle.configure("TFrame", background="#666666")
    mainStyle.configure("TLabel", background="#666666", foreground="#FFFFFF")
    mainStyle.configure("TNotebook", background="#666666")
    mainStyle.configure("TButton", background="#666666", foreground="#FF0066")
    mainStyle.configure("TEntry", background="#FF0066", foreground="#FF0066")
    mainStyle.configure("TPanedwindow", background="#FFFFFF")

    noteFrame = SpecFrame("Note", root)
    mainNoteBook = ttk.Notebook(noteFrame.frame)

    mainFrame = MainFrame("Main", mainNoteBook)
    changePassFrame = ChangePassFrame("ChangePass", mainNoteBook)
    initFrame = InitFrame("Init", root)

    mainNoteBook.add(changePassFrame.frame, text="Change Password", state="normal")
    mainNoteBook.add(mainFrame.frame, text="Ticket Generator", state="normal")

    mainNoteBook.pack()

    noteFrame.onTop()

    root.mainloop()


Main()
