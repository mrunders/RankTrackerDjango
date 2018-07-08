from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .stats import *

from .forms import *
from .models import *

def index(request):

    if request.method == 'POST':
        form = RankTableForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            
            try:
                obj.variation = obj.rank - RankTable.objects.latest('id').rank
            except:
                obj.variation = 0
            
            obj.save()
            obj = RankTable.objects.latest('id')
            obj.heros.set(form.cleaned_data['heros'])

            for hero in form.cleaned_data['heros']:
                h = Hero.objects.get(name=hero.name)
                h.occurence = h.occurence + 1
                h.save()

            obj.save()

    else:
        form = RankTableForm()

    tabs = Accounts.objects.all()
    table = RankTable.objects.all().order_by('-id')

    stats = Stats(RankTable)
    stats.evaluate()

    return render(request, 'index.html', {
        'tabs':tabs, 'table':table, 
        'form':form, 'action': '/tracker/',
        'heroList': HeroListForm(),
        'stats': stats
    })

def addElemennt(request, Table, Form, action):
    
    if request.method == 'POST':

        form = Form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Form()

    table = Table.objects.all()
    return render(request, 'elements.html', {'table':table, 'form':form, 'action': action})


def addMap(request):
    return addElemennt(request, Map, MapForm, '/map/')

def addHero(request):
    return addElemennt(request, Hero, HeroForm, '/heros/')

def addTabs(request):
    return addElemennt(request, Accounts, TabsForm, '/tabs/')

def reset(request):

    for map in settings.MAPS:
        if not Map.objects.filter(name=map).exists():
            newmap = Map(name=map)
            newmap.save()

    for hero in settings.HEROS:
        if not Hero.objects.filter(name=hero).exists():
            newhero = Hero(name=hero)
            newhero.save()
        else:
            h = Hero.objects.get(name=hero)
            h.save()

    for acc in settings.ACCOUNTS:
        if not Accounts.objects.filter(name=acc).exists():
            a = Accounts(name=acc)
            a.save()    

    return HttpResponse('done')