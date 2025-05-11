from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.post_list,name='post-list'),
    path('<slug:slug>',views.post_detail,name='post-detail'),
    path('delete/<slug:slug>',views.delete_post,name='delete-post'),
    path('update/<slug:slug>',views.update_post,name='update-post'),
]
