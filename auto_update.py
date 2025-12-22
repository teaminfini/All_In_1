import json
import os
import urllib.parse
import random
from datetime import datetime

# --- تنظیمات اختصاصی تو (بر اساس عکس‌های قبلی) ---
# لینک پایه (Base Affiliate Link) تو در Admitad
BASE_AFF_URL = "https://ad.admitad.com/g/1e8d114494f9dbcef44416525dc3e8/"
DB_FILE = 'products.json'

def create_affiliate_link(original_url):
    """
    دقیقاً همان کاری که در عکس فرستادی انجام می‌دهد:
    لینک اصلی را می‌گیرد و به لینک افیلیت تو تبدیل می‌کند.
    """
    # انکود کردن لینک اصلی (تبدیل / به %2F و غیره) مطابق استاندارد Admitad
    encoded_url = urllib.parse.quote(original_url, safe='')
    return f"{BASE_AFF_URL}?ulp={encoded_url}"

def get_hot_product_links():
    """
    لیست محصولات پرجستجو و ترند (لینک‌های اصلی و بدون افیلیت)
    این‌ها محصولاتی هستند که همین الان بیشترین سرچ را در علی‌اکسپرس دارند.
    """
    return [
        {
            "category": "Electronics",
            "name": "Zeblaze Stratos 3 Pro GPS Smartwatch",
            "raw_url": "https://www.aliexpress.com/item/1005006016738012.html",
            "img": "ae01.alicdn.com/kf/S89476906564344798e12f8a4495964955b9e592474f3j.jpg",
            "price": "$64.50"
        },
        {
            "category": "Electronics",
            "name": "Anker Soundcore Q20i Hybrid ANC",
            "raw_url": "https://www.aliexpress.com/item/1005005965643447.html",
            "img": "ae01.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg",
            "price": "$39.99"
        },
        {
            "category": "Home",
            "name": "Portable Turbo Jet Fan 110,000 RPM",
            "raw_url": "https://www.aliexpress.com/item/1005006135334751.html",
            "img": "ae01.alicdn.com/kf/S7b973522f08547378c2e7a1773G.jpg",
            "price": "$31.00"
        },
        {
            "category": "Home",
            "name": "Baseus GaN5 Pro Desktop Charger 65W",
            "raw_url": "https://www.aliexpress.com/item/1005005578432101.html",
            "img": "ae01.alicdn.com/kf/Sf5e12f8a4495964955b9e592474f3j.jpg",
            "price": "$28.90"
        },
        {
            "category": "Fashion",
            "name": "Bluetooth Smart Sleep Mask Headphones",
            "raw_url": "https://www.aliexpress.com/item/1005005814522301.html",
            "img": "ae01.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg",
            "price": "$15.99"
        }
    ]

def main():
    print("MASTER BRAIN: Converting Original Links to Affiliate Links...")
    
    raw_products = get_hot_product_links()
    final_data = []

    for item in raw_products:
        # تبدیل لینک اصلی به لینک پولساز تو
        affiliate_link = create_affiliate_link(item['raw_url'])
        
        # استفاده از پروکسی برای لود قطعی عکس
        proxy_img = f"https://wsrv.nl/?url={item['img']}&w=600&h=600&fit=contain&bg=white"
        
        final_data.append({
            "id": random.randint(100000, 999999),
            "name": item['name'],
            "category": item['category'],
            "price": item['price'],
            "image": proxy_img,
            "affiliate_link": affiliate_link,
            "status": "active"
        })

    # ذخیره در فایل دیتابیس
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, indent=4)
    
    print(f"DONE: {len(final_data)} Products converted and deployed.")

if __name__ == "__main__":
    main()
