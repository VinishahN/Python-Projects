import smtplib
from bs4 import BeautifulSoup
import lxml
import requests
MY_EMAIL = "vinishahnagarajan@gmail.com"
PASSWORD = "twlheieeglanoojy"
URL = "https://www.amazon.in/dp/B084XMKTTC/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=BY2AQXQK74SK36RPC2Y0&pf_rd_t=101&pf_rd_p=8535c449-7388-4513-9d27-13adb10e6bd2&pf_rd_i=21541608031"
headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "X-Http-Proto": "HTTP/1.1",
    "X-Real-Ip": "124.123.255.121"
}
response = requests.get(url=URL,headers=headers)

website_html = response.text
soup = BeautifulSoup(website_html, "lxml")
price_tag = soup.find(name="span", id="priceblock_ourprice")
price_with_comma = price_tag.getText()
symbol = price_tag.getText().split()[0]
price_without_commas = float(price_tag.getText().split()[1].replace(",",""))
product_title = soup.find(name="span", id="productTitle").getText()
target_price = 31000
if target_price>price_without_commas :
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        message = f"Subject: Amazon Price Alert!\n\n{product_title} is now {price_with_comma}\n{URL}".encode('utf-8')
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="nvinishah@gmail.com", msg=message)


