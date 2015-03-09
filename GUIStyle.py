#personal classes
from SpecFrame import ttk

class GUIStyle():
    
    def __init__ (self):
        self.configureAll()
        
    def configureAll(self):
        self.mainStyle = ttk.Style()
        self.mainStyle.configure("TFrame", background="#666666")
        self.mainStyle.configure("TLabel", background="#666666", foreground="#FFFFFF")
        self.mainStyle.configure("TNotebook", background="#666666")
        self.mainStyle.configure("TButton", background="#666666", foreground="#FF0066")
        self.mainStyle.configure("TEntry", background="#FF0066", foreground="#FF0066")
        self.mainStyle.configure("TPanedwindow", background="#FFFFFF")