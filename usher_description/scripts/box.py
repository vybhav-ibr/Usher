

import tkinter as tk
from time import sleep

class GUI:
    s=""
    #root = tk.Tk()
    def button_callback(button,self):
        GUI.returnroom(button.cget("text"),self)
        sleep(.5)
        self.root.destroy()

    def bottom_callback(self):
        GUI.returnroom("Reception",self)
        sleep(.5)
        self.root.destroy()
    def returnroom(a,self):
        if a[0:2]=="Ro":
            self.s=a[5::]
        else:
            self.s=a
        #self.root.destroy()
        #print("50",self.s)
        #exit
    def killwind(self):
        self.root.destroy()
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Select Room")
        self.root.geometry("440x420")
        top_frame = tk.Frame(self.root)
        top_frame.pack(side=tk.TOP,pady=50)
        for i in range(7):
            for j in range(4):
                button = tk.Button(top_frame, text=f"Room {i+1}-{j+1}")
                button.config(command=lambda button=button: GUI.button_callback(button,self))
                if j == 1:
                    button.grid(row=i, column=j, padx=(0, 50), pady=2)  # Use a tuple for the padx option to set left and right padding separately
                else:
                    button.grid(row=i, column=j, padx=1, pady=2)


        # Create a new button inside the bottom frame
        b_button = tk.Button(self.root, text="Reception")
        b_button.config(command=lambda b_button=b_button: GUI.bottom_callback(self))
        b_button.pack()
        #button.pack(pady=120)
        self.root.mainloop(0)
#g1=GUI()
#print(g1.s)
#g1.killwind()
