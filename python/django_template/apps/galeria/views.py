from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

def index(request):
    tipos_dict = {'NB': 'Nebulosa',
                  'ES': 'Estrela',
                  'GA': 'Galáxia',
                  'PL': 'Planeta'}
    
    if not request.user.is_authenticated:
        messages.error(request, 'Para acessar a galeria, faça login.')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    for fotografia in fotografias:
        fotografia.categoria = tipos_dict[str(fotografia.categoria)]
        
    return render(request, 'sobre-mim/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Para acessar a galeria, faça login.')
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'sobre-mim/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Para acessar a galeria, faça login.')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_buscado = request.GET['buscar']
        if nome_buscado:
            fotografias = fotografias.filter(nome__icontains=nome_buscado)
    return render(request, 'sobre-mim/buscar.html', {"cards": fotografias})

def nova_imagem(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Para postar imagens, faça login.')
        return redirect('login')
    
    form = FotografiaForms()

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia enviada para aprovação.')
            return redirect('index')

    return render(request, 'sobre-mim/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Para acessar a galeria, faça login.')
        return redirect('login')
    
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        messages.success(request, 'Fotografia editada com sucesso.')
        return redirect('index')

    return render(request, 'sobre-mim/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Para acessar a galeria, faça login.')
        return redirect('login')
    
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia deletada com sucesso.')
    return redirect('index')

def filtro(request, categoria):
    tipos_dict = {'NB': 'Nebulosa',
                  'ES': 'Estrela',
                  'GA': 'Galáxia',
                  'PL': 'Planeta'}
    if not request.user.is_authenticated:
        messages.error(request, 'Para acessar a galeria, faça login.')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True).filter(categoria=categoria)
    for fotografia in fotografias:
        fotografia.categoria = tipos_dict[str(fotografia.categoria)]
    return render(request, 'sobre-mim/index.html', {"cards": fotografias})