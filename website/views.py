from django.shortcuts import render, redirect
from website.forms import *
from website.models import *
from django.core.files import File
from django.conf import settings
import os

def cadastrar(request):

    # try:
        #Entregar o form como contexto
        form = UsuarioForm()

        if request.method == 'POST':

            #Pegar Valores do forms
            user = request.POST.get('user')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            confirma = request.POST.get('confirma')
            telefone = request.POST.get('telefone')
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')

            #Verificação de campos únicos já existentes
            if Perfil.objects.filter(user=user).exists():

                return render(request, 'cadastro.html', {'cadastro':form, 'msg':'*Nome já está sendo usado, tente outro..'})

            elif Perfil.objects.filter(email=email).exists():

                return render(request, 'cadastro.html', {'cadastro':form, 'msg':'*Email já cadastrado'})

            elif Perfil.objects.filter(telefone=telefone).exists():

                return render(request, 'cadastro.html', {'cadastro':form, 'msg':'*Telefone já cadastrado'})
            
            elif senha != confirma:

                return render(request, 'cadastro.html', {'cadastro':form, 'msg':'*Senha e confirmação de senha diferentes'})
            
            else:

                #Cadastra e acessa home
                perfil = Perfil(avatar='avatar/genie.png', user=user, sobrenome=sobrenome, nome=nome, email=email, telefone=telefone, senha=senha)
                perfil.save()
                
                return redirect('/home/{}'.format(perfil.id))

        return render(request, 'cadastro.html', {'cadastro':form})
    
    except:

        return render(request, 'error.html')

def login(request):
    
    try:
        #Entregar form como contexto
        form = LoginForm()

        if request.method == 'POST':

            #Pegar valores do formulário
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            perfil = Perfil.objects.filter(email=email, senha=senha, ativo=True).first() #Filtro para buscar usuário no banco

            #Verificação do cadastro no banco
            if perfil is not None:

                return redirect('home/{}'.format(perfil.id))

            else:

                return render(request, 'index.html')

        return render(request, 'index.html', {'login':form})

    # except:

    #     return render(request, 'error.html')

