from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('register/', views.register),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    path('profile/', views.profile),
    path('category/', views.categories),
    path('category/createCat/', views.createCat),
    path('profile/category/<int:category_id>/viewCat/', views.viewCat),
    path('profile/category/<int:category_id>/updateCat/', views.updateCat),
    path('profile/category/<int:category_id>/deleteCat/', views.deleteCat),
    path('shop/', views.shops),
    path('shop/createShop/', views.createShop),
    path('shop/<int:shop_id>/editShop/', views.viewShop),
    path('shop/<int:shop_id>/updateShop/', views.updateShop),
    path('shop/<int:shop_id>/deleteShop/', views.deleteShop),
    path('products/', views.products),
    path('profile/createProd/', views.createProd),
    path('profile/product/<int:product_id>/viewProd/', views.viewProd),
    path('profile/product/<int:product_id>/updateProd/', views.updateProd),
    path('profile/product/<int:product_id>/deleteProd/', views.deleteProd),
]