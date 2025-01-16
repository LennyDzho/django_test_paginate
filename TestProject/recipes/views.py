from itertools import count

from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipes(request):
    recipe_name = request.path.strip('/')
    recipe = dict(DATA.get(recipe_name))
    servings = int(request.GET.get('servings', 1))
    if not recipe:
        return HttpResponse("Рецепт не найден!", status=404)

    for ingredient in recipe:
        new_count = recipe[ingredient] * servings
        recipe[ingredient] = f"{new_count:.1f}"


    context = {
        'recipe_name': recipe_name,
        'ingredients': recipe,
        'servings': servings
    }

    return render(request, 'recipes.html', context)


