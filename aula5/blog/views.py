from django.shortcuts import render
from django.http import HttpResponseRedirect

def feed(request):
    context = {
        'posts': [
            {'author': 'Fulano', 'date': '01/02/24', 'content': 'alskdgjbaslkdgjbasdlkgjbasdlkjb'},
            {'author': 'Ciclano', 'date': '24/01/24', 'content': 'alskdgjbaslkdgjbasdlkgjbasdlkjb'},
            {'author': 'Beltrano', 'date': '10/12/24', 'content': 'alskdgjbaslkdgjbasdlkgjbasdlkjb'}
        ]
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        content = request.POST.get("content")
        print(author)
        print(content)
        return HttpResponseRedirect('/feed')
    else:
        return render(request, 'publicate.html')
