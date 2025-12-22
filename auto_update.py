import json
import os
import requests

# لینک افیلیت اختصاصی تو که از عکس برداشتم
MY_AFFILIATE_BASE = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"

def main():
    # لیست محصولاتی که می‌خواهیم همین الان در سایت ظاهر شوند
    # تو می‌توانی هر زمان خواستی این لیست را دستی زیاد کنی
    new_products = [
        {
            "id": 101,
            "name": "Mini Turbo Jet Fan - Viral Gadget",
            "category": "Tech",
            "description": "Powerful portable fan for cooling and cleaning. High velocity airflow.",
            "price": "$19.99",
            "affiliate_link": f"{MY_AFFILIATE_BASE}?ulp=https://www.aliexpress.com/item/1005006135334751.html",
            "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
            "status": "active"
        },
        {
            "id": 102,
            "name": "Bluetooth Sleep Eye Mask",
            "category": "Lifestyle",
            "description": "Soft sleep mask with built-in headphones for perfect rest.",
            "price": "$14.50",
            "affiliate_link": f"{MY_AFFILIATE_BASE}?ulp=https://www.aliexpress.com/item/1005005814522301.html",
            "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=500",
            "status": "active"
        }
    ]

    # ذخیره مستقیم در فایل - بدون هیچ شرطی تا مطمئن شویم فایل پر می‌شود
    with open('products.json', 'w') as f:
        json.dump(new_products, f, indent=4)
    
    print("Success! products.json has been updated.")

if __name__ == "__main__":
    main()
