




from matplotlib import pyplot as p
from matplotlib import animation
from matplotlib import gridspec as gs
from tkinter import *
import numpy as n
from psutil import virtual_memory
from psutil import cpu_percent
from time import sleep


t = Tk()

ss = gs.GridSpec(3,2)

fg = p.figure()
s = fg.add_subplot(ss[0,:])
s2 = fg.add_subplot(ss[1,0])#2,1,2) 
s3 = fg.add_subplot(ss[1,1])#2,1,3)
s4 = fg.add_subplot(ss[2,0])#2,1,3)
s5 = fg.add_subplot(ss[2,1])#2,1,3)

x = []
y = []
yb1 = []
yb2 = []
yb3 = []
yb4 = []


l = Label(t)
l.pack()
l2 = Label(t)
l2.pack()
l3 = Label(t)
l3.pack()
l4 = Label(t)
l4.pack()
l5 = Label(t)
l5.pack()


def cpu(ys,sb,e,x,i,c,ll) :
     yss = cpu_percent(interval=0.1,percpu=True)
     ys.append(yss[e])
     sb.clear()
     sb.plot(x,ys,c)
     sb.set_ylim(0,100)
     sb.set_ylabel("cpu ")
     sb.text(i/2,80,"cpu "+format(e+1))
     if i > 100 : 
          del(ys[0])
     print("  \n",yss)  
     ll.configure(text=" cpu "+format(e+1)+" : "+format(yss[e])+"%")
          
    
def animate(i) :
    global x , y
    ss = virtual_memory()
    yy = ss.percent
    y.append(yy)
    x.append(i)
   # yyb = cpu_percent(percpu=True)
   # yb1.append(yyb[0]) 
    #sleep(1)
    s.clear()
    s.plot(x,y)
    s.set_ylim(0,100)
    s.set_xlabel("time")
    s.set_ylabel("memory")
   # s2.clear()
   # s2.plot(x,yb,"g")
   # s2.set_ylim(0,yyb[0]+20)
   # s2.set_ylabel("cpu 1 ")
    cpu(yb1,s2,0,x,i,"g",l2)
    cpu(yb2,s3,1,x,i,"r",l3)
    cpu(yb3,s4,2,x,i,"y",l4)
    cpu(yb4,s5,3,x,i,"b",l5)
   
    if i > 100 : 
         del(y[0])
         del(x[0])
    l.configure(text=" memoire : "+format(yy)+"%  temps : "+format(i)+" s ")
    #l2.configure(text=" cpu 1 : "+format(yyb[0])+"% ")
   




a = animation.FuncAnimation(fg,animate,frames=20000)

p.show()

t.mainloop()