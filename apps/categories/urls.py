from django.urls import path
from apps.categories import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='index_category'),
    path('detail/<str:slug>/', views.CategoryDetailView.as_view(), name='detail_category'),
    path('update/<str:slug>/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('delete/<str:slug>/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('create/', views.CategoryCreateView.as_view(), name='create_category'),
]