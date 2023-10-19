from django.urls import path
from .views import *

urlpatterns = [
    path('', api_overview),

    path('all_posts/', get_all_posts),
    path('create_post/', create_post),
    path('update/<int:pk>/', update_post, name='update-post'),
    path('delete/<int:pk>/', delete_post, name='delete-post'),

    path('all_categories/', get_all_categories),
    path('create_category/', create_category),
    path('update_category/<int:pk>/', update_category, name='update-category'),
    path('delete_category/<int:pk>/', delete_category, name='delete-category'),


]