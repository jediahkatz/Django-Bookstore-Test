from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'template.html')

def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    request.session['location'] = "unknown"
    if request.user.is_authenticated():
        request.session['location'] = "NYC"
        request.session['newVar'] = "ya b we did eeet"
    return render(request, 'store.html', context)