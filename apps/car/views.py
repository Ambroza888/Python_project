from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView



def car(request):
  return render(request, "car/index.html")