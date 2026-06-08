#Core
#Autor: Pablo Pizarro
#SE: PyDev for Eclipse

#Importacion de bibliotecas
from lib import *
from pyv import *


#Funciones intrinsecas de Paint
def isNumerable(x):
    if x.strip().isdigit():
        return True
    else:
        return False

#Constantes de carpetas
DATAFOLDER = "Data/"
DATASAVES = DATAFOLDER+"saves/"
DATADOCS = DATAFOLDER+"docs/"
DATALANG = DATAFOLDER+"langs/"
DATAICONS = DATAFOLDER+"icons/"

#Informacion del programa
VERSION = 5.0,1.0
AUTOR = "Pablo Pizarro"
AUTORMAIL = "pablopizarro9@gmail.com"
PROGRAMTITLE = "Paint"

#Archivo de configuracion por defecto
CONFIGURATIONFILE = PROGRAMTITLE+".ini"

#Configuraciones por defecto
C_DATA = [[800,500],"#000000","#FFFFFF","#FFFFFF",[5,5,[1,1],0,"miter"],20,3,"ES"]

#Carga de las configuraciones y actualizacion de C_DATA
try:
    conf_file = open(CONFIGURATIONFILE,"r")
    for i in conf_file:
        i = i.strip()
        c_command = i.split("=")
        if c_command[0].strip()=="PROGRAMSIZE":
            c_after_command = str(c_command[1]).split(",")
            if isNumerable(c_after_command[0]): C_DATA[0][0]=int(c_after_command[0])
            if isNumerable(c_after_command[1]): C_DATA[0][1]=int(c_after_command[1])
        if c_command[0].strip()=="DEFAULT_COLOR": C_DATA[1]=str(c_command[1]).upper().strip()
        if c_command[0].strip()=="DEFAULT_GOMA": C_DATA[2]=str(c_command[1]).upper().strip()
        if c_command[0].strip()=="DEFAULT_FONDO": C_DATA[3]=str(c_command[1]).upper().strip()
        if c_command[0].strip()=="DEFAULT_ESTILO_HERRAMIENTA":
            c_after_command = (c_command[1].strip().replace("[","").replace("]","")).split(",")
            if isNumerable(c_after_command[0]): C_DATA[4][0] = int(c_after_command[0])
            if isNumerable(c_after_command[1]): C_DATA[4][1] = int(c_after_command[1])
            if isNumerable(c_after_command[2]): C_DATA[4][2][0] = int(c_after_command[2])
            if isNumerable(c_after_command[3]): C_DATA[4][2][1] = int(c_after_command[3])
            if isNumerable(c_after_command[4]): C_DATA[4][3] = int(c_after_command[4])
            if len(c_after_command[5])>0 and (c_after_command[5]=="miter" or c_after_command[5]=="bevel" or c_after_command[5]=="round"):
                C_DATA[4][4] = c_after_command[5].replace("\"","").lower()
        if c_command[0].strip()=="DEFAULT_GROSOR_HERRAMIENTA":
            if isNumerable(c_command[1]): C_DATA[5]=int(c_command[1])
        if c_command[0].strip()=="DEFAULT_HERRAMIENTA":
            if isNumerable(c_command[1]): C_DATA[6]=int(c_command[1])
        if c_command[0].strip()=="DEFAULT_LANGUAGE":
            C_DATA[7]=str(c_command[1]).strip().upper()
    conf_file.close()
except:
    lib("error","kernel",[1])
    lib("sonido","fatal")
    try:
        lib("conf_file",False,[CONFIGURATIONFILE,C_DATA])
        print "IO/MESSAGE: Generado nuevo archivo de configuraciones"
    except:
        print "ERROR - 0,1: No se puede crear archivo de configuraciones"

#Constantes de configuracion predefinidas
DEFAULT_TITLE = "PaintSav"
DEFAULT_EXTENSION = ".is"

