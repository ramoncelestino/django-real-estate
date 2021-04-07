"""imobiliaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.conf import settings
from imoveis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('imoveis/create', views.create_imovel, name="create_imovel"),
    path('search_imoveis/', views.search_imoveis, name="search-imoveis"),
    path('imoveis/<str:pk>', views.view_imovel, name="view_imovel"),
    path('apresentacao', views.view_apresentacao, name="apresentacao"),
    path('imoveis/', views.ImovelListView.as_view(), name="imoveis"),
    path('delete_imovel/<int:pk>', views.delete_imovel, name="delete_imovel"),
    path('update_imovel/<int:pk>', views.delete_imovel, name="update_imovel"),
    path('login/', views.login, name="login")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


