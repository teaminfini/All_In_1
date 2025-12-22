import json
import requests
import random

AFFILIATE_BASE = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"

def get_trends():
    # لیستی از محصولات واقعاً پرفروش علی‌اکسپرس که پتانسیل وایرال شدن دارند
    items = [
        {"name": "Mini Pocket Projector 4K", "price": "$45.90", "url": "https://www.aliexpress.com/item/1005006135334751.html", "img": "https://ae01.alicdn.com/kf/S8f9b90757a3e40408547378c2e7a1773G.jpg"},
        {"name": "Wireless Mechanical Keyboard", "price": "$29.10", "url": "https://www.aliexpress.com/item/1005005965643447.html", "img": "https://ae01.alicdn.com/kf/S064560751f9a460497554c2e7a1773G.jpg"},
        {"name": "RGB LED Smart Light Bar", "price": "$12.50", "url": "https://www.aliexpress.com/item/1005005578432101.html", "img": "https://ae01.alicdn.com/kf/Sf5e12f8a4495964955b9e592474f3j.jpg"},
        {"name": "Portable Turbo Jet Fan", "price": "$18.20", "url": "https://www.aliexpress.com/item/1005006135334751.html", "img": "https://ae01.alicdn.com/kf/S8f9b90757a3e40408547378c2e7a1773G.jpg"}
    ]
    return items

def main():
    print("Finding trends...")
    trends = get_trends()
    
    final_products = []
    for item in trends:
        final_products.append({
            "name": item['name'],
            "price": item['price'],
            "image": item['img'],
            "affiliate_link": f"{AFFILIATE_BASE}?ulp={item['url']}",
            "status": "active"
        })

    with open('products.json', 'w') as f:
        json.dump(final_products, f, indent=4)
    print("Done! Site updated.")

if __name__ == "__main__":
    main()
