"""
Title: YoutubeDown
Descripcion: Programa para poder descargar videos de youtube que necesito en mi caso para las clases de inglés ó algún tutorial que me interesa ver más tarde, a una calidad 720p
             para no tener que depender de páginas de internet, que me descarguen los videos con riesgo de que me inserten algun virus o algo peor, y a la vez me sirva para practicar
             python y el uso de la libreria Pytube. 
             Aparte con esto sigo practicando librerias como la de tkinter, la de pillow, etc...
             Está es la versión 1.1 porque la versión 1.0 era sin entorno gráfico, es decir por consola. subido a git
             
Autor: Tomás Rodríguez Garrido 
Version: 1.1

"""
from tkinter.constants import SUNKEN
from pytube import YouTube
from tkinter import Tk, TkVersion, Button, Entry, Label, PhotoImage, Frame
from PIL import Image, ImageTk #pip install Pillow

class YT(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)        
        
        def descarga():
            #print("Hola mundo ")
            dir =self.urlText.get()  #toma la url del supuesto video 
            
            #print(dir)
            self.urlText.delete(0, "end")
            self.statusBar = Label(bd=1, fg="grey",width=55, relief=SUNKEN, anchor='center', text="")
            self.statusBar.grid(column=0,row=1, columnspan=3, pady=5, padx=15)
            
            try:
                v = YouTube(dir)  #creamos el objeto video de youtube
                titulo = str(v.title)
                autor = str(v.author)
                visualizaciones = int(v.views)
                duracion = int(v.length)   #duración del video
                vide = v.vid_info          #me saca un diccionario enorme de datos que tengo que analizar
                vid = str(v.video_id)      #identificador de las busquedas de youtube  0zkX6nlpiSk    
                
                v.streams.get_by_resolution("720p").download()
                
                #aquí tengo que crear un canvas para hacer la barra de progreso
                
                self.statusBar = Label(bd=1, fg="grey",width=55, relief=SUNKEN, anchor='center', text=" * Video de Youtube Descargado * ")
                self.statusBar.grid(column=0,row=1, columnspan=3, pady=5, padx=15)
                
                
            except:
                #print("Error en la url del video, no es posible descargar")   
                self.statusBar = Label(bd=1, fg="red",width=55, relief=SUNKEN, anchor='center', text=" * Error, introduce una URL Válida * ")
                self.statusBar.grid(column=0,row=1, columnspan=3, pady=5, padx=15)
        
        
        self.url = Label(text="Introduzca la url: ", fg= 'red', bg='#e2e2e2',font=('Helvetica', 14, 'bold'))
        self.url.grid(column=0,row=0, pady=5, padx=15)
        
        #entrada de mi url 
        self.urlText = Entry(width=60, fg= 'white', bg='gray',font=('Helvetica',12))
        self.urlText.grid(column=1,row=0, pady=5, padx=5)
        
        note = "Este programa es capaz de descargar videos de Youtube, a una calidad Máxima de 720p en mp4, \n en siguientes versiones intentaremos descargar videos de diferentes calidades, y o solo el audio de los mismos. "
        
        self.nota = Label(text= note, fg='red', bg= '#e2e2e2', font=('Helvetica', 12, 'bold'))
        self.nota.place(relx=0.5, rely=0.92, anchor='center')
        
        self.iBoton = PhotoImage(file ='boton2.png')
        self.boton = Button(image= self.iBoton, bg='#e2e2e2', highlightbackground= '#e2e2e2', highlightthickness= 2, borderwidth= 0, command= descarga)
        self.boton.grid(column=2,row=0, pady=3, padx=20)
        
        #mi barra de estado que me avisa si hay error o se descargo bien
        self.statusBar = Label(bd=1, fg="grey",width=55, relief=SUNKEN, anchor='center', text="")
        self.statusBar.grid(column=0,row=1, columnspan=3, pady=5, padx=15)
        
    

if __name__ == "__main__":
    ventana = Tk()    
    ventana.title('YoutubeDown by Tomi 1.1')    
    ventana.config(bg= '#e2e2e2')
    ventana.minsize(height= 450,width=900)   
    ventana.resizable(0,0) 
    ventana.call('wm', 'iconphoto', ventana._w, ImageTk.PhotoImage(Image.open('descargar.png')))
    ventana.geometry('900x450')
    
    fondo = PhotoImage(file ='fondo.png')
    background = Label(image=fondo, bg='#e2e2e2')
    background.place(x=0.5, y=0.5, relwidth=1, relheight=1.25)
    
    app = YT(ventana)            
    app.mainloop()
    