def home(request, id):
    # try:
        perfil = Perfil.objects.filter(id=id, ativo=True).first() #Busca de infos do perfil
        desafios = Desafio.objects.filter(autor=perfil.id, ativo=True) #Busca de desafios criados pelo perfil
        desafios_gerais = Desafio.objects.exclude(autor=perfil.id).filter(ativo=True) #Busca excluindo desafios criados pelo perfil
        respostas = Resposta.objects.filter(autor=perfil.id, ativo=True, desafio__ativo=True) #Busca de resposta feitas pelo perfil

        #Lista vaziaz para montar contexto
        criados = []
        gerais_filtrados = []
        respostas_likes = []

        #Entregar infos de likes de respostas criadas
        for resposta in respostas:
            likes = Like.objects.filter(correspondente=resposta.id) #Busca de likes da resposta

            #Entregar uma lista de dicionários como contexto
            if len(likes) != 0: #Se tiver likes
                ultimo = likes.last() #Ultimo perfil que deu like

                #Adicionar um dicionário ao array
                respostas_likes.append({
                    'resposta':resposta,
                    'like':ultimo.perfil,
                    'likes': len(likes) #Quantidade de likes
                    })

            else:  #Senão

                #Entrega de contexto sem likes
                respostas_likes.append({ 
                    'resposta':resposta,
                    'like':'Sem likes!!'
                    })

        #Entregar apenas desafios não respondidos
        for desafio in desafios_gerais:
            if Resposta.objects.filter(desafio__id=desafio.id, autor=perfil).first() is None: #Se não houver resposta do perfil
                ultima_resposta = Resposta.objects.filter(desafio__id=desafio.id).last()
                likes = Like.objects.filter(correspondente=desafio.id) #Buscar likes do desafio
                seu_like = Like.objects.filter(correspondente=desafio.id, perfil=id).first() #Buscar se perfil já deu like

                #Entregar uma lista de dicionários como contexto
                if seu_like is None: #Se seu like não existir

                    #Adicionar um dicionário ao Array
                    gerais_filtrados.append({
                        'desafio':desafio,
                        'vc':None,
                        'likes': len(likes), #Quantidade de likes
                        'ultima':ultima_resposta
                        })

                else: #Senão

                    #Adicionar contexto de like com o perfil
                    gerais_filtrados.append({
                        'desafio':desafio,
                        'vc':'Você e mais ',
                        'likes':len(likes),
                        'ultima':ultima_resposta
                        })

        #Entregar infos de likes de desafios criados
        for desafio in desafios:
            respostas = Resposta.objects.filter(desafio=desafio) #Buscar respostas do desafio
            likes = Like.objects.filter(correspondente=desafio.id) #Buscar likes do desafio

            #Entregar uma lista de dicionários como contexto
            if len(likes) != 0: #Se houver likes
                ultimo = likes.last() #Ultimo perfil a dar like

                #Adicionar ao Array pra ser entregue como contexto
                criados.append({
                    'desafio':desafio,
                    'respostas': len(respostas), #Quantidade de respostas
                    'like':ultimo.perfil,
                    'likes': len(likes) #Quantidade de likes
                    })

            else: #Senão

                #Contexto sem likes
                criados.append({ 
                    'desafio':desafio,
                    'respostas': len(respostas),
                    'like':'Sem likes!!'
                    })
        
        #Entregar formulário
        form = DesafioForm()

        if request.method == 'POST': #Se mátodo da requisição for post
            titulo = request.POST.get('titulo')
            tema = request.POST.get('tema')
            valor = request.POST.get('valor')
            autor = Perfil.objects.filter(id=id, ativo=True).first() #Buscar perfil do autor
            filtro = Desafio.objects.filter(autor=autor, titulo=titulo, tema=tema, valor=valor, ativo=True).first() #Buscar se existe desafio idêntico

            #Verifica se Usuario já criou desafio idêntico
            if filtro is None:

                #Criação de um desafio no banco
                desafio = Desafio(autor=autor, titulo=titulo, tema=tema, valor=valor)
                desafio.save()

                return redirect('/home/{}'.format(id))

        #Entregar mensagem de 0 desafios criados
        if desafios.first() is None: #Se primeiro desafio não existir

            #Contexto sem desafios
            context = {
                'perfil':perfil, #Perfil do usuário
                'msg':'Você não criou nenhum desafio ainda, tente criar algum!!!!',
                'respostas':respostas_likes, #Array de respostas com infos
                'gerais':gerais_filtrados, #Array de desafios não respondidos com infos
                'form':form
            }

            return render(request, 'home.html', context)

        else: #Senão

            #Contexto com desafios
            context = {
                'perfil':perfil,
                'criados':criados, #Arrays com desafios criados e infos
                'respostas':respostas_likes,
                'gerais':gerais_filtrados,
                'form':form
            }

            return render(request, 'home.html', context)
    # except:

    #     return render(request, 'error.html')


