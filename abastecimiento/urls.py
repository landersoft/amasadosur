from abastecimiento import views

from django.urls import path, include

app_name = 'abastecimiento'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'productos/', views.ProductoList.as_view(), name='productos'),
    path(r'test/', views.test, name='test'),


    # path(r'reporte/boletas/detalle/<int:id>', views.detalle_boleta, name='detalle_boleta'),
    ]