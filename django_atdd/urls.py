from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from store.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view()),
]
