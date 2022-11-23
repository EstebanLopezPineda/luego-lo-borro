import _tkinter
from tkinter import *


#ventana base
base=Tk()
base.geometry("400x650")
base.title("Lista de tareas")
base.resizable(False,False)
#base.iconbitmap('C:/Users/Esteban Lopez/Downloads/Kirb.ico')


#lista principal
lista=[]


#agregar tarea
def addTask():
    tarea= entrartarea.get()
    if tarea != "":
        cajatareas.insert(END, tarea)
        entrartarea.delete(0, END)



#borrar tarea
def borrartarea():
    global lista
    tarea = cajatareas.curselection()
    cajatareas.delete(tarea)
    


#Relacionar archivo .txt con el codigo
def openTaskFile():
    #cracion de archivo
    try:
        global lista
        with open("Texto.txt","r") as taskfile:
            tareas= taskfile.readlines()

        for tarea in tareas:
             if tarea != '\n' :
               lista.append(tareas)
               cajatareas.insert(END,tareas)
    except:
      file=open("Texto.txt","w")
      file.close()



#color del fondo
base.config(background="old lace")


#titulo dentro de la ventana
titulo=Label(base,text="Tus tareas son: ", font="Times 20", fg="black", bg= "floral white")
titulo.pack(fill=X)

#entry de tareas
frame=Frame(base,width=400,height=50, bg="gold3")
frame.pack(fill=X)
tarea=str()
entrartarea=Entry(frame,width=180,font="Courier 20", bd=0)
entrartarea.place(x=5, y=7)
entrartarea.focus()


#Boton de agregar tareas
boton=Button(frame,text="Nueva",font="arial 20 bold",width=6,bg="dark goldenrod",fg="floral white", bd=0,command=addTask)
boton.place(x=300, y=0)

   
#configuracion de barra de scroll
frame1=Frame(base,bd=3,width=700,height=280, bg="gold3")
frame1.pack(pady=(60,0))
cajatareas=Listbox(frame1, font=("Times",12),width=40,height=16,bg="old lace", fg="Black", cursor="hand2",selectbackground="goldenrod3")
cajatareas.pack(side=LEFT,fill=BOTH,padx=2)
barrascroll=Scrollbar(frame1)
barrascroll.pack(side=RIGHT,fill=BOTH)
cajatareas.config(yscrollcommand=Scrollbar.set)
barrascroll.config(command=cajatareas.yview)


#Boton borrar tareas
openTaskFile()
borrar=Button(base,text="Borrar",fg="floral white",bg="dark goldenrod",font="arial 20 bold",bd=0,command=borrartarea)
borrar.pack(side=BOTTOM,pady=1)


#cerrar loop principal
base.mainloop()