from django.urls import path

from news.api.views import (
  ArticleListCreateAPIView, ArticleDetailAPIView, 
  JournalistListCreatApiView,
)


urlpatterns = [
  path(
    'articles/', 
    ArticleListCreateAPIView.as_view(), 
    name='article-list' ),

  path(
    'articles/<int:pk>/', 
    ArticleDetailAPIView.as_view(), 
    name='article-detail'),

  path(
    'journalists/',
    JournalistListCreatApiView.as_view(),
    name="article-list"
  ),

  # path(
  #   'journalist/<int:pk>/',
  #   ArticleD.as_view(),
  #   name="article-list"
  # ),

  

  

]
