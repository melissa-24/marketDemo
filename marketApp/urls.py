from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('logout/', views.logout),
    path('login/', views.login),
    path('signup/', views.signup),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('categories/', views.categories),
    path('createCat/', views.createCat),
    path('category/<int:category_id>/viewCat/', views.viewCat),
    path('category/<int:category_id>/updateCat/', views.updateCat),
    path('category/<int:category_id>/deleteCat/', views.deleteCat),
    path('products/', views.products),
    path('createProd/', views.createProduct),
    path('product/<int:product_id>/viewProd', views.viewProd),
    path('product/<int:product_id>/updateProd', views.updateProd),
    path('product/<int:product_id>/deleteProd', views.deleteProd),
]