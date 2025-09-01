from keras.utils import load_img

largo, alto = 300, 200

file = "../../Archivos/Imagenes/gafas.jpg"

img = load_img(file, target_size = (largo, alto)
               , color_mode ="grayscale"
               )

print(img.size)
print(img.mode)

img.show()