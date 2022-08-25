from cv2 import cv2
import face_recognition as fr

# imgs load

foto_control = fr.load_image_file('foto1.jpg')
foto_prueba = fr.load_image_file('foto2.jpg')

# purgue imges

foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# show imgs
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

# para que no se cierre el programa
cv2.waitKey(0)