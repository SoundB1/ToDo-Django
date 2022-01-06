from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '' , views.HomeView.as_view(), name='home' ),
    path( 'todo', views.ToDoView.as_view(), name='todo'),
    path('delete/<pk>/', views.TaskDeleteView.as_view(), name='delete'),
    path('complete/<pk>/', views.TaskCompleteView.as_view(), name='complete'),
    path('edit/<pk>/', views.TaskEditView.as_view(), name='edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
