from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

# View to list all recipes

def index(request):
    return render(request,'index.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

# View to add a new recipe
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
