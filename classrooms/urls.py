
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from API.views import (
RegisterAPIView,
ClassroomList,
ClassroomDetails,
ClassroomCreate,
UpdateClassroom,
DeleteClassroom
)
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

     path('api/login/', TokenObtainPairView.as_view(), name='api-login'),
     path('api/register/', RegisterAPIView.as_view(), name='api-register'),
     path('api/list/', ClassroomList.as_view(), name='api-classroom-list'),
     path('api/<int:classroom_id>/',ClassroomDetails.as_view(), name='api-classroom-detail'),
     path('api/classroom/create',ClassroomCreate.as_view(), name='api-classroom-create'),
     path('api/<int:classroom_id>/update',UpdateClassroom.as_view(), name='api-classroom-update'),
     path('api/<int:classroom_id>/delete',DeleteClassroom.as_view(), name='api-classroom-delete'),
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
