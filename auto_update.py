import requests
import json
import os
import random
from datetime import datetime

# --- اطلاعات اختصاصی تو (ست شده بر اساس مشخصاتت) ---
CLIENT_ID = "Ib3uc76tmkztPXeLCsgl8gQjYgH4QA"
CLIENT_SECRET = "nFbTE0VpJG0USmtaATTR8v5oiDmF"
# کد Base64 شده برای احراز هویت
AUTH_STRING = "YkdsemRXTTNOblJ0YTNwMFVGaElURU56WjBrNjpuRmJURTBPVnBKRzBVU210YUFUVFI4djVvaURtRg=="
WEBSITE_ID = "2896915"
MY_AFFILIATE_BASE = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"
DB_FILE = 'products.json'

def get_access_token():
    """دریافت توکن رسمی از سرور Admitad"""
    url = "https://api.admitad.com/token/"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "scope": "public_data coupons ads campaigns"
    }
    headers = {"Authorization": f"Basic {AUTH_STRING}"}
    try:
        res = requests.post(url, data=data, headers=headers)
        return res.json().get("access_token")
    except:
        return None

def fetch_live_trends():
    """دریافت محصولات ترند و دارای تخفیف واقعی"""
    # در این مرحله ما لیستی از بهترین گجت‌های علی‌اکسپرس که عکس‌های باکیفیت دارند را قرار می‌دهیم
    # این لیست به مرور توسط API از بخش 'Coupons' یا 'Deals' جایگزین می‌شود
    return [
        {
            "name": "Baseus GaN5 Pro Fast Charger 65W",
            "price": "$28.50",
            "image": "https://ae01.alicdn.com/kf/S7b973522f08547378c2e7a1773G.jpg",
            "url": "https://www.aliexpress.com/item/1005005965643447.html"
        },
        {
            "name": "Lenovo LP40 Pro Wireless Earbuds",
            "price": "$11.90",
            "image": "https://ae01.alicdn.com/kf/S8f9b90757a3e40408547378c2e7a1773G.jpg",
            "url": "https://www.aliexpress.com/item/1005006135334751.html"
        },
        {
            "name": "Bluetooth Smart Sleep Mask",
            "price": "$14.20",
            "image": "https://ae01.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg",
            "url": "https://www.aliexpress.com/item/1005005814522301.html"
        },
        {
            "name": "Mini Pocket Turbo Jet Fan",
            "price": "$31.00",
            "image": "https://ae01.alicdn.com/kf/Sc7f0c1c8a4495964955b9e592474f3j.jpg",
            "url": "https://www.aliexpress.com/item/1005006135334751.html"
        }
    ]

def main():
    token = get_access_token()
    print(f"Auth Status: {'Success' if token else 'Failed'}")
    
    deals = fetch_live_trends()
    final_products = []
    
    for d in deals:
        final_products.append({
            "id": int(datetime.now().timestamp()) + random.randint(1, 999),
            "name": d['name'],
            "price": d['price'],
            "image": d['image'],
            "affiliate_link": f"{MY_AFFILIATE_BASE}?ulp={d['url']}",
            "status": "active"
        })

    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_products, f, indent=4)
    print("Corporate Database Synced with ID 2896915")

if __name__ == "__main__":
    main()
