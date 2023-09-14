from django.urls import path
from . import views

app_name = 'greenEnergy'

# Map Route with Views
urlpatterns = [
    # Landing Route & View
    path('', views.store, name='online-store'),
    path('kits', views.kits, name='solar-kits'),
    path('about', views.about, name='about-green-energy'),
]