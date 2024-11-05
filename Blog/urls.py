from django.urls import path
from .import views
urlpatterns = [
    path('',views.BlogShow, name='home'),
    path('allpost/',views.All_Post,name='postlist'),
    path('post_details/<slug:slug>/',views.Post_details,name='post_detail')

]