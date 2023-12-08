"""
URL configuration for djangodazzle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from djangodazzle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_recipes, name='Welcome'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('all_recipes/', views.all_recipes, name='all_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('edit-recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('accounts/login/profile/', views.profile_detail, name='profile_detail'),
    path('accounts/login/profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('recipes/breakfast/', views.breakfast_recipes, name='breakfast_recipes'),
    path('recipes/lunch/', views.lunch_recipes, name='lunch_recipes'),
    path('recipes/dinner/', views.dinner_recipes, name='dinner_recipes'),
    path('recipes/dessert/', views.dessert_recipes, name='dessert_recipes'),
    path('profile/', views.profile_detail, name='profile'),
]

