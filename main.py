import tkinter as tk
import sys
import os.path
save_path = "notes/"
root = tk.Tk(screenName="Note taker")

writing = tk.Frame(root)
reading = tk.Frame(root)
buttonContainer = tk.Frame(reading,background= "red")
#def functions
#ToDo: funtions to desplay the notes that are in the notes folder as buttons
def initNotes():
    print("initNotes was called")
    noteNames = os.listdir(save_path)
    print(noteNames)
    return noteNames

def loadButtons(noteNames):
    print("loadButtons() was called")
    for i in noteNames:
        tk.Button(buttonContainer,text=i,command = lambda note = i: loadNote(note)).pack()

def loadNote(fileName):
    with open(save_path + fileName) as f:
        titleBox.delete(0,"end")
        titleBox.insert(0, fileName)
        textBox.delete("1.0","end")
        textBox.insert("1.0",f.read())

def showNotes():
    print("showNotes() was called")
    loadButtons(initNotes())

#Function to save notes
def saveNote():
    print("saveNotes() was called")
    filePath = save_path + titleBox.get()
    f = open(filePath,"w")
    f.write(textBox.get("1.0", "end"))
    f.close()
    titleBox.delete(0,"end")
    textBox.delete("1.0","end")

#Funtions to refresh the list of notes
def clearContainer():
    for child in buttonContainer.winfo_children():
        child.destroy()

def clear():
    clearContainer()
    showNotes()
    

#Labes for instructions 
titleBoxLable = tk.Label(writing, text="Enter note title")
textBoxLable = tk.Label(writing, text= "Write your note below")

#Input boxes for note data
titleBox = tk.Entry(writing, width=20)
textBox = tk.Text(writing, height=20, width=20)

#Buttons
save = tk.Button(writing, text="save", command  = saveNote)
refresh = tk.Button(reading, text="refresh", command= clear)


#ToDo: Container to hold all of the notes in the note folder as buttons
noteDir = tk.Frame()

#packing all widgets
titleBoxLable.pack()
titleBox.pack()
textBoxLable.pack()
textBox.pack()
save.pack()
refresh.pack()
writing.pack(side="left")
reading.pack(side="left")
buttonContainer.pack()



#This function to to make sure the VScode fully end all processes when the x it's clicked so I don't have to do it manually
def exitApp():
    root.destroy()
    sys.exit()
#Making the clicking x run exitApp
root.protocol("WM_DELETE_WINDOW",exitApp)
tk.mainloop()