"""
URL configuration for vehiclemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

   path('register/',views.RegistrationView.as_view(),name='register'),
   path('login/',views.LoginView.as_view(),name='login'),
   path('logout/',views.log_out_view,name='logout'),
   path('vehicle/create/',views.VehicleCreateView.as_view(),name='create-vehicle'),
   path('',views.VehicleListView.as_view(),name='all-vehicles'),
   path('vehicle/<int:pk>/',views.VehicleDetailView.as_view(),name='vehicle-detail'),
   path('vehicle/<int:pk>/update/',views.VehicleUpdateView.as_view(),name='update-vehicle'),
   path('vehicle/<int:pk>/delete/',views.VehicleDeleteView.as_view(),name='veh-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
