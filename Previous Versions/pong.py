from tkinter import*
import time
import random

tk =Tk()
tk.title('MiPong')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
