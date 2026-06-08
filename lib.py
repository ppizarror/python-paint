#Archivo que carga todas las librerias
#Inclusion de funciones globales

from Tkinter import *
from tkFileDialog import *


try:
    import winsound
except:
    import dummySound as winsound

ERRORS = [["Error no se encuentra en libreria",\
           "Error al cargar archivo de configuraciones!",\
           "Error al crear ventana, faltan archivos y/o el programa esta corrupto",\
           "El programa no puede iniciar"]]

class lib:
    def __init__(self,method,type=False,data=[0,0]):
        if method=="sonido": self.sonido(type)
        if method=="conf_file": self.generarArchivoConfiguraciones(data[0], data[1])
        if method=="error": self.error(type, data[0])

    def sonido(self,tipo):
        if tipo=="alerta": winsound.MessageBeep(-1)
        if tipo=="minimo": winsound.MessageBeep(0)
        if tipo=="fatal": winsound.MessageBeep(16)
        if tipo=="alerta": winsound.MessageBeep(48)
        if tipo=="exception": winsound.MessageBeep(64)

    def error(self,typeError,messageError):
        if typeError=="kernel":
            pre = "ERROR [kernel exception 0x"+str(messageError).zfill(3)+"] "
            it = 0
        elif typeError == "paint":
            pre = "ERROR [paint error 0x"+str(messageError).zfill(3)+"] "
            it = 1
        else:
            return
        try:
            print pre+ERRORS[it][messageError]
        except:
            lib("error","kernel",[0])

    def generarArchivoConfiguraciones(self,name,C_DATA):
        archivo = open(name,"w")
        archivo.write("#Configuracion de Paint\n")
        archivo.write("#No configure nada si no sabe lo que hace\n")
        archivo.write("#Cualquier error en este archivo puede traer consecuencias\n")
        archivo.write("#Fatales a la hora de ejecutar el programa\n\n")
        archivo.write("#Tamano del programa en ancho y largo\n")
        archivo.write("PROGRAMSIZE = "+str(C_DATA[0][0])+","+str(C_DATA[0][1])+"\n\n")
        archivo.write("#Color de la herramienta por defecto\n")
        archivo.write("DEFAULT_COLOR = "+str(C_DATA[1])+"\n\n")
        archivo.write("#Color de la goma por defecto\n")
        archivo.write("DEFAULT_GOMA = "+str(C_DATA[2])+"\n\n")
        archivo.write("#Color del fondo por defecto\n")
        archivo.write("DEFAULT_FONDO = "+str(C_DATA[3])+"\n\n")
        archivo.write("#Estilo de la herramienta por defecto\n")
        archivo.write("DEFAULT_ESTILO_HERRAMIENTA ="+str(C_DATA[4][0])+","+str(C_DATA[4][1])+",["+str(C_DATA[4][2][0])+","+str(C_DATA[4][2][1])+"],"+\
                      str(C_DATA[4][3])+",\""+C_DATA[4][4]+"\"\n\n")
        archivo.write("#Grosor de la herramienta por defecto\n")
        archivo.write("DEFAULT_GROSOR_HERRAMIENTA = "+str(C_DATA[5])+"\n\n")
        archivo.write("#Herramienta por defecto\n")
        archivo.write("DEFAULT_HERRAMIENTA = "+str(C_DATA[6])+"\n\n")
        archivo.write("#Idioma por defecto\n")
        archivo.write("DEFAULT_LANGUAGE = "+str(C_DATA[7])+"\n\n")
        archivo.flush()
