from cv2 import threshold
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FuncionarioForm
from .models import Funcionario
from .reconhecedor import fisherfaces


# Create your views here.

def registrar_ponto(request):
    if request.method == 'POST':
        # Captura a imagem da face do funcionário
        imagem = request.FILES['imagem']

        # realiza o reconhecimento facial
        identificacao, confianca = fisherfaces() #.predict(imagem)

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
    # Validar dados

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        data_nascimento = request.POST.get('data_nascimento')
        cargo = request.POST.get('cargo')

        if not nome:
            return HttpResponse('Nome não informado!')
        if not cpf:
            return HttpResponse('CPF não informado!')
        if not rg:
            return HttpResponse('RG não informado!')
        if not data_nascimento:
            return HttpResponse('Data de nascimento não informada!')
        if not cargo:
            return HttpResponse('Cargo não informado!')

    # Salvar funcionário
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)  # request.FILES ?
        if form.is_valid():
            form.save()
            # return redirect('ponto')

    return render(request, 'cadastrar.html', context={'form': FuncionarioForm()})

def listagem(request):
    data = {'funcionarios': Funcionario.objects.all()}
    return render(request, "/templates/listagem.html", data)

