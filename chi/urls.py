from django.contrib import admin
from django.urls import path
from chi_01.views import index, crawler_form, run_crawler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('crawler/', crawler_form, name='crawler'),
    path('run_crawler/', run_crawler, name='run_crawler'),
]
