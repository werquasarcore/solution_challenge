from django.urls import path, include
from api.views import home, frontend_css, frontend_js

urlpatterns = [
    path("", home),
    path("style.css", frontend_css),
    path("script.js", frontend_js),
    path("api/", include("api.urls")),
]