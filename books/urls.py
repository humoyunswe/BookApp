from django.urls import path, include
from .views import BookList, BookUpdate, BookDestroy

urlpatterns = [
    path('api/v1/books/', BookList.as_view(), name='book-list'),
    path('api/v1/books/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('api/v1/bookdelete/<int:pk>/', BookDestroy.as_view(), name='book-destroy'),
    path('api/v1/drf-auth',include('rest_framework.urls')),
]