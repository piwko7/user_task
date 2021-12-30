from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import UsersViewSet, TodosViewSet, get_data, send_data

router = SimpleRouter()

router.register('get_users', UsersViewSet, basename='get_users')
router.register('get_tasks', TodosViewSet, basename='get_tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('get_data', get_data, name='get_data'),
    path('send_data', send_data, name='send_data'),
]


