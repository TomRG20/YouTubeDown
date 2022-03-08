'''
    En teoria esto te permitiría bajar videos de youtube 
    en el mismo directorio que nuestro programa. 
    
    video de prueba: 
    ¿Como funciona un PC y que hace cada pieza? | Componentes del ordenador explicados
    https://www.youtube.com/watch?v=0zkX6nlpiSk 
'''
from pytube  import YouTube

link = input("Enter URL: ")    #Introducimos la URL del video que queremos descargar

def descarga (url):
    v = YouTube(url)           #Creamos el objeto video de youtube
    titulo = str(v.title)      #Sacamos su atributo título
    autor = str(v.author)
    visualizaciones = int(v.views)
    duracion = int(v.length)   #duración del video
    vide = v.vid_info          #me saca un diccionario enorme de datos que tengo que analizar
    vid = str(v.video_id)      #identificador de las busquedas de youtube  0zkX6nlpiSk    
    
    print("Descargando el video de: ", titulo)
    print("Con autor: ", autor)
    print("Con el número de ", visualizaciones , " visualizaciones")
    print("La duración del video es: ", duracion // 60 , " minutos y ", duracion % 60 , " Segundos")
    
    ''' FORMAS PARA DESCARGAR UN VIDEO o UN AUDIO de YOUTUBE
    
        Si queremos descargar solo un audio de un video: 
                v.streams.get_audio_only().download()
        si queremos descargar un video de una lista de reproducción:
                v.streams.get_by_itag().download()
        Si queremos descargar la minima resolución posible y en 3Gpp:
                v.streams.get_lowest_resolution().download()
        Si queremos descargar la maxima resolución posible y en mp4:
                v.streams.get_highest_resolution().download()
        Si queremos descargar a una resolución a nuestro gusto y en mp4:
                v.streams.get_by_resolution("la resolucion deseada").download()  "2160","1440", "1080", "720p", "480p", "360p", "240p", "144p"
    '''
    
    v.streams.get_by_resolution("720p").download()
    print("\nEl video se ha descargado con exito...\n\n")

descarga(link)     #Llamamos a la funcion descargar