from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_comments),
    path('create', create_comment),
    path('update/pk', update_comment),
    path('delete/pk', delete_comment)
]