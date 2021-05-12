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
    path('categories/', views.categories),
    path('createCat/', views.createCat),
    path('category/<int:category_id>/viewCat/', views.viewCat),
    path('category/<int:category_id>/updateCat/', views.updateCat),
    path('category/<int:category_id>/deleteCat/', views.deleteCat),
    path('shops/', views.shops),
    path('createShop', views.createShop),
    path('shop/<int:shop_id>/viewShop/', views.viewShop),
    path('shop/<int:shop_id>/updateShop', views.updateShop),
    path('shop/<int:shop_id>/deleteShop', views.deleteShop),
    path('products/', views.products),
    path('createProd/', views.createProd),
    path('product/<int:product_id>/viewProd', views.viewProd),
    path('product/<int:product_id>/updateProd', views.updateProd),
    path('product/<int:product_id>/deleteProd', views.deleteProd),
]