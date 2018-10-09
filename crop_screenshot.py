# Requieres PIL Module: http://www.pythonware.com/products/pil/
# https://pillow.readthedocs.io/en/5.3.x/installation.html
# Install with: pip install Pillow
# execute using python recortar_capturas.py

from PIL import Image
import glob, os

# -------------Define area de recorte
# Laptop con monitor personal
area1 = (0, 0, 1600, 900) # Lado izquierdo; monitor externo
# Laptop con monitor trabajo
# area2 = (1366, 0, 3286, 1080)
# Monitores trabajo
# area2 = (1366, 0, 3286, 1080)


# directorio final
dir = "crop"

# verifica que exista directorio
if os.path.exists( dir ) == False:
    os.mkdir( dir )
    print("Directorio creado")

# Se obtienen archivos de directorio actual
lista = glob.glob("*.png")
# se recorre lista
for imagen in lista:
    # obtiene nombre de imagen y extension
    file = os.path.splitext(imagen)
    name = file[0]
    ext = file[1]
    # se abre
    im = Image.open(imagen)
    # se define dimensiones obtenidas desde imagen (captura)
    width, height = im.size 

    area = ""

    #se verifica dimension (doble monitor)
    # if width == 2966 and height == 900:
    #     area = area1
    # elif width == 3286 and height == 1080:
    #     area = area2
    # else: 
    #     area = ""
    recorte = area1


    if recorte != "":
        # recortando    
        crop = im.crop(recorte)
        print(name + " recortado")
        # se guarda
        # crop.save( dir+ "/"+ name + "-crop" + ext, "PNG" )
        crop.save( dir+ "/"+ name + ext, "PNG" )
    else: 
        print(name + " omitido")
    