from . import views
from django.urls import path


urlpatterns = [
    path("clients/", views.RenderClient.as_view(), name="RenderClient"),
    path("clients/<int:pk>", views.RenderClientDetail.as_view(), name="RenderClientDetail"),
]
