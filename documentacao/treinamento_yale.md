Documentação Reconhecimento Facial

## treinamento_yale ##

Este código realiza o treinamento de classificadores de reconhecimento facial usando o 
conjunto de dados Yale Face Database. 

O conjunto de dados consiste em imagens de rostos capturados sob diferentes condições de 
iluminação e expressões faciais.

Três objetos de classificadores são criados: eigenface, fisherface e lbph. Cada um desses 
objetos será treinado para reconhecimento facial.

A função getImagemComId() é definida para percorrer a pasta "yalefaces/treinamento" 
(onde estão as imagens de treinamento do conjunto de dados Yale Face Database). 
A função carrega cada imagem, converte-a para escala de cinza usando o módulo PIL e, em seguida, 
converte a imagem do formato PIL para uma matriz NumPy. Além disso, o ID da imagem é extraído do nome do arquivo.

Os IDs e as faces das imagens de treinamento são obtidos chamando a função getImagemComId().

Os classificadores são treinados usando as faces e IDs obtidos.

Cada classificador treinado é salvo em um arquivo YAML correspondente: 'classificadorEigenYale.yml', 
'classificadorFisherYale.yml' e 'classificadorLBPHYale.yml'.

Uma mensagem é exibida indicando que o treinamento foi concluído.

Este código é usado para treinar os classificadores de reconhecimento facial com o conjunto de dados Yale Face Database. 
Certifique-se de ter o conjunto de dados corretamente organizado nas pastas antes de executar este código.

------------------------ ## code ## ----------------------------

import cv2
import os
import numpy as np
from PIL import Image

# Criação dos objetos para os classificadores
eigenface = cv2.face.EigenFaceRecognizer.create(40, 8000)
fisherface = cv2.face.FisherFaceRecognizer.create(3, 2000)
lbph = cv2.face.LBPHFaceRecognizer.create(2, 2, 7, 7, 50)

# Função para obter imagens com seus respectivos IDs
def getImagemComId():
    caminhos = [os.path.join('yalefaces/treinamento', f) for f in os.listdir('yalefaces/treinamento')]
    faces = []
    ids = []
    for caminhoImagem in caminhos:
       imagemFace = Image.open(caminhoImagem).convert('L')
       imagemNP = np.array(imagemFace, 'uint8')
       id = int(os.path.split(caminhoImagem)[1].split(".")[0].replace("subject", ""))
       ids.append(id)
       faces.append(imagemNP)
    return np.array(ids), faces

# Obtém os IDs e faces das imagens de treinamento
ids, faces = getImagemComId()

# Treinamento dos classificadores
print("Treinando os classificadores...")
eigenface.train(faces, ids)
eigenface.write('classificadorEigenYale.yml')

fisherface.train(faces, ids)
fisherface.write('classificadorFisherYale.yml')

lbph.train(faces, ids)
lbph.write('classificadorLBPHYale.yml')

print("Treinamento realizado")
