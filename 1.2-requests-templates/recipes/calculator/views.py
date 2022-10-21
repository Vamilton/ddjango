from django.shortcuts import render, reverse

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


def cook_book(request):
    template_name = 'calculator/index.html'
    recipes = {
        'Омлет': DATA['omlet'],
        'Паста': DATA['pasta'],
        'Бутерброд': DATA['buter']
    }
    context = {
        'recipe': recipes
    }
    return render(request, template_name, context)


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def omlet(request):
    template_name = 'calculator/omlet.html'
    pers = int(request.GET.get('servings', 1))
    omlet = {key: round(value*pers, 2) for (key,value) in DATA['omlet'].items()
    }
    context = {
        'om_omlet': omlet
    }
    return render(request, template_name, context)


def pasta(request):
    template_name = 'calculator/pasta.html'
    pers = int(request.GET.get('servings', 1))
    pasta = {key: round(value*pers, 2) for (key,value) in DATA['pasta'].items()
    }
    context = {
        'pa_pasta': pasta
    }
    return render(request, template_name, context)

def buter(request):
    template_name = 'calculator/buter.html'
    pers = int(request.GET.get('servings', 1))
    buter = {key: round(value*pers, 2) for (key,value) in DATA['buter'].items()
    }
    context = {
        'bu_buter': buter
    }
    return render(request, template_name, context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
