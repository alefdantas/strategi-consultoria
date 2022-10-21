
from django.shortcuts import render,redirect
from marvel import Marvel


from .models import  Equipe_1, Equipe_2, Equipe_3, Equipe_4, Personagem


# Create your views here.
m = Marvel('96880e53994404a45aae97658a555f4c','44484b10cb6931db4d228421ac367b348fc2a631')
def salva_herois(request):
    personagem = m.characters.all()['data']['results']
    vetor = []
    for i in range(len(personagem)):
        data = m.characters.all()['data']
        results = data['results']
        personagem_aux = results[i]
        vetor.append(personagem_aux)
    data = {"personagens": vetor}
    return render(request,'index.html',data)
        
def lista_candidatos(request):
    personagem = Personagem.objects.all()
    equipe_1 = Equipe_1.objects.all()
    equipe_2 = Equipe_2.objects.all()
    equipe_3 = Equipe_3.objects.all()
    equipe_4 = Equipe_4.objects.all()

    return render(request,'candidatos.html',{"candidato":personagem,"equipe_1":equipe_1,"equipe_2":equipe_2,"equipe_3":equipe_3,"equipe_4":equipe_4,})

def seleciona_personagem(request,nome):
    if request.method == 'POST':
        save =Personagem(nome=nome)
        save.save()
    return redirect('lista_candidatos')

def retira_heroi(request,id):
    personagem = Personagem.objects.filter(id=id)
    personagem.delete()
    return redirect('lista_candidatos')

def forma_equipe_1(request,id):
    if request.method == 'POST':

        personagem = Personagem.objects.filter(id=id)
        for i in personagem:
            nome =i.nome
            save = Equipe_1(nome=nome)
            save.save()
        personagem.delete()
    return redirect('lista_candidatos')

def forma_equipe_2(request,id):
    if request.method == 'POST':

        personagem = Personagem.objects.filter(id=id)
        for i in personagem:
            nome =i.nome
            save = Equipe_2(nome=nome)
            save.save()
        personagem.delete()
    return redirect('lista_candidatos')

def forma_equipe_3(request,id):
    if request.method == 'POST':

        personagem = Personagem.objects.filter(id=id)
        for i in personagem:
            nome =i.nome
            save = Equipe_3(nome=nome)
            save.save()
        personagem.delete()
    return redirect('lista_candidatos')

def forma_equipe_4(request,id):
    if request.method == 'POST':

        personagem = Personagem.objects.filter(id=id)
        for i in personagem:
            nome =i.nome
            save = Equipe_4(nome=nome)
            save.save()
        personagem.delete()
    return redirect('lista_candidatos')

def retira_equipe_1(request,id):
    if request.method == 'POST':
        equipe = Equipe_1.objects.filter(id=id)
        for i in equipe:
            nome =i.nome
            save = Personagem(nome=nome)
            save.save()
        equipe.delete()
    return redirect('lista_candidatos')

def retira_equipe_2(request,id):
    if request.method == 'POST':
        equipe = Equipe_2.objects.filter(id=id)
        for i in equipe:
            nome =i.nome
            save = Personagem(nome=nome)
            save.save()
        equipe.delete()
    return redirect('lista_candidatos')

def retira_equipe_3(request,id):
    if request.method == 'POST':
        equipe = Equipe_3.objects.filter(id=id)
        for i in equipe:
            nome =i.nome
            save = Personagem(nome=nome)
            save.save()
        equipe.delete()
    return redirect('lista_candidatos')

def retira_equipe_4(request,id):
    if request.method == 'POST':
        equipe = Equipe_4.objects.filter(id=id)
        for i in equipe:
            nome =i.nome
            save = Personagem(nome=nome)
            save.save()
        equipe.delete()
    return redirect('lista_candidatos')