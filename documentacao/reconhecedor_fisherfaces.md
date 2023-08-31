Documentação Reconhecimento Facial

## reconhecedor_fisherfaces ##

O método Fisherfaces é outro algoritmo de reconhecimento facial baseado em análise de componentes principais. 
Ele é projetado para melhorar o reconhecimento em casos em que os Eigenfaces podem não funcionar tão bem.

A lógica do código é a mesma: capturar imagens da câmera, detectar faces na imagem, 
redimensionar a região da face, realizar o reconhecimento facial usando o objeto reconhecedor e exibir o 
resultado na imagem.

------------------------ ## code ## ----------------------------

import cv2

# Carregar classificador pré-treinado para detecção de face
detectorFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Criar um objeto de reconhecimento facial usando Fisherfaces
reconhecedor = cv2.face.FisherFaceRecognizer.create()
reconhecedor.read("classificadorFisher.yml")

# Definir largura e altura desejadas para as imagens de entrada do reconhecimento
largura, altura = 220, 220

# Definir a fonte para a exibição de texto
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

# Inicializar a câmera para capturar imagens
camera = cv2.VideoCapture(0)

while True:
    conectado, imagem = camera.read()

    if not conectado:
        print("Não foi possível capturar a imagem da câmera.")
        break

    # Converter a imagem capturada para escala de cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detectar faces na imagem em escala de cinza
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(20, 20))

    # Iterar sobre as faces detectadas
    for (x, y, l, a) in facesDetectadas:
        # Recortar a região da face
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        
        # Desenhar um retângulo ao redor da face na imagem original
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        
        # Realizar o reconhecimento facial usando o objeto "reconhecedor"
        id, confianca = reconhecedor.predict(imagemFace)
        
        # Definir um nome com base no ID do reconhecimento
        nome = ""
        if id == 1:
            nome = 'Jeferson'
        elif id == 2:
            nome = 'Desconhecido'
        
        # Exibir o ID e a confiança na imagem
        cv2.putText(imagem, str(id), (x, y + (a + 30)), font, 2, (0, 0, 255))
        cv2.putText(imagem, str(confianca), (x, y + (a + 50)), font, 1, (0, 0, 255))

    # Exibir a imagem com as detecções e reconhecimentos
    cv2.imshow("Face", imagem)
    
    # Aguardar até que a tecla 'q' seja pressionada para sair do loop
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar a câmera e fechar as janelas
camera.release()
cv2.destroyAllWindows()
