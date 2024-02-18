from django.urls import path
from .views import ListBlog, DetailBlog

urlpatterns = [
    path('blog/', ListBlog.as_view(), name='blog'),
    path('blog/<slug:slug>/', DetailBlog.as_view(), name='detail_blog' )
]
