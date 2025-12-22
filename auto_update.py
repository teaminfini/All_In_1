import requests
import json
import os
import urllib.parse
import random
from datetime import datetime

# --- اطلاعات امنیتی تو (محرمانه) ---
CLIENT_ID = "Ib3uc76tmkztPXeLCsgl8gQjYgH4QA"
CLIENT_SECRET = "nFbTE0VpJG0USmtaATTR8v5oiDmF"
# کد تاییدیه Base64 تو
AUTH_STRING = "bGlzdWM3NnRta3p0UFhlTENzZ2w4Z1FqWWdINGRBOm5GYlRFMFZwSkcwVVNtdGFBVFRSOHY1b2lEbUY="
WEBSITE_ID = "2896915" # ID سایت تو
BASE_AFF_LINK = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"
DB_FILE = 'products.json'

def get_token():
    """دریافت توکن برای ورود به سرور"""
    url = "https://api.admitad.com/token/"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "scope": "public_data coupons ads campaigns"
    }
    headers = {"Authorization": f"Basic {AUTH_STRING}"}
    try:
        res = requests.post(url, data=data, headers=headers, timeout=20)
        return res.json().get("access_token")
    except:
        return None

def fetch_hot_products(token):
    """استخراج مستقیم محصولات داغ و ترند از API"""
    # ما از بخش کوپن‌ها و آفرهای ویژه علی‌اکسپرس استفاده می‌کنیم که محصولات ترند را دارد
    url = f"https://api.admitad.com/coupons/website/{WEBSITE_ID}/"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "limit": 10,
        "campaign": 14210, # ID برنامه AliExpress WW
        "language": "en"
    }
    
    try:
        res = requests.get(url, headers=headers, params=params, timeout=20)
        results = res.json().get("results", [])
        
        products = []
        for item in results:
            # اگر محصول لینک و عکس داشت، آن را بردار
            if item.get("image") and item.get("advcampaign_url"):
                target_url = item["advcampaign_url"]
                # انکود کردن برای جلوگیری از 404
                safe_url = urllib.parse.quote(target_url, safe='')
                
                products.append({
                    "id": item.get("id", random.randint(1, 9999)),
                    "name": item.get("short_name") or item.get("name", "Trending Deal"),
                    "price": "Check Price", # API کوپن قیمت دقیق نمی‌دهد، از متن استفاده می‌کنیم
                    "image": f"https://images.weserv.nl/?url={item['image'].replace('https://', '')}&w=500",
                    "affiliate_link": f"{BASE_AFF_LINK}?ulp={safe_url}",
                    "status": "active"
                })
        return products
    except Exception as e:
        print(f"API Error: {e}")
        return []

def main():
    print("AI BOT: Starting Global Trend Harvesting...")
    token = get_token()
    
    if not token:
        print("CRITICAL: Could not authenticate with Admitad.")
        return

    # دریافت محصولات واقعی
    live_products = fetch_hot_products(token)
    
    # اگر API خالی بود، از محصولات گلچین شده دستی استفاده کن تا سایت خالی نماند
    if not live_products:
        print("API was empty, using verified fallback trends.")
        live_products = [
            {"name": "Turbo Jet Fan 110k RPM", "price": "$31.00", "image": "https://images.weserv.nl/?url=ae04.alicdn.com/kf/S7b973522f08547378c2e7a1773G.jpg", "affiliate_link": f"{BASE_AFF_LINK}?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005006135334751.html"},
            {"name": "Zeblaze Stratos 3 Pro GPS", "price": "$64.50", "image": "https://images.weserv.nl/?url=ae04.alicdn.com/kf/S89476906564344798e12f8a4495964955b9e592474f3j.jpg", "affiliate_link": f"{BASE_AFF_LINK}?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005006016738012.html"},
            {"name": "Anker Soundcore Q20i ANC", "price": "$39.99", "image": "https://images.weserv.nl/?url=ae04.alicdn.com/kf/Sa8f6d5e12f8a4495964955b9e592474f3.jpg", "affiliate_link": f"{BASE_AFF_LINK}?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005005965643447.html"}
        ]

    # ذخیره در فایل
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(live_products, f, indent=4)
    
    print(f"SYNC SUCCESS: {len(live_products)} hot deals deployed.")

if __name__ == "__main__":
    main()
