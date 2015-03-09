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
        self.password_label.grid(column=2, row=2, sticky=("we"))
        self.password_entry.grid(column=2, row=3, sticky=("we"))
        self.submit.grid(column=2, row=4, sticky=("we"))

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
