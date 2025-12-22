import requests
import json
import os
from datetime import datetime
import urllib.parse

# --- تنظیمات اختصاصی تو ---
# لینکی که در عکس فرستادی را اینجا دقیقاً کپی کن:
BASE_AFFILIATE_LINK = "https://rzekl.com/g/1e8d114494f9dbcef44416525dc3e8/"
DB_FILE = 'products.json'

def create_deep_link(product_url):
    """این تابع لینک محصول را به لینک پولساز تو تبدیل می‌کند"""
    encoded_url = urllib.parse.quote(product_url)
    # ساختار استاندارد دی‌لینک در ادیتاد
    return f"{BASE_AFFILIATE_LINK}?ulp={encoded_url}"

def fetch_trending_products():
    """شبیه‌سازی پیدا کردن محصولات پربحث و ترند"""
    # در اینجا لیست محصولاتی که الان در دنیا ترند هستند را داریم
    # این لیست می‌تواند در آینده با اسکرپینگ یا API کامل‌تر شود
    trends = [
        {
            "name": "Portable Mini Turbo Jet Fan",
            "url": "https://www.aliexpress.com/item/1005006135334751.html",
            "price": "$15.99",
            "category": "Gadgets",
            "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500"
        },
        {
            "name": "Smart Sleep Mask with Bluetooth",
            "url": "https://www.aliexpress.com/item/1005005814522301.html",
            "price": "$12.50",
            "category": "Wellness",
            "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=500"
        }
    ]
    
    formatted_products = []
    for t in trends:
        formatted_products.append({
            "id": int(datetime.now().timestamp()) + hash(t['name']),
            "name": t['name'],
            "category": t['category'],
            "description": "Trending viral product with high demand and great reviews.",
            "price": t['price'],
            "affiliate_link": create_deep_link(t['url']),
            "image": t['img'],
            "status": "active",
            "last_checked": datetime.now().strftime("%Y-%m-%d")
        })
    return formatted_products

def main():
    print("Updating site with trending products...")
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            try:
                products = json.load(f)
            except: products = []
    else:
        products = []

    # ۱. چک کردن لینک‌های قدیمی (اگر خراب باشند حذف یا غیرفعال می‌شوند)
    for p in products:
        try:
            res = requests.head(p['affiliate_link'], timeout=5)
            p['status'] = 'active' if res.status_code < 400 else 'broken'
        except:
            p['status'] = 'broken'

    # ۲. اضافه کردن ترندهای جدید
    new_trends = fetch_trending_products()
    existing_names = [p['name'] for p in products]
    
    for nt in new_trends:
        if nt['name'] not in existing_names:
            products.insert(0, nt) # اضافه کردن به ابتدای لیست (بالای سایت)

    # ۳. محدود کردن تعداد محصولات (مثلاً فقط ۲۰ تای آخر) برای سرعت سایت
    products = products[:20]

    with open(DB_FILE, 'w') as f:
        json.dump(products, f, indent=4)
    
    print(f"Update complete. Total products: {len(products)}")

if __name__ == "__main__":
    main()
