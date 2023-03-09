from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # Path to access django admin
    path('admin/', admin.site.urls),
    # Path to render homePage
    path('', views.home, name='home'),
    # Path to render opportunitiesPage
    path('opportunities', views.opportunities, name='opportunities')
]
