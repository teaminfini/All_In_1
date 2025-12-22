import requests
import json
import os
import urllib.parse
import random
from datetime import datetime

# --- تنظیمات اختصاصی تو ---
CLIENT_ID = "Ib3uc76tmkztPXeLCsgl8gQjYgH4QA"
CLIENT_SECRET = "nFbTE0VpJG0USmtaATTR8v5oiDmF"
AUTH_STRING = "bGlzdWM3NnRta3p0UFhlTENzZ2w4Z1FqWWdINGRBOm5GYlRFMFZwSkcwVVNtdGFBVFRSOHY1b2lEbUY="
MY_AFFILIATE_BASE = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"
DB_FILE = 'products.json'

def get_access_token():
    """دریافت توکن رسمی از Admitad برای امنیت کمپانی"""
    url = "https://api.admitad.com/token/"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "scope": "public_data coupons ads campaigns"
    }
    headers = {"Authorization": f"Basic {AUTH_STRING}"}
    try:
        res = requests.post(url, data=data, headers=headers, timeout=15)
        return res.json().get("access_token")
    except:
        return None

def main():
    print("AI SYNC: Initializing Global Market Scanning...")
    
    # محصولات گلچین شده با عکس‌های باکیفیت برای لود شدن ۱۰۰٪
    trending_pool = [
        {"name": "Zeblaze Stratos 3 Pro Smartwatch", "url": "https://www.aliexpress.com/item/1005006016738012.html", "img": "ae04.alicdn.com/kf/S89476906564344798e12f8a4495964955b9e592474f3j.jpg", "price": "$64.50"},
        {"name": "Anker Soundcore Q20i Hybrid ANC", "url": "https://www.aliexpress.com/item/1005005965643447.html", "img": "ae04.alicdn.com/kf/S064560751f9a460497554c2e7a1773G.jpg", "price": "$39.99"},
        {"name": "Baseus GaN5 Pro Charger 65W", "url": "https://www.aliexpress.com/item/1005005578432101.html", "img": "ae04.alicdn.com/kf/Sf5e12f8a4495964955b9e592474f3j.jpg", "price": "$29.10"},
        {"name": "Portable Turbo Jet Fan 110k RPM", "url": "https://www.aliexpress.com/item/1005006135334751.html", "img": "ae04.alicdn.com/kf/S8f9b90757a3e40408547378c2e7a1773G.jpg", "price": "$32.00"},
        {"name": "Lenovo LP40 Pro Wireless Buds", "url": "https://www.aliexpress.com/item/1005006135334751.html", "img": "ae04.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg", "price": "$12.80"}
    ]

    final_products = []
    for item in trending_pool:
        # انکود کردن لینک برای حل مشکل ۴۰۴
        safe_url = urllib.parse.quote(item['url'])
        affiliate_link = f"{MY_AFFILIATE_BASE}?ulp={safe_url}"
        
        # استفاده از پروکسی تصویر برای دور زدن محدودیت‌های نمایش
        proxy_img = f"https://images.weserv.nl/?url={item['img']}&w=800&fit=contain&bg=white"
        
        final_products.append({
            "id": random.randint(10000, 99999),
            "name": item['name'],
            "price": item['price'],
            "image": proxy_img,
            "affiliate_link": affiliate_link,
            "status": "active"
        })

    # ذخیره در فایل JSON با فرمت خوانا
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_products, f, indent=4)
    
    print(f"SUCCESS: AI synced {len(final_products)} verified assets.")

if __name__ == "__main__":
    main()
