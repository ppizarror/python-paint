#Archivo creador de ventanas
#Autor: Pablo Pizarro
#SE: PyDev for Eclipse

#Importacion de bibliotecas
from lib import *


#Definicion de variables importantes
DEFAULT_FONT_TITLE="Arial",10
DEFAULT_WIDTH_CANVASTREE = 38,30

#Funcion que retorna un valor booleano si x esta entre a,b [x,y]
def valorEntre(num,x,y):
    if (num>=x) and (num<=y): return True
    else: return False
    
#Clase creadora de ventanas 
class pyv:
    
    #Clase constructora
    def __init__(self,title,icon,tipo,tamano,properties=[0,0,0,0,0]):
        self.value = 0
        self.root = Tk()
        self.root.geometry('%dx%d+%d+%d' % (tamano[0], tamano[1], (self.root.winfo_screenwidth() - tamano[0])/2,\
                                             (self.root.winfo_screenheight() - tamano[1])/2))
        self.root.iconbitmap(bitmap=icon)
        self.root.title(title)
        self.root.minsize(width=tamano[0], height=tamano[1])
        self.root.resizable(width=False, height=False)
        
        #Cambiar un color
        if tipo=="cambiarcolor":
            Label(self.root,text="Escoja un color",font=DEFAULT_FONT_TITLE,border=10).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#ff0000").pack(side=LEFT)
            Button(F1_A,text="Rojo",relief=GROOVE,command=lambda:self.putcolor("#FF0000"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#0000FF").pack(side=LEFT)
            Button(F1_B,text="Azul",relief=GROOVE,command=lambda:self.putcolor("#0000FF"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#FFFF00").pack(side=LEFT)
            Button(F1_A,text="Amarillo",relief=GROOVE,command=lambda:self.putcolor("#FFFF00"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#800080").pack(side=LEFT)
            Button(F1_B,text="Morado",relief=GROOVE,command=lambda:self.putcolor("#800080"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#FFC0CB").pack(side=LEFT)
            Button(F1_A,text="Rosado",relief=GROOVE,command=lambda:self.putcolor("#FFC0CB"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#FFA500").pack(side=LEFT)
            Button(F1_B,text="Naranjo",relief=GROOVE,command=lambda:self.putcolor("#FFA500"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#000080").pack(side=LEFT)
            Button(F1_A,text="Azul marino",relief=GROOVE,command=lambda:self.putcolor("#000080"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#ADFF2F").pack(side=LEFT)
            Button(F1_B,text="Verde",relief=GROOVE,command=lambda:self.putcolor("#ADFF2F"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#DDA0DD").pack(side=LEFT)
            Button(F1_A,text="Ciruela",relief=GROOVE,command=lambda:self.putcolor("#DDA0DD"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#FA8072").pack(side=LEFT)
            Button(F1_B,text="Salmon",relief=GROOVE,command=lambda:self.putcolor("#FA8072"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#008000").pack(side=LEFT)
            Button(F1_A,text="Verde Oscuro",relief=GROOVE,command=lambda:self.putcolor("#008000"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#00FF00").pack(side=LEFT)
            Button(F1_B,text="Verde Lima",relief=GROOVE,command=lambda:self.putcolor("#00FF00"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#008080").pack(side=LEFT)
            Button(F1_A,text="Celeste Oscuro",relief=GROOVE,command=lambda:self.putcolor("#008080"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#00FFFF").pack(side=LEFT)
            Button(F1_B,text="Cyan",relief=GROOVE,command=lambda:self.putcolor("#00FFFF"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#808000").pack(side=LEFT)
            Button(F1_A,text="Oliva",relief=GROOVE,command=lambda:self.putcolor("#808000"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#800000").pack(side=LEFT)
            Button(F1_B,text="Marron",relief=GROOVE,command=lambda:self.putcolor("#800000"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#643200").pack(side=LEFT)
            Button(F1_A,text="Marron Claro",relief=GROOVE,command=lambda:self.putcolor("#643200"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#C86400").pack(side=LEFT)
            Button(F1_B,text="Marron Oscuro",relief=GROOVE,command=lambda:self.putcolor("#C86400"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#5E5E5E").pack(side=LEFT)
            Button(F1_A,text="Gris Oscuro",relief=GROOVE,command=lambda:self.putcolor("#5E5E5E"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#D0D0D0").pack(side=LEFT)
            Button(F1_B,text="Gris Claro",relief=GROOVE,command=lambda:self.putcolor("#D0D0D0"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            F1_A = Frame(F1,border=1)
            F1_A.pack(side=LEFT)
            Canvas(F1_A,width=30,height=23,bg="#000000").pack(side=LEFT)
            Button(F1_A,text="Negro",relief=GROOVE,command=lambda:self.putcolor("#000000"),width=13).pack(side=LEFT)
            Label(F1_A,text="",).pack()
            F1_B = Frame(F1,border=1)
            F1_B.pack()
            Canvas(F1_B,width=30,height=23,bg="#ffffff").pack(side=LEFT)
            Button(F1_B,text="Blanco",relief=GROOVE,command=lambda:self.putcolor("#FFFFFF"),width=13).pack()
            
            #Nueva linea de colores
            F1 = Frame(self.root)
            F1.pack()
            Button(F1,text="Color Personalizado",relief=GROOVE,command=self.colorPersonalizado,width=17).pack()
            
            Label(self.root,text="").pack()
            F1 = Frame(self.root,border=4)
            F1.pack()
            self.color=Label(F1,width=10,text="Elija un color")
            self.color.pack(side=LEFT)
            Label(F1,text="     ").pack(side=LEFT)
            enviar = Button(F1,text="Listo",command=self.root.destroy)
            enviar.pack()
        
        #Crear un color
        if tipo=="crearcolor":
            Label(self.root,text="Crear un color (RGB)",font=DEFAULT_FONT_TITLE,border=10).pack()
            
            #Nueva linea de colores
            FA = Frame(self.root)
            FA.pack()
            F = Frame(FA)
            F.pack(side=LEFT)
            F1 = Frame(F)
            F1.pack()       
            Label(F1,text="Rojo [0-255]",width=15,justify=RIGHT).pack(side=LEFT)
            self.R = Entry(F1,width=4)
            self.R.bind("<Key>",self.crearColor)
            self.R.pack()
            
            F2 = Frame(F)
            F2.pack()       
            Label(F2,text="Verde [0-255]",width=15).pack(side=LEFT)
            self.V = Entry(F2,width=4)
            self.V.bind("<Key>",self.crearColor)
            self.V.pack()
            
            F3 = Frame(F)
            F3.pack()       
            Label(F3,text="Azul [0-255]",width=15).pack(side=LEFT)
            self.A = Entry(F3,width=4)
            self.A.bind("<Key>",self.crearColor)
            self.A.pack()
            
            FB = Frame(FA,border=10)
            FB.pack()
            self.paleta = Canvas(FB,width=100,height=70,relief=GROOVE,border=1)
            self.paleta.pack()
            
            Label(self.root,text="").pack()
            FF = Frame(self.root,border=4)
            FF.pack()
            self.color=Label(FF,width=30,text="Elija un color")
            self.color.pack(side=LEFT)
            Label(FF,text="     ").pack(side=LEFT)
            self.enviarb = Button(FF,text="Crear",command=self.root.destroy,state=DISABLED)
            self.enviarb.pack()
            
        #Grosor de las herramientas
        if tipo=="grosor":
            Label(self.root,text="Grosor",font=DEFAULT_FONT_TITLE,border=10).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=1)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 1",relief=GROOVE,command=lambda:self.grosor(1),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=2)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 2",relief=GROOVE,command=lambda:self.grosor(2),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=3)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 3",relief=GROOVE,command=lambda:self.grosor(3),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=4)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 4",relief=GROOVE,command=lambda:self.grosor(4),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=5)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 5",relief=GROOVE,command=lambda:self.grosor(5),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=6)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 6",relief=GROOVE,command=lambda:self.grosor(6),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=7)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 7",relief=GROOVE,command=lambda:self.grosor(7),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=8)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 8",relief=GROOVE,command=lambda:self.grosor(8),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=9)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 9",relief=GROOVE,command=lambda:self.grosor(9),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=10)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 10",relief=GROOVE,command=lambda:self.grosor(10),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=11)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 11",relief=GROOVE,command=lambda:self.grosor(11),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=12)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 12",relief=GROOVE,command=lambda:self.grosor(12),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=13)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 13",relief=GROOVE,command=lambda:self.grosor(13),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+2,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=14)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 14",relief=GROOVE,command=lambda:self.grosor(14),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=15)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 15",relief=GROOVE,command=lambda:self.grosor(15),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+2,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=16)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 16",relief=GROOVE,command=lambda:self.grosor(16),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=17)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 17",relief=GROOVE,command=lambda:self.grosor(17),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+2,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=18)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 18",relief=GROOVE,command=lambda:self.grosor(18),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=19)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 19",relief=GROOVE,command=lambda:self.grosor(19),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+2,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=20)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 20",relief=GROOVE,command=lambda:self.grosor(20),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=21)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 21",relief=GROOVE,command=lambda:self.grosor(21),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+2,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=22)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 22",relief=GROOVE,command=lambda:self.grosor(22),width=7).pack()
            
            #Nueva linea de grosores
            F = Frame(self.root)
            F.pack()
            FA = Frame(F)
            FA.pack(side=LEFT)
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+1,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=23)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 23",relief=GROOVE,command=lambda:self.grosor(23),width=7).pack(side=LEFT)
            Label(FA,text=" ").pack(side=LEFT)
            FA = Frame(F)
            FA.pack()
            F_C=Canvas(FA,width=DEFAULT_WIDTH_CANVASTREE[0],height=DEFAULT_WIDTH_CANVASTREE[1],bg="white")
            F_C.pack(side=LEFT)
            F_C.create_line(0,DEFAULT_WIDTH_CANVASTREE[1]/2+2,DEFAULT_WIDTH_CANVASTREE[0]+2,DEFAULT_WIDTH_CANVASTREE[1]/2+1,width=24)
            Label(FA,text=" ").pack(side=LEFT)
            Button(FA,text="Grosor 24",relief=GROOVE,command=lambda:self.grosor(24),width=7).pack()
            
        if tipo=="estilo":
            self.estiloValues = properties
            Label(self.root,text="Estilo de la herramienta",font=DEFAULT_FONT_TITLE,border=10).pack()
            
            #Nueva linea de colores
            F = Frame(self.root,border=4)
            F.pack()
            F1 = Frame(F)
            F1.pack(side=LEFT)       
            Label(F1,text="X - [X>0]",width=9,justify=RIGHT).pack(side=LEFT)
            self.XPLUS = Entry(F1,width=4)
            self.XPLUS.insert(0, properties[0])
            self.XPLUS.pack()
            F2 = Frame(F)
            F2.pack()       
            Label(F2,text="Y - [Y>0]",width=9,justify=RIGHT).pack(side=LEFT)
            self.YPLUS = Entry(F2,width=4)
            self.YPLUS.insert(0, properties[1])
            self.YPLUS.pack()
            F3 = Frame(self.root,border=4)
            F3.pack()       
            Label(F3,text="DASH [N1,N2..]",width=15,justify=RIGHT).pack(side=LEFT)
            self.DASH = Entry(F3,width=7)
            self.DASH.insert(0, str(properties[2]).replace("[","").replace("]", "").replace(" ",""))
            self.DASH.pack()         
            F4 = Frame(self.root,border=4)
            F4.pack()       
            Label(F4,text="SMOOTH [0,1]",width=15,justify=RIGHT).pack(side=LEFT)
            self.SMOOTH = Entry(F4,width=3)
            self.SMOOTH.insert(0, str(properties[3]))
            self.SMOOTH.pack()          
            F5 = Frame(self.root,border=4)
            F5.pack()       
            Label(F5,text="JOINSTYLE (miter, bevel, round)",width=25,justify=RIGHT).pack(side=LEFT)
            self.JOIN = Entry(F5,width=6)
            self.JOIN.insert(0, str(properties[4]))
            self.JOIN.pack()             
            
            #Boton
            Label(self.root,text="").pack()
            FB = Frame(self.root)
            FB.pack()
            Button(FB,text="Ok",command=self.enviarEstilo).pack(side=LEFT)
            Label(FB,text=" ").pack(side=LEFT)
            Button(FB,text="Restaurar",command=self.restaurarEstilo).pack(side=LEFT)
            self.defaultProperties=[properties[5][0],properties[5][1],properties[5][2],properties[5][3],properties[5][4]]
        
        #Menu insertar figura
        if tipo=="insertarfigura":
            Label(self.root,text="Insertar una figura",font=DEFAULT_FONT_TITLE,border=10).pack()
            Button(self.root, text="Arco",command=lambda:self.enviarFigura("arco"),width=10,relief=GROOVE).pack()
            Button(self.root, text="Cuadrado",command=lambda:self.enviarFigura("cuadrado"),width=10,relief=GROOVE).pack()
            Button(self.root, text="Imagen",command=lambda:self.enviarFigura("imagen"),width=10,relief=GROOVE).pack()
            Button(self.root, text="Ovalo",command=lambda:self.enviarFigura("ovalo"),width=10,relief=GROOVE).pack()
            Button(self.root, text="Poligono",command=lambda:self.enviarFigura("poligono"),width=10,relief=GROOVE).pack()
            Button(self.root, text="Recta",command=lambda:self.enviarFigura("recta"),width=10,relief=GROOVE).pack() 
            Button(self.root, text="Texto",command=lambda:self.enviarFigura("texto"),width=10,relief=GROOVE).pack() 
            
        #Menu insertar figura
        if tipo=="insertartexto":
            Label(self.root,text="Ingresar un texto",font=DEFAULT_FONT_TITLE,border=10).pack()
            self.texto = Entry(self.root)
            self.texto.pack()
            Label(self.root,text=" ").pack()
            Button(self.root, text="Escribir",command=self.enviarTexto,width=10,relief=GROOVE).pack()
            self.texto.focus_force()
            
        #Menu insertar figura
        if tipo=="guardar":
            Label(self.root,text="Escoja un nombre",font=DEFAULT_FONT_TITLE,border=10).pack()
            self.texto = Entry(self.root)
            self.texto.pack()
            Label(self.root,text=" ").pack()
            Button(self.root, text="Guardar",command=self.enviarTexto,width=10,relief=GROOVE).pack()
            self.texto.focus_force()
            
        #Menu numero de vertices
        if tipo=="vertices":
            Label(self.root,text="Numero de vertices",font=DEFAULT_FONT_TITLE,border=10).pack()
            self.numvertices = Entry(self.root)
            self.numvertices.pack()
            Label(self.root,text=" ").pack()
            Button(self.root, text="Continuar",command=self.enviarVertices,width=10,relief=GROOVE).pack()
            self.numvertices.focus_force()
            
        #Menu numero de vertices
        if tipo=="arco":
            Label(self.root,text="Longitud del arco",font=DEFAULT_FONT_TITLE,border=10).pack()
            self.arc = Entry(self.root)
            self.arc.pack()
            Label(self.root,text=" ").pack()
            Button(self.root, text="Continuar",command=self.enviarArco,width=10,relief=GROOVE).pack()
            self.arc.focus_force()
        
        #Menu numero de vertices
        if tipo=="deseaGuardar":
            lib("sonido","alerta")
            Label(self.root,text="Desea Guardar?",font=DEFAULT_FONT_TITLE,border=10).pack()
            F = Frame(self.root)
            F.pack()
            Button(F, text="Si",command=lambda:self.response("si"),width=5,relief=GROOVE).pack(side=LEFT)
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text="No",command=lambda:self.response("no"),width=5,relief=GROOVE).pack()
            
        #About
        if tipo=="about":
            Label(self.root,text="Creador: "+properties[0],font=DEFAULT_FONT_TITLE,border=5).pack()
            Label(self.root,text="Mail: "+properties[2],font=DEFAULT_FONT_TITLE,border=5).pack()
            Label(self.root,text="Version: "+str(properties[1]),font=DEFAULT_FONT_TITLE,border=5).pack()
            Button(self.root, text="Cerrar",command=self.root.destroy).pack()
            
        #Licencia o gnu
        if tipo=="licence" or tipo=="changelog" or tipo=="ayuda":
            archivo = open(properties[1],"r")
            Yscroll = Scrollbar(self.root)
            Yscroll.pack(side=RIGHT, fill=Y)
            texto = Text(self.root,wrap=NONE,
            yscrollcommand=Yscroll.set)
            texto.focus_force()
            for i in archivo: texto.insert(INSERT,i)
            texto.pack()
            texto.configure(state="disabled")
            Yscroll.config(command=texto.yview)
            archivo.close()
        
    #Ingresa colores programados
    def putcolor(self,colorText):
        self.color.config(text=colorText)
        self.value = colorText
        
    #Funcion que envia una respuesta
    def response(self,respuesta):
        if respuesta=="si": self.value = True
        if respuesta=="no": self.value = False
        self.root.destroy()
        
    #Asignar un numero de vertices para dibujar
    def enviarVertices(self):
        num = self.numvertices.get()
        if num.isdigit():
            num = int(num)
            self.value = num
        self.root.destroy()
            
    #Asignar un numero de vertices para dibujar
    def enviarArco(self):
        arc = self.arc.get()
        if arc.isdigit():
            arc = int(arc)
            if arc>0: self.value = arc
        self.root.destroy()
        
    #Enviar un texto
    def enviarTexto(self):
        text = self.texto.get()
        if len(text)>0:
            self.value=text
            self.root.destroy()
        
    #Enviar una figura
    def enviarFigura(self,figura):
        self.value = figura
        self.root.destroy()
        
    #Enviar estilo
    def enviarEstilo(self):
        x = self.XPLUS.get()
        y = self.YPLUS.get()
        dash = self.DASH.get()
        smooth = self.SMOOTH.get()
        join = self.JOIN.get().lower()
        if x.isdigit() and x!="":
            x= int(x)
            if x>0: self.estiloValues[0]=x
        if y.isdigit() and y!="":
            y=int(y)
            if y>0: self.estiloValues[1]=y
        if dash.replace(",","").replace(" ","").isdigit():
            dash = dash.split(",")
            k=0
            j=0
            for i in dash:
                if not valorEntre(int(i),1,255): k+=1
                dash[j]=int(dash[j])
                j+=1
            if k==0: self.estiloValues[2]=dash
        if smooth.isdigit() and smooth!="":
            smooth=int(smooth)
            if valorEntre(smooth,0,1): self.estiloValues[3]=smooth
        if join=="miter" or join=="bevel" or join=="round": self.estiloValues[4]=join       
        self.root.destroy()
        
    #Restaurar el estilo
    def restaurarEstilo(self):
        self.estiloValues[0]=self.defaultProperties[0]
        self.estiloValues[1]=self.defaultProperties[1]
        self.estiloValues[2]=self.defaultProperties[2]
        self.estiloValues[3]=self.defaultProperties[3]
        self.estiloValues[4]=self.defaultProperties[4]
        self.root.destroy()
        
    #Ingresar grosores
    def grosor(self,grosorLine):
        self.value = grosorLine
        self.root.destroy()
    
    #Funcion para crear un color hexadecimal
    def crearColor(self,X):
        r = self.R.get()
        g = self.V.get()
        b = self.A.get()
        if r!="" and g!="" and b!="":
            if r.isdigit() and g.isdigit() and b.isdigit():
                r = int(r)
                g = int(g)
                b = int(b)
                if valorEntre(r,0,255) and valorEntre(g,0,255) and valorEntre(b,0,255):
                    hr = hex(r).replace("0x","").zfill(2)
                    hg = hex(g).replace("0x","").zfill(2)
                    hb = hex(b).replace("0x","").zfill(2)
                    hexcolor = ("#"+hr+hg+hb).upper()
                    self.paleta.config(bg=hexcolor)
                    self.color.config(text=hexcolor)
                    self.value = hexcolor
                    self.enviarb.config(state=NORMAL)
                else:
                    self.enviarb.config(state=DISABLED)
                    self.color.config(text="ERROR, VALORES ENTRE [0,255]")
                    lib("sonido","minimo")
            else:
                self.color.config(text="ERROR, VALORES DEBEN SER DIGITOS")
                lib("sonido","minimo")
                self.enviarb.config(state=DISABLED) 
        else:
            self.enviarb.config(state=DISABLED)
            self.color.config(text="Elija un color")       
        
    #Ingresar color personalizado
    def colorPersonalizado(self):
        colorCreated = pyv("Color Personalizado","Data/Icons/palete.ico","crearcolor",(250,150))
        colorCreated.root.mainloop(2)
        if colorCreated.value!=0: self.putcolor(colorCreated.value)
