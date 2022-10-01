from django.urls import path

from projeto_advocacia.core.views import CustomLoginView, DiarioOficialView, CustomLogoutView, RegisterView, \
    NotPermissionView, NotExistsView, LadingPageView

urlpatterns = [
    path('', LadingPageView.as_view(), name='lading-page'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('diario-oficial/', DiarioOficialView.as_view(), name='diario-oficial'),
    path("error/403/", NotPermissionView.as_view(), name='403'),
    path("error/404/", NotExistsView.as_view(), name='404'),
]
