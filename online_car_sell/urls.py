from django.urls import path
from online_car_sell import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.user_register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('modal-data/', views.modal_data, name='modal_data'),
    path('car-register/', views.car_register, name='car_register'),
    # path('thankyou/', views.thank_you_car_register, name='thankyou-car-register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
