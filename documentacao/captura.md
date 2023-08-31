Documentação Reconhecimento Facial

## captura.py ##

O código começa importando as bibliotecas necessárias: cv2 (OpenCV) 
para processamento de imagens e numpy para manipulação de arrays.

Carrega dois classificadores pré-treinados para detecção de faces e olhos: 
classificador e classificadorOlho. 
Esses classificadores são baseados em arquivos XML que contêm informações sobre as características das faces e olhos.

Uma captura de vídeo é criada usando cv2.VideoCapture(0) para acessar a câmera do computador.

Variáveis de controle são inicializadas: amostra contará o número de amostras capturadas, 
numeroAmostras define quantas amostras você deseja capturar e id é uma entrada de identificação.

As dimensões desejadas para as imagens de rosto são definidas como largura e altura.

Um loop infinito começa para capturar imagens da câmera.

A imagem capturada da câmera é convertida para escala de cinza usando cv2.cvtColor().
- Simplificação de Dados
- Redução de Dimensionalidade
- Detecção de Características
- Redução de Ruído
- Eficiência Computacional

O classificador de detecção de face é aplicado à imagem em escala de cinza usando classificador.detectMultiScale(). 
Ele retorna as coordenadas (x, y) do canto superior esquerdo da face detectada e suas dimensões (largura e altura).

Um retângulo é desenhado ao redor da face detectada usando cv2.rectangle().

Uma região de interesse (ROI) da face é extraída da imagem original.

O classificador de detecção de olhos é aplicado à região de interesse da face em escala de cinza para detectar olhos.

Um retângulo é desenhado ao redor de cada olho detectado.

Se a tecla 'q' for pressionada, a média dos valores de intensidade de pixels da imagem em escala de cinza é calculada usando np.average(). Se for maior que 110 (um valor escolhido arbitrariamente), a região da face capturada é redimensionada para largura x altura e salva em um arquivo com um nome que inclui o identificador e o número da amostra.

A imagem é exibida na tela usando cv2.imshow() e a execução aguarda um tempo curto usando cv2.waitKey(1).

O loop é interrompido quando o número de amostras capturadas (amostra) atinge o valor numeroAmostras + 1.

O programa exibe uma mensagem de sucesso após a conclusão da captura.

A captura de vídeo é liberada e as janelas são fechadas usando camera.release() e cv2.destroyAllWindows().

Este código é destinado a capturar imagens de rostos usando a câmera do computador e detectar faces e olhos nessas imagens.

------------------------ ## code ## ----------------------------

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

# laço de repetição para capturar as imagens
while True:
    conectado, imagem = camera.read()

    if not conectado:
        print("Não foi possível capturar a imagem da câmera.")
        break

    if imagem is None:
        print("Imagem vazia.")
        continue

    # Converter a imagem para cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    #
    print(np.average(imagemCinza))
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100, 100))

    # Criando um retângulo em volta da face para a detecção
    # Salvar a foto
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + 1, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
        for (ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)
            # laço que captura as imagens a partir da tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                if np.average(imagemCinza) > 110:
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                    cv2.imwrite("fotos/pessoa." + str(id) + str(amostra) + ".jpg", imagemFace)
                    print("[foto " + str(amostra) + "capturada com sucesso]")
                    amostra += 1

	# o imshow é responsável por mostrar a imagem capturada
    cv2.imshow("face", imagem)
	# chamada que permite que você exiba uma imagem por um período específico de tempo e aguarde a entrada do teclado.
    cv2.waitKey(1)
	# se a amostra for maior ou igual o numero de amostras que eu quero, eu paro o programa
    if amostra >= numeroAmostras + 1:
        break

print("Faces capturadas com sucesso!")
# Desliga a câmera
camera.release() 
# Fecha todas as janelas abertas
cv2.destroyAllWindows()
