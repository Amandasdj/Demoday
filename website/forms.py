from django import forms
from website.models import *

class  LoginForm(forms.Form):

    #Formulário de login
    email = forms.EmailField(label='Email', widget=forms.widgets.EmailInput(), required=True)
    senha = forms.CharField(label='Senha', widget=forms.widgets.PasswordInput(), required=True, max_length=15)

class UsuarioForm(LoginForm): #Herda campos de LoginForm

    #Formulário de cadastro
    confirma = forms.CharField(label='Confirmar senha', required=True, widget=forms.widgets.PasswordInput(), max_length=15)
    user = forms.CharField(label='User', required=True, max_length=15)
    nome = forms.CharField(label='Nome', required=True, max_length=15)
    sobrenome = forms.CharField(label='Sobrenome', required=True, max_length=15)
    telefone = forms.CharField(label='Telefone', widget=forms.widgets.NumberInput(), required=True, max_length=15)

class DesafioForm(forms.ModelForm): #Usa uma model para criar campos
    class Meta:
        model = Desafio
        fields = ('titulo', 'tema', 'valor')

class RespostaForm(forms.Form):
    imagem = forms.ImageField(label='Enviar imagem', widget=forms.widgets.ClearableFileInput)
    texto =  forms.CharField(max_length=240, widget=forms.widgets.Textarea)