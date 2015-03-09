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
        self.cleanUp_label = Label(self.frame, text="Clear all data!")

    def createEntries(self):
        pass

    def createButtons(self):
        self.cleanUp = ttk.Button(self.frame, text="Clear All", command=self.clean)

    def alignAll(self):
        self.cleanUp.grid(column=3, row=3, sticky=("we"))
        self.cleanUp_label.grid(column=3, row=4, sticky=("we"))

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
