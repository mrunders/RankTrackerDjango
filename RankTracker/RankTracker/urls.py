
from django.contrib import admin
from django.urls import path, re_path, include

from RankTrackerImpl.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tracker/', index),

    path('maps/', addMap),
    path('heros/', addHero),
    path('tabs/', addTabs),
    path('reset/', reset),

    re_path(r'^api-auth/', include('rest_framework.urls'))
]
