from cv2 import threshold
from django.http import HttpResponse
from django.shortcuts import render, redirect

from reconhecedor.reconhecedor_fisherfaces import reconhecedor
from .models import Funcionario
from .forms import FuncionarioForm


# Create your views here.

def registrar_ponto(request):
    if request.method == 'POST':
        # Captura a imagem da face do funcionário
        imagem = request.FILES['imagem']

        # realiza o reconhecimento facial
        identificacao, confianca = reconhecedor.predict(imagem)

        # verifica se o funcionário foi reconhecido
        if confianca > threshold:
            # registra o ponto do funcionário
            funcionario = Funcionario.objects.get(id=identificacao)
            funcionario.pontos += 1
            funcionario.save()

            return HttpResponse('Ponto registrado com sucesso!')
        else:
            return HttpResponse('Funcionário não reconhecido!')
    return render(request, 'ponto.html')


def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES)

        if form.is_valid():
            funcionario = form.save()
            return redirect('funcionarios')
    else:
        form = FuncionarioForm()

    return render(request, 'cadastrar.html', {'form': form})
