from django.contrib import admin
from django.urls import path, include
from geral.views import Index

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
	path('', Index.as_view(), name='index'),
]