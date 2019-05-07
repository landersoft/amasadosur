from . import views
from ventas import views
from django.urls import path, include

app_name='ventas'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'nueva/', views.nueva, name='nueva'),
    path(r'nueva/boleta/', views.boleta, name='boleta'),
    path(r'nueva/add', views.detalleadd, name='add'),
    #path(r'nueva/factura/', views.factura, name='factura'),
    #path(r'nueva/factura/add', views.detalleadd, name='add'),
    path(r'nueva/lista/',views.VentaList.as_view()),
    path(r'nueva/lista/pagar', views.pagar, name='pagar'),
    path(r'nueva/lista/formapago', views.formapago, name='formapago'),
    path(r'nueva/lista/documento', views.tipodocumento, name='tipodocumento'),
    path(r'nueva/lista/verifica', views.verifica, name='verifica'),
    path(r'nueva/lista/registrocliente', views.registracliente, name='registracliente'),
    path(r'estadisticas/', views.estadisticas, name='estadisticas'),
    path(r'reporte/boletas/', views.vista_boleta, name='vista_boleta'),
    path(r'reporte/boletas/detalle/<int:id>', views.detalle_boleta, name='detalle_boleta'),
    path(r'reporte/boletas/lista', views.detalle_boleta, name='detalle_boleta'),


]
