from django.urls import re_path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    re_path(r'^user_auth/$',views.UserAuthView.as_view(),name='UserAuthView'),
    re_path(r'^roles/$',views.RoleView.as_view(),name='RoleView'),
    re_path(r'^drf_roles/$',views.RoleDRFView.as_view(),name='RoleDRFView'),
    re_path(r'^drf_users/$',views.UserDRFView.as_view(),name='UserDRFView'),
    re_path(r'^easter_egg_anjelicasilva/$',views.EasterEggView.as_view(),name='EasterEggView'),
]