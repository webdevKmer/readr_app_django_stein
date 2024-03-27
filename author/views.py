from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author

# Create your views here.

def index(request):
    authors = Author.objects.order_by('-id')
    return render(request, 'author/index.html', {
        'authors': authors
    })

def add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author:index')
    else :
        form = AuthorForm()
    return render(request, 'author/add.html', {
        'form': form
    })