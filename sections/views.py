from django.shortcuts import render

from sections.models import Section


def index(request):
    query = request.GET.get('q')
    if query:
        sections = Section.objects.filter(name__icontains=query)
    else:
        sections = Section.objects.all()
    return render(request, 'index.html', {'sections': sections})
