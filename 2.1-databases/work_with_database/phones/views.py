from django.shortcuts import render, redirect
from .models import Phone
import operator

def index(request):
    return redirect('catalog')


def show_catalog(request):
    type = request.GET.get('sort', 'name')
    p_phones = Phone.objects.all()
    if type == 'name':
        phones = sorted(p_phones, key=operator.attrgetter('name'))
    elif type == 'min_price':
        phones = sorted(p_phones, key=operator.attrgetter('price'))
    else:
        phones = Phone.objects.order_by('-price')
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug__iexact = slug)
    }
    return render(request, template, context)