#Constantes de configuracion variables
PROGRAMSIZE = C_DATA[0]
DEFAULT_COLOR = C_DATA[1]
DEFAULT_GOMA = C_DATA[2]
DEFAULT_FONDO = C_DATA[3]
DEFAULT_ESTILO_HERRAMIENTA = C_DATA[4]
DEFAULT_GROSOR_HERRAMIENTA = C_DATA[5]
DEFAULT_HERRAMIENTA = C_DATA[6]

#Clase paint
class Paint:

    #Constructor
    def __init__(self):

        try:
            #Variables de dibujo
            self.pos = [[0,0],[0,0]]
            self.activeFigura = 0
            self.vertices = 0
            self.pointable = []
            self.befpoint = [0,0]
            self.title = DEFAULT_TITLE
            self.activeherramienta = DEFAULT_HERRAMIENTA
            self.activecolor = DEFAULT_COLOR
            self.backgroundcolor = DEFAULT_COLOR
            self.colorgoma = DEFAULT_GOMA
            self.grosorHerramienta = DEFAULT_GROSOR_HERRAMIENTA
            self.estiloHerramienta = [DEFAULT_ESTILO_HERRAMIENTA[0],DEFAULT_ESTILO_HERRAMIENTA[1],DEFAULT_ESTILO_HERRAMIENTA[2],\
                                      DEFAULT_ESTILO_HERRAMIENTA[3],DEFAULT_ESTILO_HERRAMIENTA[4]]
            self.dibujado = False
            self.mainArchive = ""

            #Creacion de ventana
            self.main = Tk()
            self.main.focus_force()
            self.main.geometry('%dx%d+%d+%d' % (PROGRAMSIZE[0], PROGRAMSIZE[1], (self.main.winfo_screenwidth() - PROGRAMSIZE[0])/2,\
                                                 (self.main.winfo_screenheight() - PROGRAMSIZE[1])/2))
            self.main.title(PROGRAMTITLE)
            self.main.iconbitmap(DATAICONS+"coloricon.ico")
            self.main.minsize(PROGRAMSIZE[0], PROGRAMSIZE[1])
            self.main.resizable(width=False, height=False)

            #Eventos de ventana
            self.main.bind("<Control-S>",self.salir)
            self.main.bind("<Control-s>",self.salir)
            self.main.bind("<Control-N>",self.nuevaImagen)
            self.main.bind("<Control-n>",self.nuevaImagen)
            self.main.bind("<Control-g>",self.guardarImagen)
            self.main.bind("<Control-G>",self.guardarImagen)
            self.main.bind("<Control-a>",self.ayuda)
            self.main.bind("<Control-A>",self.ayuda)
            self.main.bind("<Control-i>",self.menuInsertarFigura)
            self.main.bind("<Control-I>",self.menuInsertarFigura)

            #Menu
            menubar = Menu(self.main)
            self.main.config(menu=menubar)

            #Archivo
            archivomenu = Menu(menubar,tearoff=0)
            archivomenu.add_command(label="Nuevo    [Ctrl-N]",command=self.nuevaImagen)
            archivomenu.add_command(label="Guardar    [Ctrl-G]",command=self.guardarImagen)
            archivomenu.add_separator()
            archivomenu.add_command(label="Salir    [Ctrl-S]",command=self.salir)
            menubar.add_cascade(label="Archivo",menu=archivomenu)

            #Opciones
            opcionesmenu = Menu(menubar,tearoff=0)
            colormenu = Menu(opcionesmenu,tearoff=0)
            opcionesmenu.add_cascade(label="Cambiar color",menu=colormenu)
            colormenu.add_command(label="De fondo",command=lambda:self.cambiarColor("fondo"))
            colormenu.add_command(label="De la goma",command=lambda:self.cambiarColor("goma"))
            colormenu.add_command(label="Principal",command=lambda:self.cambiarColor("activo"))
            opcionesmenu.add_command(label="Estilo de la herramienta",command=self.cambiarEstiloHerramienta)
            opcionesmenu.add_command(label="Grosor de la Herramienta",command=self.cambiarGrosorHerramienta)
            menubar.add_cascade(label="Opciones",menu=opcionesmenu)

            #Insertar
            insertarmenu = Menu(menubar,tearoff=0)
            insertarmenu.add_command(label="Arco",command= lambda: self.crearFigura("arco"))
            insertarmenu.add_command(label="Cuadrado",command= lambda: self.crearFigura("cuadrado"))
            insertarmenu.add_command(label="Imagen",command= lambda: self.crearFigura("imagen"))
            insertarmenu.add_command(label="Ovalo",command= lambda: self.crearFigura("ovalo"))
            insertarmenu.add_command(label="Poligono",command= lambda: self.crearFigura("poligono"))
            insertarmenu.add_command(label="Recta",command= lambda: self.crearFigura("recta"))
            insertarmenu.add_command(label="Texto",command= lambda: self.crearFigura("texto"))
            menubar.add_cascade(label="Insertar",menu=insertarmenu)

            #Herramientas
            herrammenu = Menu(menubar,tearoff=0)
            hmenu = Menu(herrammenu,tearoff=0)
            hmenu.add_command(label="Goma de Borrar",command=lambda:self.herramienta("goma"))
            hmenu.add_command(label="Lapiz",command=lambda:self.herramienta("lapiz"))
            hmenu.add_command(label="Plumon Fino",command=lambda:self.herramienta("plumonf"))
            hmenu.add_command(label="Plumon Grueso",command=lambda:self.herramienta("plumong"))
            menubar.add_cascade(label="Herramientas",menu=hmenu)

            #Ayuda
            ayudamenu = Menu(menubar,tearoff=0)
            ayudamenu.add_command(label="Acerca de",command=self.acercade)
            ayudamenu.add_command(label="Ayuda    [Ctrl-A]",command=self.ayuda)
            ayudamenu.add_command(label="Changelog",command=self.changelog)
            ayudamenu.add_command(label="Licencia",command=self.licence)
            menubar.add_cascade(label="Ayuda",menu=ayudamenu)

            #Plano de dibujo
            ParentFrame = Frame(self.main)
            ParentFrame.pack()

            #Canvas de dibujo
            ventanaframe = Frame(ParentFrame)
            ventanaframe.pack(side=LEFT)
            self.pantalla = Canvas(ventanaframe,width=PROGRAMSIZE[0]*0.8, height=PROGRAMSIZE[1],bg=DEFAULT_FONDO)
            self.pantalla.pack()

            #Botones
            Buttonframe = Frame(ParentFrame,border=5)
            Buttonframe.pack()
            Label(Buttonframe,text="Herramientas",border=10).pack()
            Button(Buttonframe,text="Goma de Borrar",relief=GROOVE,width=20,command=lambda:self.herramienta("goma")).pack()
            Button(Buttonframe,text="Lapiz",relief=GROOVE,width=20,command=lambda:self.herramienta("lapiz")).pack()
            Button(Buttonframe,text="Plumon Fino",relief=GROOVE,width=20,command=lambda:self.herramienta("plumonf")).pack()
            Button(Buttonframe,text="Plumon Grueso",relief=GROOVE,width=20,command=lambda:self.herramienta("plumong")).pack()
            Button(Buttonframe,text="Insertar Objeto",relief=GROOVE,width=20,command=self.menuInsertarFigura).pack()

            #Informacion de la herramientas
            Label(Buttonframe,text="Herramienta",border=10).pack()
            GrosorLapiz = Frame(Buttonframe)
            GrosorLapiz.pack()
            self.infogrosorlapiz = Label(GrosorLapiz,text=str(self.grosorHerramienta),border=3,font=10,width=2)
            self.infogrosorlapiz.pack(side=LEFT)
            Label(GrosorLapiz,text="  ").pack(side=LEFT)
            Button(GrosorLapiz,text="Grosor",relief=GROOVE,command=self.cambiarGrosorHerramienta,width=9).pack()
            EstiloLapiz = Frame(Buttonframe)
            EstiloLapiz.pack()
            Label(EstiloLapiz,text=" ",border=3,font=10,width=2).pack(side=LEFT)
            Label(EstiloLapiz,text="  ").pack(side=LEFT)
            Button(EstiloLapiz,text="Estilo",relief=GROOVE,command=self.cambiarEstiloHerramienta,width=9).pack()

            #Informaciones color
            Label(Buttonframe,text="Colores",border=10).pack()
            ActiveColor = Frame(Buttonframe)
            ActiveColor.pack()
            self.infoactivedcolor = Canvas(ActiveColor,width=30,height=20,bg=self.activecolor)
            self.infoactivedcolor.pack(side=LEFT)
            Button(ActiveColor,text="Color principal",relief=FLAT,command=lambda:self.cambiarColor("activo"),width=10).pack()
            ActiveColor = Frame(Buttonframe)
            ActiveColor.pack()
            self.infoactivedbackgroundcolor = Canvas(ActiveColor,width=30,height=20,bg=self.backgroundcolor)
            self.infoactivedbackgroundcolor.pack(side=LEFT)
            Button(ActiveColor,text="Color de fondo",relief=FLAT,command=lambda:self.cambiarColor("fondo"),width=10).pack()
            ActiveColor = Frame(Buttonframe)
            ActiveColor.pack()
            self.infoactivedcolorgoma = Canvas(ActiveColor,width=30,height=20,bg=self.colorgoma)
            self.infoactivedcolorgoma.pack(side=LEFT)
            Button(ActiveColor,text="Color goma ",relief=FLAT,command=lambda:self.cambiarColor("goma"),width=10).pack()

            #Informacion para el usuario
            Label(Buttonframe,height=1).pack()
            self.messageUser = Label(Buttonframe,text="",relief=GROOVE,width=30,height=10,justify=CENTER,wraplength=125)
            self.messageUser.pack()

            #Inicializacion de funciones indev
            self.herramienta(self.activeherramienta)
            self.pantalla.bind("<ButtonRelease-1>",self.posPuntero)

            #Se crea la ventana
            self.main.mainloop(0)

        except:
            lib("error","kernel",[2])
            lib("error","kernel",[3])

    #Dibujar en forma 'libre'
    def freeDraw(self,event):
        if self.activeherramienta==1 or self.activeherramienta==3 or self.activeherramienta==4:
            colorpaint = self.activecolor
        if self.activeherramienta==2:
            colorpaint = self.colorgoma
        if self.grosorHerramienta==1:
            if self.befpoint==[0,0]:
                self.befpoint = [event.x,event.y]
            self.pantalla.create_line(event.x,event.y,self.befpoint[0]+self.estiloHerramienta[0]-DEFAULT_ESTILO_HERRAMIENTA[0],self.befpoint[1]+\
                                  self.estiloHerramienta[1]-DEFAULT_ESTILO_HERRAMIENTA[1], dash=self.estiloHerramienta[2],\
                                  width=self.grosorHerramienta,fill=colorpaint,smooth=self.estiloHerramienta[3])
            self.befpoint = [event.x,event.y]
        else:
            if self.activeherramienta==3:
                self.pantalla.create_rectangle(event.x,event.y,event.x+self.estiloHerramienta[0],event.y+\
                                  self.estiloHerramienta[1],dash=self.estiloHerramienta[2],\
                                  width=self.grosorHerramienta,fill=colorpaint,outline = colorpaint)
            elif self.activeherramienta==4:
                self.pantalla.create_oval(event.x,event.y,event.x+self.estiloHerramienta[0],event.y+\
                                  self.estiloHerramienta[1],dash=self.estiloHerramienta[2],\
                                  width=self.grosorHerramienta,fill=colorpaint,outline = colorpaint)
            else:
                self.pantalla.create_line(event.x,event.y,event.x+self.estiloHerramienta[0],event.y+\
                                  self.estiloHerramienta[1],dash=self.estiloHerramienta[2],\
                                  width=self.grosorHerramienta,fill=colorpaint,smooth=self.estiloHerramienta[3])
        self.dibujado = True

    #Nueva imagen
    def nuevaImagen(self,i="null"):
        if self.dibujado:
            resp = pyv("Guardar",DATAICONS+"alert.ico","deseaGuardar",(250,80))
            resp.root.mainloop(1)
            if resp.value!=0:
                if resp.value: self.guardarImagen()
        self.messageUser.config(text="")
        self.pantalla.create_rectangle(0,0,2*PROGRAMSIZE[0], 2*PROGRAMSIZE[1],fill=DEFAULT_FONDO)
        self.dibujado = False

    #Guardar imagen
    def guardarImagen(self,i="null"):
        if self.dibujado:
            self.pantalla.update()
            txt = pyv("Guardar",DATAICONS+"save.ico","guardar",(250,110))
            txt.root.mainloop(1)
            if txt.value!=0:
                self.pantalla.postscript(file=DATASAVES+str(txt.value)+DEFAULT_EXTENSION)
                self.dibujado = False
            else:
                self.pantalla.postscript(file=DATASAVES+DEFAULT_TITLE+DEFAULT_EXTENSION)
                self.dibujado = False


    #Salir de programa
    def salir(self,i="null"):
        if self.dibujado:
            resp = pyv("Guardar",DATAICONS+"alert.ico","deseaGuardar",(250,80))
            resp.root.mainloop(1)
            if resp.value!=0:
                if resp.value: self.guardarImagen()
        self.main.destroy()

    #Cambiar el color de la herramienta    - activo, goma
    def cambiarColor(self,herramienta):
        a = pyv("Cambiar color",DATAICONS+"color.ico","cambiarcolor",(280,440))
        a.root.mainloop(1)
        if a.value!=0:
            if herramienta=="activo":
                self.activecolor = a.value
                self.infoactivedcolor.config(bg=self.activecolor)
            if herramienta=="goma":
                self.colorgoma = a.value
                self.infoactivedcolorgoma.config(bg=self.colorgoma)
            if herramienta=="fondo":
                self.backgroundcolor = a.value
                self.infoactivedbackgroundcolor.config(bg=self.backgroundcolor)

    #Cambiar grosor de la herramienta
    def cambiarGrosorHerramienta(self):
        a = pyv("Grosor Herramienta",DATAICONS+"grosor.ico","grosor",(260,450))
        a.root.mainloop(1)
        if a.value!=0:
            self.grosorHerramienta = a.value
            self.infogrosorlapiz.config(text=str(a.value))

    #Cambiar estilo de la herramienta
    def cambiarEstiloHerramienta(self):
        a = pyv("Estilo de la Herramienta",DATAICONS+\
                "estilo.ico","estilo",(260,210),[self.estiloHerramienta[0],self.estiloHerramienta[1],\
                                                 self.estiloHerramienta[2],self.estiloHerramienta[3],\
                                                 self.estiloHerramienta[4],[DEFAULT_ESTILO_HERRAMIENTA[0],\
                                                                            DEFAULT_ESTILO_HERRAMIENTA[1],\
                                                                            DEFAULT_ESTILO_HERRAMIENTA[2],\
                                                                            DEFAULT_ESTILO_HERRAMIENTA[3],\
                                                                            DEFAULT_ESTILO_HERRAMIENTA[4]]])
        a.root.mainloop(1)
        self.estiloHerramienta[0] = a.estiloValues[0]
        self.estiloHerramienta[1] = a.estiloValues[1]
        self.estiloHerramienta[2] = a.estiloValues[2]
        self.estiloHerramienta[3] = a.estiloValues[3]
        self.estiloHerramienta[4] = a.estiloValues[4]

    #Insertar figuras
    def menuInsertarFigura(self,E=False):
        a = pyv("Insertar Figura",DATAICONS+"shaperound.ico","insertarfigura",(260,230))
        a.root.mainloop(1)
        self.crearFigura(a.value)

    #Retornar la posicion del mouse en dos posiciones y crear alguna figurilla
    def callbackPos(self,event):
        if self.pos[0]==[0,0]:
            self.pos[0][0]=event.x
            self.pos[0][1]=event.y
        else:
            self.pos[1][0]=event.x
            self.pos[1][1]=event.y
            if self.activeFigura==1:
                self.pantalla.create_rectangle(self.pos[0][0],self.pos[0][1],self.pos[1][0],self.pos[1][1],\
                                               fill=self.backgroundcolor,outline=self.activecolor)
            if self.activeFigura==2:
                self.pantalla.create_oval(self.pos[0][0],self.pos[0][1],self.pos[1][0],self.pos[1][1],\
                                          fill=self.backgroundcolor,outline=self.activecolor)
            if self.activeFigura==3:
                self.pantalla.create_line(self.pos[0][0],self.pos[0][1],self.pos[1][0],self.pos[1][1],\
                                          fill=self.backgroundcolor,width=self.grosorHerramienta)
            if self.activeFigura==5:
                a = pyv("Crear arco",DATAICONS+"arc.ico","arco",(260,115))
                self.messageUser.config(text="Ingrese los grados de su arco, 0 para cancelar")
                a.root.mainloop(1)
                if a.value>0:
                    self.pantalla.create_arc(self.pos[0][0],self.pos[0][1],self.pos[1][0],self.pos[1][1],\
                                               fill=self.backgroundcolor,outline=self.activecolor, extent=a.value)
            self.dibujado = True
            self.pantalla.bind("<ButtonPress-1>",self.breakpoint)
            self.herramienta(self.activeherramienta)
            self.pos=[[0,0],[0,0]]
            self.messageUser.config(text="")

    #Crear un poligono
    def crearPoligono(self,event):
        if self.vertices>0:
            self.messageUser.config(text="Haga click en la pantalla para definir los vertices de su figura, "+str(self.vertices-1)+" restantes")
            self.vertices-=1
            self.pointable.append([event.x,event.y])
        if self.vertices==0:
            self.pantalla.create_polygon(self.pointable,fill=self.backgroundcolor,outline=self.activecolor)
            self.pointable=[]
            self.herramienta(self.activeherramienta)
            self.pantalla.bind("<ButtonPress-1>",self.breakpoint)
            self.messageUser.config(text="")
            self.dibujado = True

    #Insertar un texto
    def crearTexto(self,event):
        txt = pyv("Ingresar un texto",DATAICONS+"text.ico","insertartexto",(250,110))
        txt.root.mainloop(1)
        self.messageUser.config(text="")
        self.pantalla.create_text(event.x,event.y,text=txt.value,font="Arial")
        self.pantalla.bind("<ButtonPress-1>",self.breakpoint)
        self.dibujado = True

    #Crear una figura
    def crearFigura(self,figura):
        if figura=="cuadrado":
            self.pantalla.bind("<ButtonPress-1>",self.callbackPos)
            self.pantalla.bind("<B1-Motion>",self.breakpoint)
            self.activeFigura = 1
            self.messageUser.config(text="Haga click en dos puntos del dibujo para crear un cuadrado")
        if figura=="ovalo":
            self.pantalla.bind("<ButtonPress-1>",self.callbackPos)
            self.pantalla.bind("<B1-Motion>",self.breakpoint)
            self.activeFigura = 2
            self.messageUser.config(text="Haga click en dos puntos del dibujo para crear un ovalo")
        if figura=="recta":
            self.pantalla.bind("<ButtonPress-1>",self.callbackPos)
            self.pantalla.bind("<B1-Motion>",self.breakpoint)
            self.messageUser.config(text="Haga click en dos puntos del dibujo para crear una recta")
            self.activeFigura = 3
        if figura=="texto":
            self.pantalla.bind("<ButtonPress-1>",self.crearTexto)
            self.messageUser.config(text="Haga click en el dibujo para poner su texto")
        if figura=="arco":
            self.pantalla.bind("<ButtonPress-1>",self.callbackPos)
            self.pantalla.bind("<B1-Motion>",self.breakpoint)
            self.activeFigura = 5
            self.messageUser.config(text="Haga click en dos puntos del dibujo para definir los limites de su arco")
        if figura=="imagen":
            self.messageUser.config(text="Ingrese la ubicacion de su imagen")
            file = askopenfilename(title="Abrir",initialdir="C:/",defaultextension=".gif",filetypes=[("GIF",".gif")])
            self.messageUser.config(text="")
            if file!="" and (file[len(file)-4:len(file)]==".gif" or file[len(file)-4:len(file)]==".GIF"):
                self.mainArchive=file
                self.pantalla.bind("<ButtonPress-1>",self.insertarImagen)
                self.pantalla.bind("<B1-Motion>",self.breakpoint)
                self.messageUser.config(text="Haga click en un punto del dibujo para insertar su imagen, ESC para terminar")
                self.main.bind("<Escape>",self.terminarImagen)
        if figura =="poligono":
            a = pyv("Numero de aristas",DATAICONS+"shaperound.ico","vertices",(260,115))
            self.messageUser.config(text="Ingrese el numero de aristas que tendra su nueva figura, 0 para cancelar")
            a.root.mainloop(1)
            self.activeFigura = 4
            self.vertices = a.value
            if self.vertices>0:
                self.pantalla.bind("<ButtonPress-1>",self.crearPoligono)
                self.pantalla.bind("<B1-Motion>",self.breakpoint)
                self.messageUser.config(text="Haga click en la pantalla para definir los vertices de su figura, "+str(self.vertices)+" restantes")
            else:
                self.messageUser.config(text="")

    #Cargar una herramienta - goma, lapiz, plumon
    def herramienta(self,herr):
        if herr=="lapiz" or herr==1: self.activeherramienta=1
        if herr=="goma" or herr==2: self.activeherramienta=2
        if herr=="plumong" or herr==3: self.activeherramienta=3
        if herr=="plumonf" or herr==4: self.activeherramienta=4
        self.pantalla.bind("<B1-Motion>",self.freeDraw)

    #Cargar una ventana con ayudas
    def ayuda(self,i="null"):
        a = pyv("Ayuda",DATAICONS+"help.ico","ayuda",(600,400),[PROGRAMTITLE,DATADOCS+"AYUDA.TXT"])
        a.root.mainloop(0)

    #Insertar una imagen
    def insertarImagen(self,event):
        imagen = PhotoImage(file=self.mainArchive)
        self.pantalla.create_image(event.x,event.y,image=imagen)
        self.pantalla.update()
        imagen.name=None

    #Terminar de poner las imagenes
    def terminarImagen(self,i):
        self.messageUser.config(text="")
        self.pantalla.bind("<B1-Motion>",self.freeDraw)
        self.pantalla.bind("<ButtonPress-1>",self.breakpoint)
        self.mainArchive=""
        self.main.bind("<Escape>",self.breakpoint)

    #Cargar el acercade
    def acercade(self,i="null"):
        a = pyv("Acerca de "+PROGRAMTITLE,DATAICONS+"coloricon.ico","about",(220,120),[AUTOR,VERSION[0],AUTORMAIL])
        a.root.mainloop(0)

    #Posicionar puntero
    def posPuntero(self,event):
        self.befpoint=[0,0]

    #Lista de cambios del programa
    def changelog(self):
        a = pyv("Changelog",DATAICONS+"changelog.ico","changelog",(600,400),[PROGRAMTITLE,DATADOCS+"CHANGELOG.TXT"])
        a.root.mainloop(0)

    #Licencia del programa
    def licence(self):
        a = pyv("Licencia GNU [English]",DATAICONS+"gnu.ico","licence",(600,400),[PROGRAMTITLE,DATADOCS+"GNU.TXT"])
        a.root.mainloop(0)

    #Funcion para salir
    def breakpoint(self,breakeable):
        return

#Se carga la clase Paint
Paint()