#personal classes
from SpecFrame import *

class ContextFrame(SpecFrame):

    def __init__ (self, name, parent):
        SpecFrame.__init__(self, name, parent)  # @UndefinedVariable

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
        self.oldPassword_label.grid(column=1, row=2, sticky=("we"))
        self.passwordOne_label.grid(column=1, row=3, sticky=("we"))
        self.passwordTwo_label.grid(column=1, row=4, sticky=("we"))
        
        self.oldPassword_entry.grid(column=2, row=2, sticky=("we"))
        self.passwordOne_entry.grid(column=2, row=3, sticky=("we"))
        self.passwordTwo_entry.grid(column=2, row=4, sticky=("we"))
        
        self.changePassword_label.grid(column=2, row=1, sticky=("we"))
        
        self.validCheck_label.grid(column=4, row=2, sticky=("we"))
        self.submit.grid(column=4, row=4, sticky=("we"))

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