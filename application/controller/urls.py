from django.urls import path
from . import views

urlpatterns = [
    path("detect/", views.startFlowAnalysis),
    path("tcp/override/", views.insertTcpOverridingModule),
    path("ttl/override/", views.applyTtlMaximization),
    path("delay/override/", views.insertDelyaQueue),
]
