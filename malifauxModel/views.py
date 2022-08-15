from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from . import models


# Create your views here.
class DetailView(generic.DetailView):
    model = models.MalifauxModel
    template_name = 'model.html'