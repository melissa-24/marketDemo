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
        'footer': FOOTER,
        'accts': Acct.objects.all()
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

# -------Hidden Create Acct Landing page-------
def acct(request):
    context = {
        'accts': Acct.objects.all().values(),
    }
    return render(request, 'accts.html', context)

# -------Hidden Create Acct Route-------

def createAcct(request):
    Acct.objects.create(
        typeName=request.POST['typeName'],
    )
    return redirect('/accts/')


# -----------------Private pages and routes-----------------

# -------Dashboard Landing Page-------
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    ownerShops = Shop.objects.filter(user_id=request.session['user_id'])
    prods = Product.objects.filter(theOwner=request.session['user_id'])
    ownerProds = Product.objects.filter(theOwner = user)
    # print(user.acct_id)
    if user.acct_id == 1:
        context = {
            'footer': FOOTER,
            'user': user,
            'allProd': Product.objects.all().values(),
            'shops': Shop.objects.all().values(),
            'cats': Category.objects.all().values(),
        }
        return render(request, 'userSide/dashboard.html', context)
    else:
        context = {
            'footer': FOOTER,
            'user': user,
            'ownerShops': ownerShops,
            'ownerProds': ownerProds,
            'prods':prods,
        }
        return render(request, 'ownerSide/ownerDash.html', context)


# -----------------Owner Private pages and routes-----------------

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
    return render(request, 'ownerSide/shops.html', context)

# -------Create Shop Route-------
def createShop(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Shop.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/shop/')
    Shop.objects.create(
        shopName=request.POST['shopName'],
        shopDescription=request.POST['shopDescription'],
        user_id=request.POST['user'],
    )
    return redirect('/shop/')

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
    return render(request, 'ownerSide/edit/editShop.html', context)

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
    return render(request, 'ownerSide/categories.html', context)

# -------Create Category Route-------
def createCat(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Category.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/category/')
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
    return render(request, 'ownerSide/products.html', context)

# -------Create Product Route-------
def createProd(request):
    if 'user_id' not in request.session:
        return redirect('/')
    Product.objects.create(
        itemName=request.POST['itemName'],
        itemDescription=request.POST['itemDescription'],
        itemPrice=request.POST['itemPrice'],
        itemImg=request.POST['itemImg'],
        itemCount=request.POST['itemCount'],
    )
    return redirect('/product/')

# -------Edit Product Landing Page-------
def viewProd(request, product_id):
    user = User.objects.get(id=request.session['user_id'])
    ownerShops = Shop.objects.filter(user_id=request.session['user_id'])
    oneProd = Product.objects.get(id=product_id)
    allCats = Category.objects.all().values()
    context = {
        'editProd': oneProd,
        'user': user,
        'ownerShops':ownerShops,
        'allCats': allCats,
        'users': User.objects.filter(acct_id=2)
    }
    return render(request, 'ownerSide/edit/editProducts.html', context)
# -------Update Product Dashboard Route-------
def updateProd(request, product_id):
    toUpdate = Product.objects.get(id=product_id)
    toUpdate.itemName = request.POST['itemName']
    toUpdate.itemDescription = request.POST['itemDescription']
    toUpdate.itemPrice = request.POST['itemPrice']
    toUpdate.itemImg = request.POST['itemImg']
    toUpdate.itemCount = request.POST['itemCount']
    toUpdate.save()

    return redirect('/dashboard/')

# -------Delete Product Dashboard Route-------
def deleteProd(request, product_id):
    toDelete = Product.objects.get(id=product_id)
    toDelete.delete()

    return redirect('/dashboard/')

# -------Add Shop to Product Route-------
def assignShop(request, product_id):
    product = Product.objects.get(id=product_id)
    aShop = Shop.objects.get(id=request.POST['shop_id'])
    product.shop.add(aShop)
    return redirect('/dashboard/')

# -------Add Category to Product Route-------
def assignCat(request, product_id):
    product = Product.objects.get(id=product_id)
    cats = Category.objects.get(id=request.POST['category_id'])
    product.categories.add(cats)
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

# -------Edit New Product Landing-------
def viewNewProd(request, product_id):
    user = User.objects.get(id=request.session['user_id'])
    oneProd = Product.objects.get(id=product_id)
    ownerShops = Shop.objects.filter(user_id=request.session['user_id'])
    context = {
        'editProd': oneProd,
        'user': user,
        'ownerShops': ownerShops,
        'users': User.objects.filter(acct_id=2)
    }
    return render(request, 'ownerSide/edit/assignProd.html', context)

# -------Update New Product Route-------
def updateNewProd(request, product_id):
    toUpdate = Product.objects.get(id=product_id)
    toUpdate.itemName = request.POST['itemName']
    toUpdate.itemDescription = request.POST['itemDescription']
    toUpdate.itemPrice = request.POST['itemPrice']
    toUpdate.itemImg = request.POST['itemImg']
    toUpdate.itemCount = request.POST['itemCount']
    toUpdate.save()

    return redirect('/product/')

# -----------------Customer Private pages and routes-----------------

# -------View Shop Items Landing-------
def viewShopItems(request, shop_id):
    user = User.objects.get(id=request.session['user_id'])
    oneShop = Shop.objects.get(id=shop_id)
    prods = Product.objects.all().values()    
    context = {
        'footer': FOOTER,
        'user': user,
        'oneShop': oneShop,
        'prods':prods,
    }
    return render(request, 'userSide/userViewShopProd.html', context)

# -------View Category Items Landing-------
def viewCatItems(request):
    pass

# -------User View One Product Landing-------
def viewItem(request, product_id):
    user = User.objects.get(id=request.session['user_id'])
    oneProd = Product.objects.get(id=product_id)
    context = {
        'footer': FOOTER,
        'user': user,
        'oneProd': oneProd,

    }
    return render(request, 'userSide/userViewProd.html', context)