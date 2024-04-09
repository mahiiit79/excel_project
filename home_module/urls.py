from . import views
from django.urls import path

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home_page'),
    path('exel/',views.export_excel,name='export_excel'),
]