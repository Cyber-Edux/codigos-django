from django.shortcuts import render

LOREM_IPSUM = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'

def home(request):
    publicacoes = [
        {'autor':'fulano',
         'data': '25/02/2024',
         'conteudo': LOREM_IPSUM},
        {'autor':'BELTRANO',
         'data': '25/02/2024',
         'conteudo': LOREM_IPSUM},
        {'autor':'CICLANO',
         'data': '25/02/2024',
         'conteudo': LOREM_IPSUM},
                   ]
    return render(request, 'index.html', {'publicacoes':publicacoes})