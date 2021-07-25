from django.urls import path
from apps.comments.views import *


urlpatterns = [
    path('<int:id>/', comment_index, name='comment_index'),
    path('update/<int:id>/', update_comment, name='update_comment'),
    path('delete/<int:id>/', delete_comment, name='delete_comment'),
]