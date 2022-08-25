from cv2 import cv2
import face_recognition as fr

# imgs load

foto_control = fr.load_image_file('foto1.jpg')
foto_prueba = fr.load_image_file('foto2.jpg')

# purgue imges

foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# find face
cara_place_A = fr.face_locations(foto_control)[0]
cara_encode_A = fr.face_encodings(foto_control)[0]

cara_place_B = fr.face_locations(foto_prueba)[0]
cara_encode_B = fr.face_encodings(foto_prueba)[0]


# show in screen face
cv2.rectangle(foto_control, (cara_place_A[3], cara_place_A[0]),(cara_place_A[2], cara_place_A[1]),(255, 0 ,0), 2)
cv2.rectangle(foto_prueba, (cara_place_B[3], cara_place_B[0]),(cara_place_B[2], cara_place_B[1]),(255, 0 ,0), 2)

# compare

resultado = fr.compare_faces([cara_encode_A], cara_encode_B)



# show imgs
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)


# para que no se cierre el programa
cv2.waitKey(0)