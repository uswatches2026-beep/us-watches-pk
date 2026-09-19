from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('watch/<int:watch_id>/', views.watch_detail, name='watch_detail'),

    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:watch_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:watch_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:watch_id>/', views.remove_from_cart, name='remove_from_cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)