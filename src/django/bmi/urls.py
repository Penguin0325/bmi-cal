from django.urls import path
from .views import bmiIndexView, bmiCreateView, bmiHomeView

urlpatterns = [
    path("", bmiIndexView),
    path("create/", bmiCreateView, name="bmi-create"),
    path("home/", bmiHomeView, name="bmi-home")
]