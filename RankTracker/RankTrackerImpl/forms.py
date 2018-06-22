
from django import forms
from .models import *

from django.db.models import Max

class RankTableForm(forms.ModelForm):

    class Meta:
        model = RankTable
        exclude = ['date','variation','tab']

    def __init__(self, *args, **kwargs):
        super(RankTableForm, self).__init__(*args, **kwargs)

        try:
            self.fields['rank'].initial = RankTable.objects.latest('id').rank 
        except:
            self.fields['rank'].initial = 0
 
class MapForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = '__all__'

class HeroForm(forms.ModelForm):

    class Meta:
        model = Hero
        exclude = ['occurence']


class TabsForm(forms.ModelForm):

    class Meta:
        model = Accounts
        fields = '__all__'

class HeroListForm(forms.Form):
    
    heros = forms.ChoiceField(choices=[(h.id, h.name) for h in Hero.objects.all()])
