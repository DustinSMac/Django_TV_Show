from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('shows/new',new),
    path('shows',shows),
    path('shows/newShow',newShow),
    path('shows/<int:show_id>',ShowPage),
    path('shows/<int:show_id>/edit',EditShow),
    path('shows/<int:show_id>/delete',DeleteShow),
    path('shows/<int:show_id>/editShow',editShowPage),
]
