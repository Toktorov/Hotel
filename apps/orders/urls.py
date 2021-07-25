from django.urls import path
from apps.orders import views


urlpatterns = [
    path('', views.OrderIndexView.as_view(), name = 'order_index'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(), name='detail_order'),
    path('create/', views.create_order, name='create_order'),
]