from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import EstudanteViewSet, DisciplinaViewSet

router = routers.DefaultRouter()
router.register('Estudantes', EstudanteViewSet, basename = 'Estudantes')
router.register('Disciplinas', DisciplinaViewSet, basename = 'Disciplinas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
