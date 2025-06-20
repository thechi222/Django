from django.contrib import admin
from django.urls import path
from chi_01.views import index, crawler_form, run_crawler  # ✅ 你定義的 views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('crawler/', crawler_form, name='crawler'),  # 對應 crawler.html 表單
    path('run_crawler/', run_crawler, name='crawl_ptt_food'),  # 對應提交表單後處理邏輯
]
