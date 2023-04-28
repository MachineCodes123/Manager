import os
import zipfile
import random

class Manager:
      def editor(self):
           os.system("clear")
           print("antes de iniciar con el editor deberia decirme el nombre del archivo.")
           print("")
           nombre_archivo = input("nombre del archivo: ")
           print("")
           print("bien ahora su extencion")
           extension_archivo = input("extencion del archivo: ")
           os.system("nano " + nombre_archivo + "." + extension_archivo)
        
      def ejec(self):
           os.system("clear")
           print("Deberías darme el nombre del archivo (solo corre python).")
           nombre_archivo = input("Nombre del archivo: ")
           os.system("python " + nombre_archivo + ".py")
      
      def compresor(self):
           os.system("clear")
           print("para continuar debera de darme el archivo en comum.")
           archivo = input("nombre: ")
           print("tambien deberia darme su extension.")
           extension = input("extencion: ")
           os.system("clear")
           print("este programa actualmente no tiene función de agregar nombre al zip, no obstante el archivo será números aleatorios.")
           pausa = input("presione cualquier cosa para avanzar.")
           os.system("clear")
           a = random.randint(1, 10000)
           with zipfile.ZipFile(str(a) + ".zip", mode="w", compress_type=zipfile.ZIP_BZIP2) as zip:
                zip.write(archivo + "." + extension)
