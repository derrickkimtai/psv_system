from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cashier_dashboard/', views.cashier_dashboard, name='cashier_dashboard'),
    path('cashier_signup/', views.cashier_signup, name='cashier_signup'),
    path('cashier_login/', views.cashier_login, name='cashier_login'),
    path('cut-ticket/', views.cut_ticket, name='cut_ticket'),
    path('load-cars/', views.load_cars, name='load_cars'),  # For AJAX call to load cars
    path('load-seats/', views.load_seats, name='load_seats'),  # For AJAX call to load available seats
    path('get_stages/<int:route_id>/', views.get_stages, name='get_stages'),
    path('get_price/<int:route_id>/<int:stage_id>/', views.get_price, name='get_price'),
    path('all_tickets/', views.all_tickets, name='all_tickets'),
]