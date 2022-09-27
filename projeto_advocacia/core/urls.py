from django.urls import path

from projeto_advocacia.core.views import CustomLoginView, DiarioOficialView

urlpatterns = [
    path('', CustomLoginView.as_view()),
    path('diario-oficial/', DiarioOficialView.as_view()),
]
