from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .crawler import crawl_ptt_food
def index(request):
    return render(request,'index.html')
def crawler(request):
    return render(request,'crawler.html')
def crawl_ptt_food_view(request):
    try:
        crawl_ptt_food()
        return render(request, 'crawl_success.html', {'message':'爬蟲執行完成,資料已儲存'})
    except Exception as e:
        return render(request, 'crawl_error.html',{'message': f'爬蟲執行失敗:{str(e)}'})
def crawler_view(request):
    return render(request, 'crawler.html', {
        'passenger_range': range(1, 11)
    })

