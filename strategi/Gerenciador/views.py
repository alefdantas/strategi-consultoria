
from django.shortcuts import render,redirect
from marvel import Marvel


from .models import Personagem


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
    return render(request,'candidatos.html',{"candidato":personagem})

def seleciona_personagem(request,nome):
    if request.method == 'POST':
        save =Personagem(nome=nome)
        save.save()
    return redirect('lista_candidatos')