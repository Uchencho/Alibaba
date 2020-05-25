from django.urls import path, include

from .views import (ProductListView, 
                    ProductDetailView,
                    ProductFeaturedListView,
                    ProductFeaturedDetailView)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    # path('<int:pk>/', ProductDetailView.as_view()),
    path('<slug:slug>/', ProductDetailView.as_view()),
]