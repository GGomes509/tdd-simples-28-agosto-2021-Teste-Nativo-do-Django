from django.shortcuts import render
from .models import BuscarRaças 

def home(request):
    #Colocar 'nomeModel.objects.all()' para ver ser o 'test_views.py' esta funcionado' 
    #context={'terra':BuscarRaças.objects.all()}
    #end
    #Esse é para colocar depois que teste o test_views.py
    context = {'terra': None}

    if 'buscar' in request.GET:
        raças = BuscarRaças.objects.all()
        raças_pesquisadas =request.GET['buscar']
        terra = raças.filter(nome_raça__icontains = raças_pesquisadas)
        context ={ 'terra':terra}
    
    #end#
    return render(request, 'home.html', context)
