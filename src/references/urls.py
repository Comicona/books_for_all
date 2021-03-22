from django.urls import path
from . import views


app_name = 'references'

urlpatterns = [
    path('authors/', views.AuthorsList.as_view(), name='authors-list'),
    path('genres/', views.GenresList.as_view(), name='genres-list'),
    path('series/', views.SeriesList.as_view(), name='series-list'),
    path('publishers/', views.PublishersList.as_view(), name='publishers-list'),
    path('categories/', views.CategoriesList.as_view(), name='categories-list'),
    path('formats/', views.FormatsList.as_view(), name='formats-list'),

    path('authors-delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),
    path('genres-delete/<int:pk>/', views.GenreDelete.as_view(), name='genre-delete'),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name='series-delete'),
    path('publishers-delete/<int:pk>/', views.PublisherDelete.as_view(), name='publisher-delete'),
    path('categories-delete/<int:pk>/', views.CategoryDelete.as_view(), name='category-delete'),
    path('formats-delete/<int:pk>/', views.FormatDelete.as_view(), name='format-delete'),
    
    path('authors-update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('genres-update/<int:pk>/', views.GenreUpdate.as_view(), name='genre-update'),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(), name='series-update'),
    path('publishes-update/<int:pk>/', views.PublisherUpdate.as_view(), name='publisher-update'),
    path('categories-update/<int:pk>/', views.CategoryUpdate.as_view(), name='category-update'),
    path('formats-update/<int:pk>/', views.FormatUpdate.as_view(), name='format-update'),
    
    path('authors-create/', views.AuthorCreate.as_view(), name='author-create'),
    path('genres-create/', views.GenreCreate.as_view(), name='genre-create'),
    path('series-create/', views.SeriesCreate.as_view(), name='series-create'),
    path('publishers-create/', views.PublisherCreate.as_view(), name='publisher-create'),
    path('categories-create/', views.CategoryCreate.as_view(), name='category-create'),
    path('bformats-create/', views.FormatCreate.as_view(), name='format-create')
]