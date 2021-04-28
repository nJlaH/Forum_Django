from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:a_id>/add_comment/', views.add_comment, name='add_comment'),
    path('add_article/', views.add_article, name='add_article'),
    path('<int:a_id>', views.certain_article, name='certain_article'),
]