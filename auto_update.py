import json
import os

# لینک پایه افیلیت تو
MY_AFFILIATE_BASE = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"

def main():
    # محصولات با عکس‌های واقعی و هماهنگ
    new_products = [
        {
            "id": 101,
            "name": "Portable Turbo Jet Fan",
            "category": "Tech",
            "description": "High-speed powerful fan for cooling and cleaning electronics.",
            "price": "$19.99",
            # لینک محصول واقعی در علی اکسپرس
            "affiliate_link": f"{MY_AFFILIATE_BASE}?ulp=https://www.aliexpress.com/item/1005006135334751.html",
            # عکس واقعی توربو فن
            "image": "https://ae01.alicdn.com/kf/S8f9b90757a3e40408547378c2e7a1773G.jpg",
            "status": "active"
        },
        {
            "id": 102,
            "name": "Bluetooth Sleep Headphones",
            "category": "Lifestyle",
            "description": "Ultra-soft eye mask with built-in speakers for better sleep.",
            "price": "$14.50",
            # لینک محصول واقعی
            "affiliate_link": f"{MY_AFFILIATE_BASE}?ulp=https://www.aliexpress.com/item/1005005814522301.html",
            # عکس واقعی چشم‌بند بلوتوثی
            "image": "https://ae01.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg",
            "status": "active"
        }
    ]

    with open('products.json', 'w') as f:
        json.dump(new_products, f, indent=4)
    
    print("Database Updated with real images and links!")

if __name__ == "__main__":
    main()
