from keras.utils import load_img

# dimensiones para que la imagen se pueda ver bien con bajos pixeles (aceptable)
#200, 300
#300, 400

largo, alto = 300, 400

file = "../../Archivos/Imagenes/gafas.jpg"

img = load_img(file, target_size = (largo, alto)
               , color_mode ="grayscale"
               )

print(img.size)
print(img.mode)

img.show()