from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from projeto_advocacia.processo.apis.viewsets import LeiAPI, AplicacaoPenalAPI

schema_view = get_schema_view(
   openapi.Info(
      title="Projeto Advocacia",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ismaelbenjamim15@hotmail.com"),
      license=openapi.License(name="CC BY-NC-ND"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register("legislacao", LeiAPI)

APIs = [
    path("legislacao/servico", AplicacaoPenalAPI.as_view())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(APIs)),
    path('', include('projeto_advocacia.core.urls')),
    path('dashboard/', include('projeto_advocacia.dashboard.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
