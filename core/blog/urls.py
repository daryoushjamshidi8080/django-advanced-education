from importlib.resources import contents

from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"
urlpatterns = [
    path('about/', views.IndexViews, name="fbv-test"), # function base urls 
    path('test/', RedirectView.as_view(pattern_name = "blog:home", permanent=False), name='test'),
    # path('', TemplateView.as_view(template_name ='index.html', extra_context={'name': 'ali'}), name='home') # direct redirect 
    path('', views.IndexView.as_view(), name='home'),
    path('post/<int:pk>/', views.MyRedirectView.as_view(), name ='post_redirect'), # custom redirect 
    path('post-list/', views.PostList.as_view(), name='post-list'),
    path('post/form/', views.PostFormView.as_view(), name="post-form"),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete')
]
