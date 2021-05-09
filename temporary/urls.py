"""temporary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.core.mail import EmailMessage



from home.views import register, login, contac, home_client, home, home_instructor, home_graduated, home_client_students, home_instructor_students, mensaje #<-agregado

handler404 = 'home.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', register),
    path('login/', login),
    path('contac/<int:id>/<int:sid>/', contac),#"nueva"
    path('mensaje/<int:id>/<int:sid>/', mensaje),#nueva
    path('client-home/<int:id>', home_client),
    path('client-home-students/<int:id>', home_client_students),
    path('instructor-home/<int:id>', home_instructor),
    path('instructor-home-students/<int:id>', home_instructor_students),
    path('graduated-home/<int:id>', home_graduated),
 

    

]

