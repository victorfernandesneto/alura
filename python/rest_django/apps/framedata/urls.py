from django.urls import path, include
from apps.framedata.views import CharacterViewSet, MoveViewSet, ListCharacterMove
from rest_framework import routers

router = routers.DefaultRouter()
router.register('characters', CharacterViewSet, basename='characters')
router.register('moves', MoveViewSet, basename='moves')

urlpatterns = [
    path('', include(router.urls)),
    path('characters/<int:pk>/moves/', ListCharacterMove.as_view())
]