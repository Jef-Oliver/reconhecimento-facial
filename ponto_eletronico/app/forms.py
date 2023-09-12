import os

from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    foto_1 = forms.ImageField(required=True)
    foto_2 = forms.ImageField(required=True)
    foto_3 = forms.ImageField(required=True)
    foto_4 = forms.ImageField(required=True)
    foto_5 = forms.ImageField(required=True)

    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'rg', 'data_nascimento', 'cargo']

    def save(self, commit=True):
        funcionario = super().save(commit=False)

        # Cria uma pasta para o funcionario
        pasta_funcionario = f'fotos/funcionarios/{funcionario.id}'
        os.makedirs(pasta_funcionario, exist_ok=True)

        # Salva as fotos na pasta do funcionário
        foto_1 = self.cleaned_data['foto_1']
        foto_1.save(os.path.join(pasta_funcionario, 'foto_1.jpg'))
        foto_2 = self.cleaned_data['foto_2']
        foto_2.save(os.path.join(pasta_funcionario, 'foto_2.jpg'))
        foto_3 = self.cleaned_data['foto_3']
        foto_3.save(os.path.join(pasta_funcionario, 'foto_3.jpg'))
        foto_4 = self.cleaned_data['foto_4']
        foto_4.save(os.path.join(pasta_funcionario, 'foto_4.jpg'))
        foto_5 = self.cleaned_data['foto_5']
        foto_5.save(os.path.join(pasta_funcionario, 'foto_5.jpg'))

        if commit:
            funcionario.save()

        return funcionario
