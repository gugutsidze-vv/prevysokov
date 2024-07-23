from django.urls import path

from sections import views as sections

urlpatterns = [path('', sections.index, name='index')]
