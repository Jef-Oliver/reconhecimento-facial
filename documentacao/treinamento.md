Documentação Reconhecimento Facial

## treinamento ##

Três objetos de classificadores são criados: eigenface, fisherface e lbph. 
Cada um desses objetos será treinado para reconhecimento facial.

A função getImagemComId() é definida para percorrer a pasta "fotos" e coletar os caminhos das imagens de treinamento, 
bem como os IDs correspondentes a cada imagem. As imagens são convertidas para escala de cinza e adicionadas a uma 
lista faces, enquanto os IDs são adicionados a uma lista ids.

Os objetos eigenface, fisherface e lbph são treinados usando as faces e IDs obtidos da função getImagemComId().

Cada classificador treinado é salvo em um arquivo YAML correspondente: 'classificadorEigen.yml', 'classificadorFisher.yml' 
e 'classificadorLBPH.yml'.

Uma mensagem é exibida indicando que o treinamento foi concluído.

Este código é usado para treinar os classificadores de reconhecimento facial com as imagens coletadas na pasta "fotos". 
Cada classificador é treinado em diferentes métodos de reconhecimento facial e os resultados são salvos em arquivos YAML 
para uso posterior na detecção e reconhecimento de rostos em tempo real. Certifique-se de ter as imagens de treinamento 
corretamente organizadas na pasta "fotos" antes de executar este código.

------------------------ ## code ## ----------------------------

import cv2
import os
import numpy as np

# Criação dos objetos para os classificadores
eigenface = cv2.face.EigenFaceRecognizer.create(num_components=50, threshold=2)
fisherface = cv2.face.FisherFaceRecognizer.create()
lbph = cv2.face.LBPHFaceRecognizer.create()

# Função para obter imagens com seus respectivos IDs
def getImagemComId():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        ids.append(id)
        faces.append(imagemFace)
    return np.array(ids), faces

# Obtém os IDs e faces das imagens de treinamento
ids, faces = getImagemComId()

# Treinamento dos classificadores
print("Treinamento dos classificadores...")
eigenface.train(faces, ids)
eigenface.write('classificadorEigen.yml')

fisherface.train(faces, ids)
fisherface.write('classificadorFisher.yml')

lbph.train(faces, ids)
lbph.write('classificadorLBPH.yml')

print('Treinamento Realizado')
