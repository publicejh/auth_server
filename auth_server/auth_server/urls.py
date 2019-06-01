from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-management/doc/', get_swagger_view(title='Rest API Document')),
    path('user-management/v1/', include('accounts.api.urls')),
]
