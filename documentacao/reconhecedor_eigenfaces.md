Documentação Reconhecimento Facial

## reconhecedor_eigenfaces ##

Carrega um classificador pré-treinado para detecção de faces chamado detectorFace usando o arquivo XML 
"haarcascade_frontalface_default.xml".

Ele cria um objeto de reconhecimento facial chamado reconhecedor usando o método cv2.face.EigenFaceRecognizer.create(). 
Em seguida, ele lê um arquivo de classificador treinado chamado "classificadorEigen.yml".

Define as dimensões desejadas (largura e altura) para as imagens usadas no processo de reconhecimento.

Usa a fonte cv2.FONT_HERSHEY_COMPLEX_SMALL para exibir texto na imagem.

Inicializa a câmera usando cv2.VideoCapture(0) para capturar imagens da webcam.

O loop começa a capturar imagens da câmera.

As imagens capturadas são convertidas para escala de cinza usando cv2.cvtColor().

O classificador detectorFace é aplicado à imagem em escala de cinza para detectar faces.

Para cada face detectada, o código recorta a região da face, desenha um retângulo ao redor dela na 
imagem original e realiza o reconhecimento facial usando o objeto reconhecedor.

Com base no ID do reconhecimento, ele define um nome para exibição na imagem.

As informações do reconhecimento (ID e confiança) são exibidas na imagem usando cv2.putText().

A imagem com as detecções e reconhecimentos é exibida usando cv2.imshow().

O loop continua até que a tecla 'q' seja pressionada, momento em que a câmera é liberada e as janelas são 
fechadas usando camera.release() e cv2.destroyAllWindows().

------------------------ ## code ## ----------------------------

import cv2

# Carregar classificador pré-treinado para detecção de face
detectorFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Criar um objeto de reconhecimento facial usando Eigenfaces
reconhecedor = cv2.face.EigenFaceRecognizer.create()
reconhecedor.read("classificadorEigen.yml")

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
        if id == 11:
            nome = 'Jeferson'
        elif id == 12:
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
