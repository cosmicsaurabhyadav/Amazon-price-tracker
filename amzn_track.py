import smtplib,requests,ssl,os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()
OWN_EMAIL = os.getenv('MY_USERNAME')
OWN_PASSWORD = os.getenv('MY_PASSWORD')


URL="https://www.amazon.in/gp/product/B0B31FR4Y2/ref=s9_acss_bw_cg_NewLL_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-8&pf_rd_r=BRJFWMXZBN8GZTZ79HB2&pf_rd_t=101&pf_rd_p=d3472a5b-9771-4f9b-8e7f-5862b00cbf4d&pf_rd_i=1388921031"
HEADER={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
    "Accept-Language": "en-US,en;q=0.9"
}

Given_limit=5000

response=requests.get(URL, headers=HEADER)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
product_name=soup.find("span",id='productTitle').text.strip()
stuff = (soup.find(class_="a-offscreen")).text.replace(',', '')
print(product_name)
print(stuff)
price=stuff.replace("₹","")

s = smtplib.SMTP(host="smtp.gmail.com", port=587)
s.starttls()
s.login(OWN_EMAIL,OWN_PASSWORD )

message = f"""\
Subject: Low Price Alert -- ₹{price} for {product_name}

{product_name}'s

PRICE IS DROPPED!! 📉

from your expected price  ₹{Given_limit}  ☞  ₹{price}.

Check it now!!!:
{URL}   """     
def notify():
    if float(price)<float(Given_limit):
        print("send mail immediately")
            
        try:
            print("this")
            s.sendmail(OWN_EMAIL, OWN_EMAIL, message.encode('utf-8'))         
            print ("Successfully sent email")
        except smtplib.SMTPException:
            print("that")
            print ("Error: unable to send email")
        

    else:
        print("not now")
    
notify()

print("done now......")

