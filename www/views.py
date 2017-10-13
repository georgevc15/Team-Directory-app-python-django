from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
	people = Person.objects.all()
	return render(request, 'index.html', {'people':people})

def detail(request, slug):
	person = Person.objects.get(slug=slug)
	return render(request, 'detail.html', {'person':person})


def edit(request, slug):
	person = Person.objects.get(slug=slug)
	if (request.method == 'POST'):
		#process the form
		form = PersonForm(data=request.POST, instance=person)
		if form.is_valid():
			form.save(commit = True)
		return redirect(reverse('detail', args=[slug]))
	else:
		person_dict = model_to_dict(person)
		form = PersonForm(person_dict)
		return render(request, 'edit.html', {'form':form})

def verify_email(backend, user, response, *args, **kwargs):
	if backend.name == 'google-oauth2':
		existing_person = Person.objects.get(email=kwargs.get('detail').get('email'))
		if not existing_person:
			return HttpResponse("You do not have access!")


