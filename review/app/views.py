from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User


def index(request):
    if 'email' in request.session:
        return HttpResponseRedirect("/success")
    else:
        return render(request, "app/index.html")


def showsign(request):
    if 'email' in request.session:
        return HttpResponseRedirect("/success")
    else:
        return render(request, "app/login.html")


def login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = User.objects.get(email=email, password=password)
        request.session['email'] = email
        request.session['name'] = user.name
        return HttpResponseRedirect("/success")
    except User.DoesNotExist:
        request.session['wrong'] = "true"
        return HttpResponseRedirect("/")


def google(request):
    gemail = request.POST['gemail']
    gname = request.POST['gname']
    request.session['email'] = gemail
    request.session['name'] = gname
    return HttpResponseRedirect("/success")


def success(request):
    return render(request, "app/product.html")


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/success")


def register(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    phone = request.POST['phone']
    if repassword == password:
        try:
            user = User.objects.get(email=email)
            request.session['already'] = "true"
            return HttpResponseRedirect("/signup")
        except User.DoesNotExist:
            User.objects.create(
                name=name, email=email, password=password, phone=phone)
            request.session['registered'] = "true"
            return HttpResponseRedirect("/")
    else:
        request.session["double"] = "true"
        return render(request, "app/login.html")
