from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('register/', views.register),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    # path('profile/', views.profile),
    path('category/', views.categories),
    path('category/createCat/', views.createCat),
    path('shop/', views.shops),
    path('shop/createShop/', views.createShop),
    path('shop/<int:shop_id>/editShop/', views.viewShop),
    path('shop/<int:shop_id>/updateShop/', views.updateShop),
    path('shop/<int:shop_id>/deleteShop/', views.deleteShop),
    path('product/', views.products),
    path('product/createProd/', views.createProd),
    path('product/<int:product_id>/editProd/', views.viewProd),
    path('product/<int:product_id>/addCat/', views.addProdCat),
    path('product/<int:product_id>/updateProd/', views.updateProd),
    path('product/<int:product_id>/deleteProd/', views.deleteProd),
]