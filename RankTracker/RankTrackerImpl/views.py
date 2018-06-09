from django.shortcuts import render
from .forms import *
from .models import *

def index(request):

    if request.method == 'POST':
        form = RankTableForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            
            try:
                obj.variation = obj.rank - RankTable.objects.latest('id').rank
            except:
                obj.variation = obj.rank
            
            obj.save()
            obj = RankTable.objects.latest('id')
            obj.heros.set(form.cleaned_data['heros'])
            obj.save()

    else:
        form = RankTableForm()

    tabs = Accounts.objects.all()
    table = RankTable.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'tabs':tabs, 'table':table, 
        'form':form, 'action': '/tracker/',
        'heroList': HeroListForm(),
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
