import os

from django.core.paginator import Paginator
from django.shortcuts import render
import csv



def load_csv_data(file_path):
    global DATA
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        DATA = [row for row in reader]

    return DATA

DATA = load_csv_data('stations/data-398-2018-08-30.csv')

def get_paginate_stations(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(DATA, 10)
    page = paginator.get_page(page_num)
    content = {
        'page': page
    }
    return render(request, 'stations.html', content)


