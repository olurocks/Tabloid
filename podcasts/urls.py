from django.urls import path
from .views import HomePageView, VanguardView

urlpatterns = [
    path("nairaland",HomePageView.as_view(), name = "homepage"),
    path("vanguard",VanguardView.as_view(), name = "vanguard" )
]