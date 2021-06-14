from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('log', views.log, name='log'),
	path('logout', views.logout, name = 'logout'),
	path('main/', views.main, name = 'main/'),
	path('add_item', views.add_item, name = 'add_item'),
	path('add_budget', views.add_budget, name = 'add_budget'),
	path('transaction_success/', views.transaction_success, name = "transaction_success/"),
	path('budget_success/', views.budget_success, name = "budget_success/")
]