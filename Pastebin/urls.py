from django.urls import path
from . import views

urlpatterns = [
    path('homePage/', views.home_page ,name="homePage"),
    path('history/',views.history, name="history"),
    path('addText/', views.add_text, name="addText"),
    path('show_text/<text_id>', views.show_text, name='show-text'),
]
