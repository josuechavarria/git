from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from evaluaciones.models import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [
    url(r'^$', permission_required('evaluaciones.evaluaciones_enterprise')(views.principal), name='principal'),
    #url(r'^accounts/login/$', views.LoginView.as_view(), name='login'), 
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),    
    url(r'^empresas/(?P<pk>\d+)/$', login_required(views.IndexEmpresaView.as_view()), name='principal_empresa'),
    url(r'^empresas/crear/$', permission_required('evaluaciones.evaluaciones_enterprise')(views.CrearEmpresa.as_view(model= empresas)), name='crear_empresa'),
    url(r'^empresas/actualizar/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_enterprise')(views.ActualizarEmpresa.as_view(model= empresas)), name='actualiza_empresa'),
    url(r'^empresas/listar', permission_required('evaluaciones.evaluaciones_enterprise')(views.ListarEmpresas.as_view(model= empresas)), name='listar_empresa'),
    url(r'^puesto/crear/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.CrearPuesto.as_view(model=puestos)), name='crear_puesto'),
    url(r'^puesto/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.ActualizarPuesto.as_view(model= puestos)), name='actualiza_puesto'),
    url(r'^puesto/listar/(?P<pk>\d+)/$',permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.ListarPuestos.as_view(model=puestos)), name='listar_puesto'),
    url(r'^puesto/borrar/(?P<pk>\d+)/(?P<id>\d+)/$',permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.BorrarPuesto.as_view(model=puestos)), name='borrar_puesto'),
    url(r'^puesto/activo/', views.activar_puesto.as_view(),
        name='activar_puesto'),
    url(r'^departamento/crear/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.CrearDepartamento.as_view(model=departamentos)), name='crear_departamento'),
    url(r'^departamento/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.ActualizarDepartamento.as_view(model= departamentos)), name='actualiza_departamento'),
    url(r'^departamento/listar/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.ListarDepartamentos.as_view(model= departamentos)), name='listar_departamento'),
    url(r'^departamento/borrar/(?P<pk>\d+)/(?P<id>\d+)/$',views.BorrarDepartamento.as_view(model=departamentos), name='borrar_departamento'),
    url(r'^sucursal/crear/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.CrearSucursal.as_view(model=sucursales)), name='crear_sucursal'),
    url(r'^sucursal/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.ActualizarSucursal.as_view(model= sucursales)), name='actualiza_sucursal'),
    url(r'^sucursal/listar/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_listasdesplegables')(views.ListarSucursales.as_view(model= sucursales)), name='listar_sucursal'),
    url(r'^sucursal/borrar/(?P<pk>\d+)/(?P<id>\d+)/$',views.BorrarSucursal.as_view(model=sucursales), name='borrar_sucursal'),    
    url(r'^sucursal/activo/', views.activar_sucursal.as_view(),
        name='activar_sucursal'),
    url(r'^roles/listar/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_roles')(views.RolesView.as_view()), name='listar_roles'),
    url(r'^roles/crear/(?P<pk>\d+)/$', permission_required('evaluaciones.evaluaciones_roles')(views.RolesNuevoView.as_view()), name='crear_roles'),
    url(r'^criterio/crear/(?P<pk>\d+)/$', views.CrearCriterio.as_view(model=criterios), name='crear_criterio'),
    url(r'^criterios/listar/(?P<pk>\d+)/$',
        views.ListarCriterios.as_view(), name='listar_criterios'),
    url(r'^criterios/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$',
        views.ActualizarCriterios.as_view(model=criterios), name='actualizar_criterio'),
    url(r'^criterios/borrar/(?P<pk>\d+)/(?P<id>\d+)/$',views.BorrarCriterios.as_view(model=criterios), name='borrar_criterios'),
    url(r'^criterio/activo/', views.activar_criterio.as_view(),
        name='activar_criterio'),
    url(r'^periodo/crear/(?P<pk>\d+)/$', views.CrearPeriodos.as_view(model=periodos), name='crear_periodo'),
    url(r'^periodo/listar/(?P<pk>\d+)/$', views.ListarPeriodos.as_view(model=periodos), name='listar_periodos'),
    url(r'^periodo/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$',
        views.ActualizarPeriodos.as_view(model=periodos), name='actualizar_periodos'),
    url(r'^periodo/borrar/(?P<pk>\d+)/(?P<id>\d+)/$',
        views.BorrarPeriodo.as_view(model=periodos), name='borrar_periodo'),
    url(r'^periodo/activo/', views.activar_periodo.as_view(),
        name='activar_periodo'),
    url(r'^objetivo/crear/(?P<pk>\d+)/$', views.CrearObjetivos.as_view(model=objetivos), name='crear_objetivos'),
    url(r'^objetivos/listar/(?P<pk>\d+)/$', views.ListarObjetivos.as_view(), name='listar_objetivos'),
    url(r'^objetivos/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$',
        views.ActualizarObjetivos.as_view(model=objetivos), name='actualizar_objetivos'),
    url(r'^objetivo/activo/', views.activar_objetivo.as_view(),
        name='activar_objetivo'),
    url(r'^empresa/activo/', views.activar_empresa.as_view(),
        name='activar_empresa'),
    url(r'^objetivos/borrar/(?P<pk>\d+)/(?P<id>\d+)/$',views.BorrarObjetivos.as_view(model=objetivos), name='borrar_objetivos'),
    url(r'^departamentos/importar/',views.simple_upload, name='borrar_objetivos'),
    url(r'^departamentos/activo/', views.activar_departamento.as_view(),
        name='activar_departamento'),
    url(r'^objetivo/activo/', views.activar_objetivo.as_view(),
        name='activar_objetivo'),
    url(r'^empresa/activo/', views.activar_empresa.as_view(),
        name='activar_empresa'),
    url(r'^objetivos/borrar/(?P<pk>\d+)/(?P<id>\d+)/$',views.BorrarObjetivos.as_view(model=objetivos), name='borrar_objetivos'),
    url(r'^departamentos/importar/',views.simple_upload, name='borrar_objetivos'),
    url(r'^departamentos/activo/', views.activar_departamento.as_view(),
        name='activar_departamento'),
    url(r'^usuario/crear/(?P<pk>\d+)/$', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    url(r'^usuario/perfil/(?P<pk>\d+)/(?P<id>\d+)/$', views.Perfil_.as_view(), name='perfil_'),
    url(r'^usuario/listar/(?P<pk>\d+)/$', views.ListarUsuarioView.as_view(), name='listar_usuario'),
    url(r'^usuario/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$', views.ActualizarUsuarioView.as_view(), name='actualiza_usuario'),
    url(r'^usuario/eliminar/(?P<pk>\d+)/(?P<id>\d+)/$', views.EstadoUsuarioView.as_view(), name='estado_usuario'),
    url(r'^usuario/actualizar/pass/(?P<pk>\d+)/(?P<id>\d+)/(?P<oldpass>\w+)/$', views.ResetPasswordView.as_view(), name='actualiza_password'),
    url(r'^usuario/actualizar/pass/notificacion/(?P<pk>\d+)/(?P<id>\d+)/$', views.ResetPasswordNotificacionView.as_view(), name='notificacion_password'),
    url(r'^usuario/actualizar/pass/(?P<pk>\d+)/(?P<id>\d+)/$', views.ExpiredPasswordView.as_view(), name='expired_password'),
    url(r'^roles/actualizar/(?P<pk>\d+)/(?P<id>\d+)/$', views.RolesActualizarView.as_view(), name='actualiza_rol'),
    url(r'^roles/eliminar/(?P<pk>\d+)/(?P<id>\d+)/$', views.RolesEliminarView.as_view(), name='estado_rol'),
    url(r'^misevaluaciones/ver/(?P<pk>\d+)/$', views.ColaboradorMisEvaluaciones.as_view(), name='misevaluaciones'),
    url(r'^evaluaciones/listar/(?P<pk>\d+)/$', views.SupervisorEvaluacionesList.as_view(), name='evaluacioneslist'),
    url(r'^evaluaciones/crear/(?P<pk>\d+)/$', views.CrearEvaluacion.as_view(model=evaluaciones), name='crear_evaluacion'),
    url(r'^evaluaciones/guardar/', views.guardar_evaluacion.as_view(),
        name='guardar_evaluacion'),
    url(r'^evaluaciones/listar/(?P<pk>\d+)/$',
        views.ListarEvaluaciones.as_view(), name='listar_evaluaciones'),
    
    url(r'^evaluaciones/borrar/', views.borrar_evaluaciones.as_view(), name='borrar_evaluaciones'),
    url(r'^evaluaciones/actualiza_tabla/', views.actualizar_tabla,
        name='actualizar_tabla'),
    
    url(r'^evaluaciones/actualiza_tablacriterios/', views.actualizar_tablacriterios,
        name='actualizar_tablacriterios'),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

