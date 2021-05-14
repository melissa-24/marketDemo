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
    path('profile/createCat/', views.createCat),
    path('profile/category/<int:category_id>/viewCat/', views.viewCat),
    path('profile/category/<int:category_id>/updateCat/', views.updateCat),
    path('profile/category/<int:category_id>/deleteCat/', views.deleteCat),
    path('profile/shops/', views.shops),
    path('profile/createShop/', views.createShop),
    path('profile/shop/<int:shop_id>/viewShop/', views.viewShop),
    path('profile/shop/<int:shop_id>/updateShop', views.updateShop),
    path('profile/shop/<int:shop_id>/deleteShop', views.deleteShop),
    path('products/', views.products),
    path('profile/createProd/', views.createProd),
    path('profile/product/<int:product_id>/viewProd', views.viewProd),
    path('profile/product/<int:product_id>/updateProd', views.updateProd),
    path('profile/product/<int:product_id>/deleteProd', views.deleteProd),
]