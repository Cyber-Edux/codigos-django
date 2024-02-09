from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Publication
from datetime import date

def feed(request):
    context = {
        'posts': Publication.objects.all()
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        content = request.POST.get("content")
        publication = Publication()
        publication.author = author
        publication.content = content
        publication.date = date.today()
        publication.save()
        return HttpResponseRedirect('/feed')
    else:
        return render(request, 'publicate.html')
