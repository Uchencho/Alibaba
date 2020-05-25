from django.urls import path, include

from .views import (ProductListView, 
                    ProductDetailView,
                    ProductFeaturedListView,
                    ProductFeaturedDetailView)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('featured/', ProductFeaturedListView.as_view(), name='featured'),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view(), name='featured-detail'),
    # path('<int:pk>/', ProductDetailView.as_view()),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
]