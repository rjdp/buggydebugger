from django.shortcuts import render
from django.views import generic
from .models import MyModel
# Create your views here.

class BlogIndex(generic.ListView):
	queryset = MyModel.objects.all()
	template_name = "home.html"
