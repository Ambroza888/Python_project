from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView



def log_reg(request):
  return render(request, "my_apps/log_reg.html")

def reg_in_data(request):
  errors = User.objects.basic_validator_user(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      # messages.error(request, value)
      messages.add_message(request, messages.ERROR, value, extra_tags="register")
    return redirect('/log_reg')
  else:
    name = request.POST['name']
    alias = request.POST['alias']
    email = request.POST['email']
    password = request.POST['password']
    re_password = request.POST['re_password']
    pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    new_user = User.objects.create(name=name,alias=alias,email=email,password=pw_hash)
    id = new_user.id
    request.session['user_id'] = id
    return redirect("/img_sharing")

def log_in_data(request):
  user = User.objects.filter(email=request.POST['email'])
  if user:
    logged_user = user[0]
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
      request.session['user_id'] = logged_user.id
      return redirect("/img_sharing")
    else:
      messages.add_message(request, messages.ERROR, "Invalid information", extra_tags='login')
  return redirect('log_reg')

def index(request):
    return render(request, "my_apps/index.html")

def contact(request):
  return render(request, "my_apps/contact.html")

def reviews(request):
  context = {
    "all_reviews": Review.objects.order_by("-created_at")
  }
  return render(request, 'my_apps/reviews.html', context)

def taking_review(request):
  errors = Review.objects.basic_validator_review(request.POST)
  if len(errors) > 0:
    for key,value in errors.items():
      messages.error(request, value)
    return redirect('/reviews')
  else:
    name = request.POST['name']
    rating = request.POST['rating']
    text = request.POST['review_text']
    add_review = Review.objects.create(name=name,text=text,rating=rating)
  return redirect("/reviews")

def img_sharing(request):
  try:
    context = {
      "user": User.objects.get(id=int(request.session['user_id']))
    }

    return render(request, "my_apps/img_sharing.html", context)
  except:
    return render(request, "my_apps/img_sharing.html")


def uploading_file(request):
  uploaded_file = request.FILES['document']
  fs = FileSystemStorage()
  fs.save(uploaded_file.name, uploaded_file)
  return redirect('/img_sharing')


def clean_session(request):
  request.session.clear()
  return redirect('/img_sharing')



def cars_home(request):
  return render(request, "my_apps/cars_home.html")