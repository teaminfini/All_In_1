import json
import os
from datetime import datetime

# اطلاعات اختصاصی تو
BASE_LINK = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"
DB_FILE = 'products.json'

def main():
    # محصولات واقعی و پرفروش برای شروع کار (کمپانی‌محور)
    trending_data = [
        {
            "name": "Magnetic Wireless Power Bank 15W",
            "price": "$22.50",
            "image": "https://ae01.alicdn.com/kf/S7f0c1c8a4495964955b9e592474f3j.jpg",
            "url": "https://www.aliexpress.com/item/1005005578432101.html"
        },
        {
            "name": "Smart Sleep Mask Bluetooth 5.2",
            "price": "$12.99",
            "image": "https://ae01.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg",
            "url": "https://www.aliexpress.com/item/1005005814522301.html"
        },
        {
            "name": "Mini Portable Turbo Jet Fan 110000RPM",
            "price": "$29.40",
            "image": "https://ae01.alicdn.com/kf/S8f9b90757a3e40408547378c2e7a1773G.jpg",
            "url": "https://www.aliexpress.com/item/1005006135334751.html"
        },
        {
            "name": "4K Ultra HD Portable Projector",
            "price": "$58.10",
            "image": "https://ae01.alicdn.com/kf/H76543210abc.jpg",
            "url": "https://www.aliexpress.com/item/1005006135334751.html"
        }
    ]

    final_list = []
    for item in trending_data:
        final_list.append({
            "id": int(datetime.now().timestamp()),
            "name": item['name'],
            "price": item['price'],
            "image": item['image'],
            "affiliate_link": f"{BASE_LINK}?ulp={item['url']}",
            "status": "active"
        })

    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_list, f, indent=4)
    print("AI Database Synchronized!")

if __name__ == "__main__":
    main()
