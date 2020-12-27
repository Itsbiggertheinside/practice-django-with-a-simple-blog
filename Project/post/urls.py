from django.urls import path
from . import views

urlpatterns = [
    path('write/', views.post_write, name='post_write'),
    # path('delete/', views.post_delete, name='post_delete'),

    path('write/<slug:url_text>/', views.post_update, name='post_update'),
    path('<slug:url_text>/', views.post_detail, name='post_detail'),
]
