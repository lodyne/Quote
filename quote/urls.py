from django.urls import path
from . import views
from .views import IndexView
urlpatterns = [
    path('',views.home,name='index'),
    # path('index/',IndexView.as_view(),name='index'),
    path('index/',views.index, name='index'),
    path('another/',views.another, name='another'),
    path('another1/',views.another1, name='another1'),
]