"""

Author: Jacob Sanders
_____________________

"""

import os
from Tkinter import *
import ttk
from ttk import *
import hashlib
from PIL import Image, ImageTk
import qrcode
import shutil

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


class InitFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)
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
        self.password_label.grid(column=2, row=2, sticky=(W+E))
        self.password_entry.grid(column=2, row=3, sticky=(W+E))
        self.submit.grid(column=2, row=4, sticky=(W+E))

    def submitPassword(self):
        self.password_var = self.password_entry.get()
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

    def focusOn(self):
        self.password_entry.focus()

    def binding(self):
        self.frame.bind("<Return>", self.submitPassword)


class ContextFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)

    def createStrVars(self):
        self.oldPassword_var = StringVar()
        self.passwordOne_var = StringVar()
        self.passwordTwo_var = StringVar()

    def createEntries(self):
        self.oldPassword_entry = ttk.Entry(self.frame, textvariable=self.oldPassword_var, show="*")
        self.passwordOne_entry = ttk.Entry(self.frame, textvariable=self.passwordOne_var, show="*")
        self.passwordTwo_entry = ttk.Entry(self.frame, textvariable=self.passwordTwo_var, show="*")      

    def createLabels(self):
        self.changePassword_label = ttk.Label(self.frame, text="Change Password")
        self.validCheck_label = ttk.Label(self.frame, text="Validity")
        self.oldPassword_label = ttk.Label(self.frame, text="Old Password")
        self.passwordOne_label = ttk.Label(self.frame, text="Password")
        self.passwordTwo_label = ttk.Label(self.frame, text="Re-enter")

    def createButtons(self):
        self.submit = ttk.Button(self.frame, text="Submit", command=self.submitPassword)

    def createMunus(self):
        self.event_menu = Menu(self.frame)

    def alignAll(self):     
        self.oldPassword_label.grid(column=1, row=2, sticky=(W+E))
        self.passwordOne_label.grid(column=1, row=3, sticky=(W+E))
        self.passwordTwo_label.grid(column=1, row=4, sticky=(W+E))
        
        self.oldPassword_entry.grid(column=2, row=2, sticky=(W+E))
        self.passwordOne_entry.grid(column=2, row=3, sticky=(W+E))
        self.passwordTwo_entry.grid(column=2, row=4, sticky=(W+E))
        
        self.changePassword_label.grid(column=2, row=1, sticky=(W+E))
        
        self.validCheck_label.grid(column=4, row=2, sticky=(W+E))
        self.submit.grid(column=4, row=4, sticky=(W+E))

    def submitPassword(self):
        self.passwordTwo_var = self.passwordTwo_entry.get()
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
        self.oldPassword_entry.focus()

    def binding(self):
        self.submit("<Return>", self.submitPassword)

    def removeOldPass(self):
        if(os.path.exists('user')):
            if(os.path.isfile('user/pass.txt')):
                os.remove('user/pass.txt')
        self.storePass()
    

class MainFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)

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
        self.encrypt = ttk.Button(self.frame, text="Encrypt", command=self.encryptData)

    def alignAll(self):
        
        #Column 1
        self.name_label.grid(column=1, row=2, sticky=(W+E))
        self.name_entry.grid(column=1, row=3, sticky=(W+E))
        self.data_entry.grid(column=1, row=4, sticky=(W+E))
        
        #Column 2
        self.event_label.grid(column=2, row=2, sticky=(W+E))
        self.event_entry.grid(column=2, row=3, sticky=(W+E))
        self.qr_label.grid(column=2, row=4, sticky=(W+E))
        
        #Column 3
        self.encrypt.grid(column=3, row=3, sticky=(W+E))

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
        
class OptionsFrame(SpecFrame):
    
    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)
        
    def clean(self):
        if (os.path.exists('user') == True):
            shutil.rmtree('user')
            
        if (os.path.exists('applicants') == True):
            shutil.rmtree('applicants')
        
    def createStrVars(self):
        pass

    def createLabels(self):
        self.cleanUp_label = Label(self.frame, text="Clear all data!")

    def createEntries(self):
        pass

    def createButtons(self):
        self.cleanUp = ttk.Button(self.frame, text="Clear All", command=self.clean)

    def alignAll(self):
        self.cleanUp.grid(column=3, row=3, sticky=(W+E))
        self.cleanUp_label.grid(column=3, row=4, sticky=(W+E))

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

        
def Main():
        
    """
        order of creation matters. initializer should be called last
        so that is can assert itself above or beloew other frames
        depending on the presence of a password file
        
    """
    
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
    contextFrame = ContextFrame("ChangePass", mainNoteBook)
    optionsFrame = OptionsFrame("Options", mainNoteBook)

    mainNoteBook.add(mainFrame.frame, text="Ticket Generator", state="normal")
    mainNoteBook.add(contextFrame.frame, text="Context", state="normal")
    mainNoteBook.add(optionsFrame.frame, text="Options", state="normal")
    mainNoteBook.pack()

    noteFrame.onTop()
    
    initFrame = InitFrame("Init", root)

    root.mainloop()


Main()
