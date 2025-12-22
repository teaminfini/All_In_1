import json
import urllib.parse
import random
from datetime import datetime

# اطلاعات اختصاصی تو
BASE_URL = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"

def main():
    # لیست ترندهای داغ علی‌اکسپرس در دسته‌بندی‌های مختلف
    hot_trends = [
        # Electronics
        {"category": "Electronics", "name": "Zeblaze Stratos 3 Pro GPS", "url": "https://www.aliexpress.com/item/1005006016738012.html", "price": "$64.50", "img": "ae04.alicdn.com/kf/S89476906564344798e12f8a4495964955b9e592474f3j.jpg"},
        {"category": "Electronics", "name": "Baseus GaN5 Pro 65W Charger", "url": "https://www.aliexpress.com/item/1005005578432101.html", "price": "$28.90", "img": "ae04.alicdn.com/kf/Sf5e12f8a4495964955b9e592474f3j.jpg"},
        
        # Home
        {"category": "Home", "name": "Portable Turbo Jet Fan 110k RPM", "url": "https://www.aliexpress.com/item/1005006135334751.html", "price": "$31.00", "img": "ae04.alicdn.com/kf/S7b973522f08547378c2e7a1773G.jpg"},
        {"category": "Home", "name": "Smart LED RGB Light Bar", "url": "https://www.aliexpress.com/item/1005005578432101.html", "price": "$12.50", "img": "ae04.alicdn.com/kf/S064560751f9a460497554c2e7a1773G.jpg"},
        
        # Fashion / Accessories
        {"category": "Fashion", "name": "Luxury Skeleton Automatic Watch", "url": "https://www.aliexpress.com/item/1005006001234567.html", "price": "$45.00", "img": "ae04.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg"},
        {"category": "Fashion", "name": "Bluetooth Sleep Headphones Mask", "url": "https://www.aliexpress.com/item/1005005814522301.html", "price": "$15.90", "img": "ae04.alicdn.com/kf/Sf5e12f8a4495964955b9e592474f3j.jpg"}
    ]

    final_db = []
    for item in hot_trends:
        # انکود کردن آدرس برای جلوگیری از 404
        safe_url = urllib.parse.quote(item['url'], safe='')
        
        final_db.append({
            "name": item['name'],
            "category": item['category'],
            "price": item['price'],
            "image": f"https://images.weserv.nl/?url={item['img']}&w=500&fit=contain&bg=white",
            "affiliate_link": f"{BASE_URL}?ulp={safe_url}"
        })

    # ذخیره در فایل
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(final_db, f, indent=4)
    
    print(f"SUCCESS: AI Engine deployed {len(final_db)} products across categories.")

if __name__ == "__main__":
    main()
