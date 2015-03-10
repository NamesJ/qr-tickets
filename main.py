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
from SpecFrame import Tk
from GeneratorFrame import GeneratorFrame
from InitFrame import InitFrame
from ContextFrame import ContextFrame
from OptionsFrame import OptionsFrame
from NoteBook import NoteBook
from GUIStyle import GUIStyle

        
def Main():
        
    """
        order of creation of objects matters. initFrame should be called last
        so that is can assert itself above or below other frames
        depending on the presence of a password file
        
    """
    
    root = Tk()
    root.title('QR Ticket Generator')
    
    mainStyle = GUIStyle()
    
    noteBook = NoteBook("notebook", root)

    mainFrame = GeneratorFrame("Main", noteBook)
    contextFrame = ContextFrame("ChangePass", noteBook)
    optionsFrame = OptionsFrame("Options", noteBook)

    noteBook.add(mainFrame.frame, text="Ticket Generator", state="normal")
    noteBook.add(contextFrame.frame, text="Context", state="normal")
    noteBook.add(optionsFrame.frame, text="Options", state="normal")
    noteBook.grid(column=0, row=0, sticky=("nwes"))
    
    initFrame = InitFrame("Init", root)
    
    for child in root.children.values():
        child.columnconfigure=1
        child.rowconfigure=1

    root.mainloop()


Main()
