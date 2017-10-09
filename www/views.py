from django.shortcuts import render
from .models import Person
from .forms import PersonForm

# Create your views here.

def index(request):
	people = Person.objects.all()
	return render(request, 'index.html', {'people':people})

def detail(request, slug):
	person = Person.objects.get(slug=slug)
	return render(request, 'detail.html', {'person':person})


def edit(request, slug):
	form = PersonForm()
	return render(request, 'edit.html', {'form':form})
