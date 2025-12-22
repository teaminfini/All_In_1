import requests
import json
import os
import xml.etree.ElementTree as ET

DB_FILE = 'products.json'

def get_trending_from_feed():
    print("Fetching real trends...")
    # استفاده از فید محصولات جدید و پرطرفدار (به عنوان نمونه)
    feeds = [
        "https://www.gadgetreview.com/feed",
        "https://www.techradar.com/rss"
    ]
    
    new_items = []
    for url in feeds:
        try:
            response = requests.get(url, timeout=10)
            root = ET.fromstring(response.content)
            for item in root.findall('./channel/item')[:3]: # ۳ تای اول هر فید
                title = item.find('title').text
                link = item.find('link').text
                new_items.append({
                    "id": hash(title),
                    "name": title,
                    "category": "Trending",
                    "description": "Hot product recently searched and discussed.",
                    "price": "Check Site",
                    "affiliate_link": link, # در مرحله بعد این را به لینک خودت تبدیل می‌کنیم
                    "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
                    "status": "active"
                })
        except Exception as e:
            print(f"Error fetching feed: {e}")
    return new_items

def update_system():
    # ۱. بارگذاری دیتابیس فعلی
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            try:
                products = json.load(f)
            except: products = []
    else:
        products = []

    # ۲. چک کردن زنده بودن لینک‌ها (همان چیزی که خواسته بودی)
    for p in products:
        try:
            res = requests.head(p['affiliate_link'], timeout=5, allow_redirects=True)
            p['status'] = 'active' if res.status_code < 400 else 'broken'
        except:
            p['status'] = 'broken'

    # ۳. اضافه کردن محصولات پرسرچ جدید
    trending_products = get_trending_from_feed()
    existing_names = [p['name'] for p in products]

    for tp in trending_products:
        if tp['name'] not in existing_names:
            products.append(tp)
            print(f"New trend added: {tp['name']}")

    # ۴. ذخیره نهایی
    with open(DB_FILE, 'w') as f:
        json.dump(products, f, indent=4)
    print("All done!")

if __name__ == "__main__":
    update_system()
