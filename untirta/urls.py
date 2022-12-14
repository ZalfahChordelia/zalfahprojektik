"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from feb.views import prodi
from fh.views import prodi1
from fisip.views import prodi2
from fk.views import prodi3
from fkip.views import prodi4
from faperta.views import prodi5, tambah_dosen, tambah_mahasiswa, tambah_staf
from ft.views import prodi6
from pascasarjana.views import prodi7
from profil.views import profil0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feb/', prodi),
    path('fh/', prodi1),
    path('fisip', prodi2),
    path('fk', prodi3),
    path('fkip', prodi4),
    path('faperta', prodi5),
    path('ft', prodi6),
    path('pascasarjana', prodi7),
    path('profil', profil0),
    path('tambah-dosen/', tambah_dosen),
    path('tambah-mahasiswa/', tambah_mahasiswa),
    path('tambah-staf/', tambah_staf),
]
