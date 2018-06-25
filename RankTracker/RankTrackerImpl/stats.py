
from .models import *

class Stats:

    db = None
    res = {}

    def __init__(self, dbmodel):
        self.change(dbmodel)

    def change(self, dbmodel):
        self.db = dbmodel
        self.res = {}

    def evaluate(self):
        self.res['Games Lose'] = self.db.objects.filter(variation__lt=0).count()
        self.res['Games Win']  = self.db.objects.filter(variation__gt=0).count()
        self.res['Games Draw'] = self.db.objects.filter(variation=0).count()
        self.res['Total games']= self.db.objects.count()

    def __str__(self):

        tr = ''
        for key,item in self.res.items():
            tr += '<th>{}</th><td>{}</td>'.format(key,item)

        return '<table><tr>{}</tr></table>'.format(tr)
