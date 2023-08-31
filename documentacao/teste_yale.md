Documentação Reconhecimento Facial

## teste_yale ##

Este código é usado para testar a precisão do classificador de reconhecimento facial treinado 
usando o conjunto de dados Yale Face Database. Ele carrega o classificador treinado e o aplica às 
imagens de teste, calculando o percentual de acertos e a confiança média das previsões.

O classificador pré-treinado para detecção de face é carregado usando cv2.CascadeClassifier.

O classificador treinado usando o método Fisherfaces é carregado usando cv2.face.FisherFaceRecognizer.

O código percorre as imagens de teste na pasta "yalefaces/teste".

Para cada imagem, a detecção de face é realizada usando o classificador de detecção de face.

O reconhecimento facial é aplicado à imagem detectada, e o ID previsto e a confiança são obtidos.

O ID real da pessoa na imagem de teste é extraído do nome do arquivo.

O código exibe a previsão feita e compara com o ID real.

Se a previsão estiver correta, os resultados são atualizados.

Após processar todas as imagens de teste, o código calcula o percentual de acertos e a média da confiança das previsões.

Este código permite avaliar a precisão do classificador de reconhecimento facial treinado usando 
as imagens de teste do conjunto Yale Face Database. Certifique-se de ter as imagens de teste corretamente 
organizadas na pasta antes de executar este código.


-------------------------- # code # ------------------------------ 
import cv2
import os
import numpy as np
from PIL import Image

# Carregar o classificador de detecção de face pré-treinado
detectorFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Carregar o classificador de reconhecimento treinado
reconhecedor = cv2.face.FisherFaceRecognizer.create()
reconhecedor.read("classificadorFisherYale.yml")

# Inicialização de variáveis para armazenar resultados
totalAcertos = 0
percentualAcerto = 0.0
totalConfianca = 0.0

# Percorrer as imagens de teste
caminhos = [os.path.join('yalefaces/teste', f) for f in os.listdir('yalefaces/teste')]
for caminhoImagem in caminhos:
    imagemFace = Image.open(caminhoImagem).convert('L')
    imagemFaceNP = np.array(imagemFace, 'uint8')
    
    # Detectar faces na imagem
    facesDetectadas = detectorFace.detectMultiScale(imagemFaceNP)
    for (x, y, l, a) in facesDetectadas:
        # Prever o ID da pessoa na imagem
        idprevisto, confianca = reconhecedor.predict(imagemFaceNP)
        
        # Obter o ID real da pessoa na imagem de teste
        idatual = int(os.path.split(caminhoImagem)[1].split(".")[0].replace("subject", ""))
        
        print(str(idatual) + " foi classificado como " + str(idprevisto) + " - " + str(confianca))
        
        # Verificar se a previsão está correta e atualizar as variáveis de resultados
        if idprevisto == idatual:
            totalAcertos += 1
            totalConfianca += confianca

# Calcular percentual de acertos e média da confiança
percentualAcerto = (totalAcertos / 30) * 100  # 30 imagens de teste no conjunto Yale
totalConfianca = totalConfianca / totalAcertos if totalAcertos > 0 else 0

# Exibir os resultados
print("Percentual de acerto: " + str(percentualAcerto))
print("Total confiança média: " + str(totalConfianca))
