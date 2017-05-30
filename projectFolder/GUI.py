from Tkinter import *
import train_m as tr 
import test_m as t
import tkMessageBox

def ask_quit():
    if tkMessageBox.askokcancel("Quit", "You want to quit now? "):
        root.destroy()

def classify(): 
    if mylabel.visible: 
        
        btn.place_forget()
        root.title("Classification")
        
#         picture = PhotoImage(file="image/new.gif")
#         newlabel = Label(root, compound = CENTER, image = picture)
#         newlabel.visible = True 
#         newlabel.place(x = 0, y = 0)
#                   
        btn_train = Button(root, height = 2, width = 20, text = "Train", font = "Arial", command = tr.train)
        btn_train.place(x = 70, y = 310)
        btn_test = Button(root, height = 2, width = 20, text = "Test", font = "Arial", command = t.test)
        btn_test.place(x = 350, y = 310)
              


if __name__ == '__main__':        
    root = Tk() 
    
    picture = PhotoImage(file="image/1.gif")
    
    root.title("Music Genre Classification")
    root.geometry("600x400")
    
    mylabel = Label(root, compound = CENTER, image = picture)
    mylabel.visible = True 
    mylabel.place(x = 0, y = 0) 
    
    btn = Button(root, height = 2, width = 50, text="CLICK HERE TO START!", font = 'Arial', relief=GROOVE, command = classify) 
    btn.place(x = 60, y = 310)
    
    root.protocol("WM_DELETE_WINDOW", ask_quit)

    root.mainloop()
    