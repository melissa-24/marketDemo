from django.contrib import admin
from .models import Acct, User, Shop, Product, Category

admin.site.register(Acct)
admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)