"""smartclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from assessment.serializers import QuizViewSet
from department.serializers import DepartmentViewSet
from account.serializers import StudentProfileViewSet, InstructorProfileViewSet
from account.views import ProfileCreateAPIView

router = routers.DefaultRouter()
router.register(r'quizes', QuizViewSet)
router.register(r'student-profiles', StudentProfileViewSet)
router.register(r'instructor-profiles', InstructorProfileViewSet)
router.register(r'quizes', QuizViewSet)
router.register(r'departments', DepartmentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/sign-up/', ProfileCreateAPIView.as_view(), name='sign-up'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)