from django.contrib import admin
from django.urls import path

from tours.views import main_view, departure_view, tour_view, custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('departure/<str:departure>/', departure_view),
    path('tour/<int:id>/', tour_view),
]


handler404 = custom_handler404
handler500 = custom_handler500
