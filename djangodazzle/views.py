from datetime import timezone
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Recipe, Comment, UserProfile
from .forms import RecipeForm, CommentForm, UserProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('edit_profile')  # Redirect to all_recipes after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edit_profile')  # Redirect to all_recipes after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def all_recipes(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(title__icontains=query)

    return render(request, 'all_recipes.html', {'recipes': recipes})


@login_required
def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            new_recipe = recipe_form.save()
            return redirect('all_recipes')
    else:
        recipe_form = RecipeForm()
    return render(request, 'create_recipe.html', {'recipe_form': recipe_form})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    comments = recipe.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        comment_form = CommentForm()

    return render(request, 'recipe_detail.html', {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            # Delete the recipe if required
            recipe.delete()
            return HttpResponseRedirect('all_recipes')

        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            updated_recipe = recipe_form.save()
            return redirect('profile')
    else:
        recipe_form = RecipeForm(instance=recipe)

    return render(request, 'edit_recipe.html', {'recipe_form': recipe_form, 'recipe_id': recipe_id})

@login_required
def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')  # Redirect to profile detail after saving profile
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def profile_detail(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
        try:
            profile = UserProfile.objects.get(user=request.user)
            user_recipes = Recipe.objects.filter(userprofile=profile)
            return render(request, 'profile_detail.html', {'profile': profile, 'user_recipes': user_recipes})
        except UserProfile.DoesNotExist:
            return redirect('edit_profile')
        return render(request, 'profile_detail.html', {'profile': profile, 'user_recipes': user_recipes})
    except UserProfile.DoesNotExist:
        return redirect('edit_profile')


def breakfast_recipes(request):
    breakfast_recipes = Recipe.objects.filter(category='breakfast')
    return render(request, 'breakfast.html', {'recipes': breakfast_recipes})


def lunch_recipes(request):
    lunch_recipes = Recipe.objects.filter(category='lunch')
    return render(request, 'lunch.html', {'recipes': lunch_recipes})


def dinner_recipes(request):
    dinner_recipes = Recipe.objects.filter(category='dinner')
    return render(request, 'dinner.html', {'recipes': dinner_recipes})


def dessert_recipes(request):
    dessert_recipes = Recipe.objects.filter(category='dessert')
    return render(request, 'desserts.html', {'recipes': dessert_recipes})


