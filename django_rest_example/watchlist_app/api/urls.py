from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
]