#Página de um desafio
def desafio(request, id, id_desafio):
    
    # try:
        desafio = Desafio.objects.filter(id=id_desafio, ativo=True).first() #Buscar desafio
        respostas = Resposta.objects.filter(desafio__id=id_desafio, ativo=True) #Buscar respostas do desafio
        likes = Like.objects.filter(correspondente=id_desafio) #Buscar likes
        likes_respostas = []

        #Pegar os likes das respostas
        for resposta in respostas:

            l = Like.objects.filter(correspondente=resposta.id)
            ultimo = l.last()

            likes_respostas.append({
                'resposta':resposta,
                'likes':len(l),
                'ultimo':ultimo
            })

        ultimo = False

        if len(likes) != 0:
            ultimo = likes.last() #Ultimo perfil a dar like

        #Entrega formulário
        form = RespostaForm()
        
        #Para verificação de resposta idêntica
        if request.method == 'POST':
            imagem = request.FILES.get('imagem')
            valor = request.POST.get('texto')
            autor = Perfil.objects.filter(id=id, ativo=True).first() #Buscar perfil do autor
            filtro = Resposta.objects.filter(autor=autor, desafio=desafio).first()

            if filtro is None:
                #Criação de uma resposta no banco
                resposta = Resposta(valor=valor, autor=autor, desafio=desafio, imagem=imagem)
                resposta.save()
            
        filtro = Resposta.objects.filter(autor__id=id, desafio=desafio, ativo=True).first() #Filtrar existencia de resposta idêntica
        perfil = Perfil.objects.filter(id=id).first()
        
        #Entrega o contexto do desafio
        if  len(likes) != 0 and (filtro is None and desafio.autor.id != perfil.id): 
            context = {

                'perfil':perfil.id,
                'desafio':desafio,
                'respostas':likes_respostas,
                'likes':len(likes),
                'like':ultimo,
                'form':form
            }
        elif filtro is None and desafio.autor.id != perfil.id:
            context = {

                'perfil':perfil.id,
                'desafio':desafio,
                'respostas':likes_respostas,
                'likes':len(likes),
                'like':ultimo,
                'form':form
            }
        else:
            context = {

                'perfil':perfil.id,
                'desafio':desafio,
                'respostas':likes_respostas,
                'likes':len(likes),
                'like':ultimo,
                'respondido':True
            }
                

        return render(request, 'desafio.html', context)

    # except:
        
    #     return render(request, 'error.html')

#Página de um Perfil
def usuario(request, user):
    # try:
        perfil = Perfil.objects.filter(user=user, ativo=True).first() #Buscar perfil
        respostas = Resposta.objects.filter(autor__user=user, ativo=True) #Buscar respostas do perfil
        desafios = Desafio.objects.filter(autor__user=user, ativo=True) #Buscar desafios criados pelo perfil


        #Entregar contexto do Perfil
        if perfil is not None:
            context = {

                'perfil':perfil,
                'respostas':respostas,
                'desafios':desafios
            }

            return render(request, 'usuario.html', context)
    # except:

    #     return render(request, 'error.html')

#Fazer um like em um desafio
def like_desafio(request, id, id_desafio):
    # try:
        filtro = Like.objects.filter(correspondente=id_desafio, perfil__id=id).first() #Buscar like já existente

        #Verificar se Usuário já deu like
        if filtro is None:
            perfil = Perfil.objects.filter(id=id).first() #Buscar perfil do like

            #Salvar like no banco
            like = Like(correspondente=id_desafio, perfil=perfil)
            like.save()

        return redirect('/desafio/{}/{}'.format(id, id_desafio))
    
    # except:

    #     return render(request, 'error.html')

def like_resposta(request, id, id_resposta):
    # try:
        resposta = Resposta.objects.filter(id=id_resposta, ativo=True).first() #Buscar resposta
        filtro = Like.objects.filter(correspondente=id_resposta, perfil__id=id).first() #Buscar like já existente

        if filtro is None:
            perfil = Perfil.objects.filter(id=id).first() #Buscar perfil do like

            #Salvar like no banco
            like = Like(perfil=perfil, correspondente=resposta.id)
            like.save()
    
        return redirect('/desafio/{}/{}'.format(id, resposta.desafio.id))

    # except:

    #     return render(request, 'error.html')

def delete_desafio(request, id, id_desafio):
    # try:
        desafio = Desafio.objects.filter(id=id_desafio, ativo=True).first() #Buscar desafio

        #Verificar a existencia do desafio
        if desafio is not None:

            #Alterar para inativo
            desafio.ativo = False
            desafio.save()

            return redirect('/home/{}'.format(id))
    # except:

    #     return render(request, 'error.html')

def avatar(request, id):
    # try:
        if request.method == 'POST':
            perfil = Perfil.objects.filter(id=id).first()

            if request.FILES.get('avatar') is not None:
                perfil.avatar = request.FILES.get('avatar')
                perfil.save()

        return redirect('/home/{}'.format(id))

    # except:

    #     return render(request, 'error.html')