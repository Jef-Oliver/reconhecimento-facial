import cv2
import numpy as np

classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
classificadorOlho = cv2.CascadeClassifier("haarcascade_eye.xml")
camera = cv2.VideoCapture(0)  # Indica câmera do pc
amostra = 1
numeroAmostras = 25
id = input('Digite seu identificador: ')
largura, altura = 220, 220
print("Capturando as imagens...")

while True:
    conectado, imagem = camera.read()

    if not conectado:
        print("Não foi possível capturar a imagem da câmera.")
        break

    if imagem is None:
        print("Imagem vazia.")
        continue

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    print(np.average(imagemCinza))
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100, 100))

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + 1, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
        for (ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if np.average(imagemCinza) > 110:
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                    cv2.imwrite("fotos/pessoa." + str(id) + str(amostra) + ".jpg", imagemFace)
                    print("[foto " + str(amostra) + "capturada com sucesso]")
                    amostra += 1

    cv2.imshow("face", imagem)
    cv2.waitKey(1)

    if amostra >= numeroAmostras + 1:
        break

print("Faces capturadas com sucesso!")
camera.release()
cv2.destroyAllWindows()
