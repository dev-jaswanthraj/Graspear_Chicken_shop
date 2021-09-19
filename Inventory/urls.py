from django.urls import path
from .views import (
    home,
    calculator
)

urlpatterns = [
    path('', home, name='home'),
    path('result/', calculator, name='calculator')
]