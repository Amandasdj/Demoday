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

class DesafioForm(forms.Form): #Usa uma model para criar campos
    titulo = forms.CharField(label='', required=True, max_length=15, widget=forms.widgets.TextInput(attrs={'placeholder':'Aqui o título!!!'}))
    tema = forms.CharField(label='', required=True, max_length=15, widget=forms.widgets.TextInput(attrs={'placeholder':'Qual o tema?!? Do que se trata?!'}))
    valor = forms.CharField(label='', required=True, max_length=240, widget=forms.widgets.Textarea(attrs={'placeholder':'Descreva seu desafio aqui... '}))

class RespostaForm(forms.Form):
    imagem = forms.ImageField(label='Enviar imagem', widget=forms.widgets.ClearableFileInput)
    texto =  forms.CharField(label='', max_length=240, widget=forms.widgets.Textarea(attrs={'placeholder': 'Sua resposta...'}))