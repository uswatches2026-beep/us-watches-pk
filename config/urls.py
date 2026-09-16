from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('watch/<int:watch_id>/', views.watch_detail, name='watch_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)