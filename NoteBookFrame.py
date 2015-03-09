#personal classes
from SpecFrame import *

class NoteBookFrame(SpecFrame):
	
	def __init__(self, name, parent):
		SpecFrame.__init__ (self, name, parent)  # @UndefinedVariable
		self.createNoteBooks()
		
	def createNoteBooks(self):
		self.noteBook = ttk.Notebook(self.frame)