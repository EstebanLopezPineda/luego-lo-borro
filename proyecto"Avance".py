import _tkinter
from tkinter import *
base=Tk()
base.geometry("400x650")
base.title("Lista de tareas")
base.resizable(False,False)
base.iconbitmap('C:/Users/Esteban Lopez/Downloads/Kirb.ico')


lista=[]
def addTask():
    tarea= entrartarea.get()
    entrartarea.delete(0,END)

    if tarea:
        with open("Texto.txt","a") as taskfile:
         taskfile.write(f"\n{tarea}")
        lista.append(tarea)
        cajatareas.insert(END, tarea)

#color del fondo
base.config(background="grey")

titulo=Label(base,text="Tus tareas son: ", font="arial 20 bold", fg="black", bg= "green")
titulo.pack(fill=X)


frame=Frame(base,width=400,height=50, bg="grey")
frame.pack(fill=X)
tarea=str()
entrartarea=Entry(frame,width=180,font="arial 20", bd=0)
entrartarea.place(x=5, y=7)
entrartarea.focus()
boton=Button(frame,text="Nueva",font="arial 20 bold",width=6,bg="red",fg="#fff", bd=0,command=addTask)
boton.place(x=300, y=0)




def openTaskFile():
    try:
        global lista
        with open("Texto.txt","r") as taskfile:
            tareas= taskfile.readlines()

        for task in tareas:
             if task != '\n' :
               lista.append(tareas)
               cajatareas.insert(END,tareas)
    except:
      file=open("Texto.txt","w")
      file.close()
    


frame1=Frame(base,bd=3,width=700,height=280, bg="green")
frame1.pack(pady=(60,0))
cajatareas=Listbox(frame1, font=("arial",12),width=40,height=16,bg="white", fg="Black", cursor="hand2",selectbackground="grey")
cajatareas.pack(side=LEFT,fill=BOTH,padx=2)
barrascroll=Scrollbar(frame1)
barrascroll.pack(side=RIGHT,fill=BOTH)
cajatareas.config(yscrollcommand=Scrollbar.set)
barrascroll.config(command=cajatareas.yview)


openTaskFile()
#insertar icono de borrar
Button(base,text="Borrar",bg="red",font="arial 20 bold",bd=0).pack(side=BOTTOM,pady=1)

base.mainloop()
