from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Shop, Category, Product
import bcrypt

# -------Used for all pages-------
FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Market Place'
}

# -----------------User account pages and routes-----------------


# -------Main Landing page-------
def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

# -------User login route-------
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

# -------Register landing page-------
def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

# -------User register route-------
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

# -------User Logout-------
def logout(request):
    request.session.clear()
    return redirect('/')



# -----------------Private pages and routes-----------------

# -------User Dashboard Landing Page-------
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'footer': FOOTER,
        'user': user,
    }
    return render(request, 'dashboard.html', context)

# -------User Profile Landing Page-------
def profile(request):
    pass

# -------Categories Landing Page-------
def categories(request):
    pass

# -------Create Category Route-------
def createCat(request):
    pass

# -------View Category Landing Page-------
def viewCat(request):
    pass

# -------Update Category Route-------
def updateCat(request):
    pass

# -------Delete Category Route-------
def deleteCat(request):
    pass

# -------Shops Landing page-------
def shops(request):
    pass

# -------Create Shop Route-------
def createShop(request):
    pass

# -------View Shop Landing Page-------
def viewShop(request):
    pass

# -------Update Shop Route-------
def updateShop(request):
    pass

# -------Delete Shop Route-------
def deleteShop(request):
    pass

# -------Products Landing Page-------
def products(request):
    pass

# -------Create Product Route-------
def createProd(request):
    pass

# -------View Product Landing Page-------
def viewProd(request):
    pass

# -------Update Product Route-------
def updateProd(request):
    pass

# -------Delete Product Route-------
def deleteProd(request):
    pass