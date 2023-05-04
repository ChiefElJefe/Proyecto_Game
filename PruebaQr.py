import cv2, qrcode
# import numpy as np
# import webbrowser
# from pyzbar.pyzbar import decode
#
# # img = cv2.imread('1.png')
# # for barcode in decode(img):
# #     datos = barcode.data.decode('utf-8')
# #     print(datos)
# img = qrcode.make("El Cabeza Cono")
# img.save("cabezacono.png")
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
#
# while True:
#     success, img = cap.read()
#     for barcode in decode(img):
#         datos = barcode.data.decode('utf-8')
#         print(datos)
#         pts = np.array([barcode.polygon], np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(img, [pts], True, (255, 0, 255), 5)
#         webbrowser.open(datos)
#
#         cv2.destroyAllWindows()
#         break
#
#     cv2.imshow('Resultado', img)
#     cv2.waitKey(1)
# cap.release()
# cv2.destroyAllWindows()
import random
import string

all_code = []


def generar_codigo():
    existe = True

    while existe:
        existe = False
        codigo = '-'.join([''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for i in range(3)])
        for x in all_code:
            if x == codigo:
                existe = True

        if not existe:
            all_code.append(codigo)


for i in range(50):
    generar_codigo()

print(all_code)
