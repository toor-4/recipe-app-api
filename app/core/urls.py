from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    path('menu-items', views.MenuItemsView.as_view()),
    path('categories', views.CategoryView.as_view()),
    path('token-auth', obtain_auth_token)

]
