from django.db import models
from django.utils import timezone

class Hero(models.Model):

    name = models.CharField(verbose_name="Hero name",max_length=50)

    def __str__(self):
        return self.name

class Map(models.Model):

    name = models.CharField(verbose_name="Map name",max_length=50)

    def __str__(self):
        return self.name

class Accounts(models.Model):

    name = models.CharField(verbose_name='name', max_length=255)

    def __str__(self):
        return self.name

class RankTable(models.Model):

    tab  = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    rank = models.IntegerField()
    variation = models.IntegerField()
    map  = models.ForeignKey(Map, on_delete=models.CASCADE)
    heros= models.ManyToManyField('Hero')

    def getHerosstr(self):
        return ",".join([i.name for i in self.heros.all()])

    def herosSplit(self):
        return [i.name for i in self.heros.all()]

    def herosId(self):
        return ",".join([i.name for i in self.heros.all()])

    def __str__(self):
        return "{} : {} on {} ".format(self.date,self.rank,self.map)
