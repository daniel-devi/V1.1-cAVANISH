from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.home, name='home'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('room/<int:room_id>/', views.room , name='room'),
    path('tenant/dasboard/', views.dashboard , name='dashboard'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
    #path('room/<id:room_id>/make-payment'),
]
