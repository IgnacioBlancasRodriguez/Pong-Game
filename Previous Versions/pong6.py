from tkinter import*
import time
import random

class Pelota:
    def __init__(self,canvas,raquta,color):
        self.canvas = canvas
        self.raqueta = raqueta
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        empezar = [-3,-2,-1,1,2,3]
        random.shuffle(empezar)
        self.x = empezar[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def golpear_raqueta(self,pos):
        raquta_pos = self.canvas.coords(self.raquta.id)
        if pos[2] >= raqueta_pos[0] and pos[0] <= raqueta_pos[2]:
            if pos[3] >= raquta_pos[1] and pos[3] <= raqueta_pos[3]:
                return True
            return False
    
    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.golpear_raqueta(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Raqueta:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.ir_izq)
        self.canvas.bind_all('<KeyPress-Right>',self.ir_der)

    def ir_izq(self,evt):
        self.x = -2
    def ir_der(self,evt):
        self.x = 2

    def dibujar(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos [0] <= 0:
            self.x = 0
        if pos [2] >= self.canvas_width:
            self.x = 0
 


tk =Tk()
tk.title('MiPong')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()


pelota = Pelota(canvas,raqueta,'red')
raqueta = Raqueta(canvas,'blue')

while 1:
    pelota.dibujar()
    raqueta.dibujar()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
