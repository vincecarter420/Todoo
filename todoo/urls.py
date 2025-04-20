from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<uuid:pk>/status/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<uuid:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
]