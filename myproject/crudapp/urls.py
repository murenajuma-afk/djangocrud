from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='index'),
    path('products/', views.admin, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete/<int:id>/', views.delete_product, name='delete'),
    path('update/<int:id>/', views.update_product, name='update'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('user_dashboard', views.user_dashboard, name='user'),
    path('logout/', views.logout_user, name='logout')
  

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)