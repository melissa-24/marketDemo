from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Used for all pages
FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Market Place'
}

# -------Main Landing page (general user sign-in)-------
def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

# -------General user login route-------
def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/')

# -------Register landing page (for General Users)-------
def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

# -------General user register route-------
def register(request):
    if request.method == 'GET':
        return redirect('/signup/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/signup/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')