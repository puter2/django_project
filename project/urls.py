"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, re_path
from school.views import test_view, home, add_room, edit_room, delete_room, add_res

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',test_view),
    path('', home),
    path('add_room/', add_room),
    path('edit/<int:id>', edit_room),
    path('delete/<int:id>', delete_room),
    path('add_reservation/<int:id>', add_res)
]
