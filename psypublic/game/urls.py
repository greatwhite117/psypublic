from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?:intro-(?P<num>\d+))/$', views.intro, name='intro'),
    url(r'(?:practice-(?P<num>\d+))/$', views.practice, name='practice'),
    url(r'(?:real_game-(?P<num>\d+))/$', views.real_game, name='real_game'),
    url(r'^hidden$', views.downloadcsv, name='downloadcsv')
]