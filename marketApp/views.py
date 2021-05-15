from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Acct, User, Shop, Category, Product
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
        'footer': FOOTER,
        'accts': Acct.objects.all()
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
        password = hashedPw,
        acct_id=request.POST['acct']
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
    shops = Shop.objects.all().values()
    ownerShops = Shop.objects.filter(user_id=request.session['user_id'])
    prods = Product.objects.all().values()
    ownerProds = Product.objects.filter(theOwner_id=request.session['user_id'])
    # print(user.acct_id)
    if user.acct_id == 1:
        context = {
            'footer': FOOTER,
            'user': user,
            'allProd': Product.objects.all().values(),
        }
        return render(request, 'dashboard.html', context)
    else:
        context = {
            'footer': FOOTER,
            'user': user,
            'ownerShops': ownerShops,
            'ownerProds': ownerProds,
        }
        return render(request, 'ownerDash.html', context)

# -------Create Shop Landing-------
def shops(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    shops = Shop.objects.all().values()
    context = {
        'footer': FOOTER,
        'user': user,
        'shops':shops,
        'users': User.objects.filter(acct_id=2),
    }
    return render(request, 'shops.html', context)

# -------Create Shop Route-------
def createShop(request):
    if 'user_id' not in request.session:
        return redirect('/')
    Shop.objects.create(
        shopName=request.POST['shopName'],
        shopDescription=request.POST['shopDescription'],
        user_id=request.POST['user'],
    )
    return redirect('/shops/')

# -------View Shop Landing Page-------
def viewShop(request,shop_id):
    user = User.objects.get(id=request.session['user_id'])
    oneShop = Shop.objects.get(id=shop_id)
    cats = Category.objects.all().values()
    prods = Product.objects.all()
    context = {
        'editShop': oneShop,
        'user': user,
        'cats': cats,
        'prods': prods,
        'users': User.objects.filter(acct_id=2)
    }
    return render(request, 'editShop.html', context)

# -------Update Shop Route-------
def updateShop(request, shop_id):
    toUpdate = Shop.objects.get(id=shop_id)
    toUpdate.shopName = request.POST['shopName']
    toUpdate.shopDescription = request.POST['shopDescription']
    toUpdate.user_id = request.POST['user_id']
    toUpdate.save()

    return redirect('/dashboard/')

# -------Delete Shop Route-------
def deleteShop(request, shop_id):
    toDelete = Shop.objects.get(id=shop_id)
    toDelete.delete()

    return redirect('/dashboard/')

# -------User Profile Landing Page-------
def profile(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'footer': FOOTER
    }
    return render(request, 'profile.html', context)

# -------Categories Landing Page-------
def categories(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    cats = Category.objects.all().values()
    context = {
        'footer': FOOTER,
        'user': user,
        'cats': cats,
        'users': User.objects.filter(acct_id=2),
    }
    return render(request, 'categories.html', context)

# -------Create Category Route-------
def createCat(request):
    if 'user_id' not in request.session:
        return redirect('/')
    Category.objects.create(
        catName=request.POST['catName'],
        theUser_id=request.POST['theUser'],
    )
    return redirect('/category/')

# -------Products Landing Page-------
def products(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    prods = Product.objects.all().values()
    shops = Shop.objects.all().values()
    cats = Category.objects.all().values()
    context ={
        'footer': FOOTER,
        'user': user,
        'prods':prods,
        'shops':shops,
        'cats': cats,
        'users': User.objects.filter(acct_id=2),
    }
    return render(request, 'products.html', context)
    

# -------Create Product Route-------
def createProd(request):
    if 'user_id' not in request.session:
        return redirect('/')
    Product.objects.create(
        itemName=request.POST['itemName'],
        itemDescription=request.POST['itemDescription'],
        itemPrice=request.POST['itemPrice'],
        itemImg=request.POST['itemPrice'],
        itemCount=request.POST['itemPrice'],
        theOwner_id=request.POST['theOwner'],
        shop_id=request.POST['shop'],
    )
    return redirect('/product/')

# -------View Product Landing Page-------
def viewProd(request, product_id):
    user = User.objects.get(id=request.session['user_id'])
    oneProd = Product.objects.get(id=product_id)
    context = {
        'editProd': oneProd,
        'user': user,
        'users': User.objects.filter(acct_id=2)
    }
    return render(request, 'editProducts.html', context)

# -------Add Category to Product Route-------
def addProdCat(request):
    pass

# -------Update Product Route-------
def updateProd(request, product_id):
    toUpdate = Product.objects.get(id=product_id)
    toUpdate.itemName = request.POST['itemName']
    toUpdate.itemDescription = request.POST['itemDescription']
    toUpdate.itemPrice = request.POST['itemPrice']
    toUpdate.itemImg = request.POST['itemImg']
    toUpdate.itemCount = request.POST['itemCount']
    toUpdate.theOwner_id = request.POST['theOwner']
    toUpdate.shop_id = request.POST['shop']
    toUpdate.save()

    return redirect('/dashboard/')

# -------Delete Product Route-------
def deleteProd(request):
    pass