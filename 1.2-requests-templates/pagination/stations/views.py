from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    my_bus = []
    page_number = int(request.GET.get('page', 1))
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            my_bus.append(row)
    pagi = Paginator(my_bus, 10)
    page = pagi.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    #
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
