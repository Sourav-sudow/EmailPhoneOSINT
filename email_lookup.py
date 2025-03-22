import requests

API_KEY = "YOUR_APILAYER_ACCESS_KEY"  # Replace with your API key

def email_info(email):
    url = f"http://apilayer.net/api/check?access_key={API_KEY}&email={email}&format=1"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print("\n📧 Email Information:")
        print(f"✅ Valid: {data.get('format_valid', 'N/A')}")
        print(f"📍 Domain: {data.get('domain', 'N/A')}")
        print(f"🔍 Disposable: {data.get('disposable', 'N/A')}")
        print(f"🕵️‍♂️ Free Email: {data.get('free', 'N/A')}")
    
    else:
        print("❌ Error fetching email data.")
