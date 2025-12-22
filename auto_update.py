import requests
import json
import os

# فایل دیتابیس ما
DB_FILE = 'products.json'

def check_links_and_status():
    print("Starting link validation...")
    
    # ۱. خواندن اطلاعات از فایل JSON
    if not os.path.exists(DB_FILE):
        print("Error: products.json not found!")
        return

    with open(DB_FILE, 'r') as f:
        products = json.load(f)

    updated = False

    # ۲. بررسی تک‌تک محصولات
    for product in products:
        link = product.get('affiliate_link')
        print(f"Checking: {product['name']}...")
        
        try:
            # ارسال یک درخواست سریع برای چک کردن زنده بودن لینک
            # ما از Header استفاده می‌کنیم تا ترافیک کمتری مصرف شود
            response = requests.head(link, timeout=10, allow_redirects=True)
            
            # اگر کد وضعیت بین ۲۰۰ تا ۳۹۹ باشد یعنی لینک سالم است
            if response.status_code >= 400:
                if product['status'] != 'broken':
                    product['status'] = 'broken'
                    updated = True
                    print(f"!!! ALERT: {product['name']} is broken (Status: {response.status_code})")
            else:
                if product['status'] != 'active':
                    product['status'] = 'active'
                    updated = True
                    print(f"--- OK: {product['name']} is active.")
                    
        except Exception as e:
            # اگر کلاً سایت باز نشود (مثلاً فیلتر باشد یا کلاً حذف شده باشد)
            if product['status'] != 'broken':
                product['status'] = 'broken'
                updated = True
                print(f"!!! ALERT: {product['name']} is unreachable. Error: {e}")

    # ۳. اگر تغییری در وضعیت لینک‌ها ایجاد شد، فایل را ذخیره کن
    if updated:
        with open(DB_FILE, 'w') as f:
            json.dump(products, f, indent=4)
        print("Database updated successfully.")
    else:
        print("No changes needed. All links are in their previous state.")

if __name__ == "__main__":
    check_links_and_status()
