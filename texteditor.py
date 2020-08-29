from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    root = Tk()
    root.title("Untitled - EdiPy")
    TextArea = Text(root,font=("arial",15))
    menubar = Menu(root)

    FileMenu = Menu(menubar,tearoff=0)
    EditMenu = Menu(menubar, tearoff=0)
    HelpMenu = Menu(menubar, tearoff=0)

    Scrollbar = Scrollbar(TextArea)
    file = None


    def __init__(self):
        #text area adjustable
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.TextArea.grid(sticky=N + S + E + W)

        #file menu
        self.FileMenu.add_command(label="New",command=self.new_File)
        self.FileMenu.add_command(label="Open",command=self.open_file)
        self.FileMenu.add_command(label="Save",command=self.save_File)
        self.FileMenu.add_command(label="Save As",command=self.saveAs_File)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit",activebackground="red",command=self.quit_App)
        self.menubar.add_cascade(label="File", menu=self.FileMenu)

        #edit menu
        self.EditMenu.add_command(label="Select All    ( ctrl + A )",command=self.SelectAll)
        self.EditMenu.add_command(label="Cut              ( ctrl + X )",command=self.cut)
        self.EditMenu.add_command(label="Copy           ( ctrl + C )",command=self.copy)
        self.EditMenu.add_command(label="Paste           ( ctrl + V )",command=self.paste)
        self.menubar.add_cascade(label="Edit", menu=self.EditMenu)

        #help menu
        self.HelpMenu.add_command(label="About Notepad", command=self.show_About)
        self.menubar.add_cascade(label="Help", menu=self.HelpMenu)

        self.root.config(menu=self.menubar)
        self.Scrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.Scrollbar.set)


    def quit_App(self):
        self.root.destroy()
    def show_About(self):
        showinfo("Edipy","This is Normal Text Editor Application. Nilesh Raj ")

    def open_file(self):
        self.file = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("text document ","*.txt")])
        if self.file == "":
            self.file=None
        else:
            self.root.title(os.path.basename(self.file)+" -EdiPy")
            self.TextArea.delete(1.0,END)
            file=open(self.file,"r")
            self.TextArea.insert(1.0,file.read())
            file.close()
    def new_File(self):
        self.root.title("Untitled - EdiPy")
        self.file=None
        self.TextArea.delete(1.0,END)

    def save_File(self):
        if self.file == None :
            self.file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("text document ",".txt")])
            if self.file == "":
                self.file=None
            else:
                file=open(self.file,"w")
                file.write(self.TextArea.get(1.0,END))
                file.close()
                self.root.title(os.path.basename(self.file)+" - EdiPy")
        else:
            file = open(self.file,"w")
            file.write(self.TextArea.get(1.0,END))
            file.close()
    def saveAs_File(self):
        if self.file == None :
            self.file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("text document ",".txt")])
            if self.file == " ":
                self.file=None
            else:
                file=open(self.file,"w")
                file.write(self.TextArea.get(1.0,END))
                file.close()
                self.root.title(os.path.basename(self.file)+" - EdiPy")
        else:
            file = open(self.file,"w+")
            file.write(self.TextArea.get(1.0,END))
            file.close()


    def cut(self):
        self.TextArea.event_generate("<<Cut>>")
    def SelectAll(self):
        self.TextArea.event_generate("<<Select All>>")
    def copy(self):
        self.TextArea.event_generate("<<Copy>>")
    def paste(self):
        self.TextArea.event_generate("<<Paste>>")



    def run(self):
        self.root.mainloop()

notepad = Notepad()
notepad.run()


