from django.shortcuts import render
from .crawler import crawl_all_airlines
import traceback  # ✅ 加入錯誤印出工具

def index(request):
    return render(request, 'index.html', {
        'passenger_range': range(1, 11)
    })

def crawler_form(request):
    return render(request, 'crawler.html', {
        'passenger_range': range(1, 11)
    })

def run_crawler(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        depart_date = request.POST.get('depart_date')
        return_date = request.POST.get('return_date') or None
        passengers = request.POST.get('passengers') or 1

        print(f"📝 使用者輸入：{origin=} {destination=} {depart_date=} {return_date=} {passengers=}")

        try:
            results = crawl_all_airlines(
                origin=origin,
                destination=destination,
                depart_date=depart_date,
                return_date=return_date,
                passengers=int(passengers)
            )

            return render(request, 'crawl_success.html', {
                'message': '✅ 所有航空資料已成功抓取！',
                'results': results
            })

        except Exception as e:
            print("❌ 爬蟲失敗 traceback：")
            traceback.print_exc()
            return render(request, 'crawl_error.html', {
                'message': f'❌ 抓取失敗：{str(e)}'
            })

    else:
        return render(request, 'crawler.html', {
            'passenger_range': range(1, 11)
        })
