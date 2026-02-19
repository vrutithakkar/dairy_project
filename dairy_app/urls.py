from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.home, name="home"),

    # auth (only login/logout)
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('farmers/', views.farmer_list, name="farmer_list"),
    path('farmers/add/', views.add_farmer, name="add_farmer"),
    path('farmers/delete/<int:id>/', views.delete_farmer, name="delete_farmer"),

    path('staff/', views.staff_list, name="staff_list"),
    path('staff/add/', views.add_staff, name="add_staff"),

    path('animals/', views.animal_list, name="animal_list"),
    path('animals/add/', views.add_animal, name="add_animal"),

    path('products/', views.product_list, name="product_list"),
    path('products/add/', views.add_product, name="add_product"),

    path('bills/', views.bill_list, name="bill_list"),
    path('bills/add/', views.add_bill, name="add_bill"),
]
