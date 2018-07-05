
from .models import *
import math

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
        self.res['Winrate']    = '{}%'.format(math.floor((self.res['Games Win'] / self.res['Total games'])* 100))

    def __str__(self):

        tr = ''
        row = 0
        for key,item in self.res.items():
            tr += '<th>{}</th><td>{}</td>'.format(key,item)
            if row == 2:
                row = 0
                tr += '</tr><tr>'
            else:
                row += 1

        return '<table><tr>{}</tr></table>'.format(tr)
