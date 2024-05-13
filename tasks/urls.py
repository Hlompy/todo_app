from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail'),
    path('new_task/', TaskCreate.as_view(), name='new_task'),
    path('update_task/<int:pk>', TaskUpdate.as_view(), name='update_task'),
    path('delete_task/<int:pk>', TaskDelete.as_view(), name='delete_task'),
]
