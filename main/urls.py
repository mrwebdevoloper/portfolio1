from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('portdetail/<int:pk>/', PortfolioDetail.as_view()),
    path('blogdetail/<int:pk>/', BlogDetail.as_view()),
    path('send-msg/', SendMsg),
    path('page404/', Page404)


]