"""

Author: Jacob Sanders
_____________________

"""

#personal classes
from MainFrame import *
from InitFrame import *
from ContextFrame import *
from OptionsFrame import *
from NoteBookFrame import *
from GUIStyle import *

        
def Main():
        
    """
        order of creation matters. initializer should be called last
        so that is can assert itself above or beloew other frames
        depending on the presence of a password file
        
    """
    
    root = Tk()
    root.title('Encrypted QR Ticket Generator')

    noteBookFrame = NoteBookFrame("Note", root)

    mainFrame = MainFrame("Main", noteBookFrame.noteBook)
    contextFrame = ContextFrame("ChangePass", noteBookFrame.noteBook)
    optionsFrame = OptionsFrame("Options", noteBookFrame.noteBook)

    noteBookFrame.noteBook.add(mainFrame.frame, text="Ticket Generator", state="normal")
    noteBookFrame.noteBook.add(contextFrame.frame, text="Context", state="normal")
    noteBookFrame.noteBook.add(optionsFrame.frame, text="Options", state="normal")
    noteBookFrame.noteBook.pack()

    noteBookFrame.onTop()
    
    initFrame = InitFrame("Init", root)

    root.mainloop()


Main()
