from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def create_driver():
    options = Options()
    options.add_argument('--headless')  # 無畫面模式
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver

def crawl_starlux(origin, destination, depart_date, return_date=None, passengers=1):
    print("🛫 開始爬取星宇航空...")
    driver = create_driver()
    try:
        driver.get('https://www.starlux-airlines.com/zh-tw')
        time.sleep(3)

        from_input = driver.find_element(By.ID, 'departure-station')
        from_input.click()
        from_input.send_keys(origin)
        time.sleep(1)

        to_input = driver.find_element(By.ID, 'arrival-station')
        to_input.click()
        to_input.send_keys(destination)
        time.sleep(1)

        driver.execute_script(f"document.querySelector('#departure-date').value = '{depart_date}'")

        search_btn = driver.find_element(By.CSS_SELECTOR, '.btn-search')
        search_btn.click()

        time.sleep(5)

        price_element = driver.find_element(By.CSS_SELECTOR, '.fare-amount')
        price_text = price_element.text

        return {
            'airline': '星宇航空',
            'price': price_text,
            'url': driver.current_url
        }

    except Exception as e:
        print("星宇航空爬取失敗:", e)
        return {
            'airline': '星宇航空',
            'error': str(e)
        }
    finally:
        driver.quit()

def crawl_china_air(origin, destination, depart_date, return_date=None, passengers=1):
    print("🛫 正在爬取中華航空...")
    driver = create_driver()
    try:
        driver.get('https://www.china-airlines.com/tw/zh')
        time.sleep(3)
        return {
            'airline': '中華航空',
            'price': '尚未實作',
            'url': driver.current_url
        }
    except Exception as e:
        print("❌ 華航爬取失敗:", e)
        return {'airline': '中華航空', 'error': str(e)}
    finally:
        driver.quit()

def crawl_eva_air(origin, destination, depart_date, return_date=None, passengers=1):
    print("🛫 正在爬取長榮航空...")
    driver = create_driver()
    try:
        driver.get('https://www.evaair.com/zh-tw/')
        time.sleep(3)
        return {
            'airline': '長榮航空',
            'price': '尚未實作',
            'url': driver.current_url
        }
    except Exception as e:
        print("❌ 長榮爬取失敗:", e)
        return {'airline': '長榮航空', 'error': str(e)}
    finally:
        driver.quit()

def crawl_japan_airlines(origin, destination, depart_date, return_date=None, passengers=1):
    print("🛫 正在爬取日本航空...")
    driver = create_driver()
    try:
        driver.get('https://www.jal.co.jp/twl/zh/')
        time.sleep(3)
        return {
            'airline': '日本航空',
            'price': '尚未實作',
            'url': driver.current_url
        }
    except Exception as e:
        print("❌ 日本航空爬取失敗:", e)
        return {'airline': '日本航空', 'error': str(e)}
    finally:
        driver.quit()

def crawl_all_airlines(origin, destination, depart_date, return_date=None, passengers=1):
    results = []
    results.append(crawl_starlux(origin, destination, depart_date, return_date, passengers))
    results.append(crawl_china_air(origin, destination, depart_date, return_date, passengers))
    results.append(crawl_eva_air(origin, destination, depart_date, return_date, passengers))
    results.append(crawl_japan_airlines(origin, destination, depart_date, return_date, passengers))
    return results
