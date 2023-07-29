from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

TOKEN = <YOUR_TOKEN> #@BotFather will give it to you 
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
PRODUCT_URL = <YOUR_PRODUCT_URL> # "https://www.amazon.in/POCO-Pro-Yellow-128GB-Storage/dp/B0B6GDLMQK/ref=sr_1_1?crid=3EB9ZPVILWI2J&keywords=poco+x4+pro+5g&qid=1690330911&sprefix=poco+x4+pro%2Caps%2C243&sr=8-1
TARGET = <YOUR_TARGET_PRICE> # 17000
CHAT_ID = <YOUR_CHAT_ID> 

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) \
        Gecko/20100101 Firefox/91.0"
    }

cookies = {
    "csm-hit": "",
    "session-token": "",
    "ubid-acbin": "",
    "i18n-prefs": "",
    "lc-acbin": "",
    "session-id-time": "",
    "session-id": "",
}    #UPDATE THEM FROM YOUR BROWSER 

def get_prices(url=PRODUCT_URL):
    
    sess = requests.Session()
    sess.headers.update(headers)
    sess.cookies.update(cookies)
    response = sess.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    input_tag = soup.find("input", {"id": "attach-base-product-price"})
    price_primary = float(input_tag["value"])

    price_tag = soup.find("span", {"class": "a-price-whole"})
    price_whole = float(price_tag.text.replace(",", ""))
    return price_primary, price_whole

def send_telegram_message(message, chat_id=CHAT_ID):
    """Sends a message to a specified chat in Telegram."""
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(TELEGRAM_API_URL, data=data, timeout=20)
    return response.json()

@app.get("/")
def check_price():
    message = ''
    try:
        price_primary, price_whole = get_prices()
        if price_primary == price_whole:
            message = f"Price of product is {price_primary}"
            if price_primary <= TARGET:
                message = f"ALERT PRICE DROP Price of product is {price_primary}"
        else:
            message = (
                f"Price mismatch for product between {price_primary} and {price_whole}"
            )
            if price_primary <= TARGET or price_whole <= TARGET:
                message = f"ALERT PRICE DROP WITH MISMATCH Price of product is {min(price_primary,price_whole)}"
    except Exception as e:
        message = f"Error: {str(e)}"
    finally:
        send_telegram_message(message)
        return {"message": message}    

