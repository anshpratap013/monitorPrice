import bs4
import urllib.request
import smtplib
import time
prices_list=[]
def check_price():
    

    url = 'https://www.amazon.in/dp/B082MDMW3X/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=CF9JY0WX1GAAPBD3S9KW&pf_rd_t=101&pf_rd_p=8398f427-fbf5-4310-a31e-29a4be7a59bc&pf_rd_i=26297682031'
    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")
    price = soup.find(id="priceblock_dealprice").get_text()
    p1 = float(price.replace(",","").replace("₹",""))
    print(price)
    print(p1)
    prices_list.append(p1)
    return p1
check_price()

def send_email(message):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("anshtestiing123@gmail.com","anshpratap013@")
    s.sendmail("anshtestiing123@gmail.com","anshpratap013@gmail.com",message)
    s.quit()

send_email("Hi Ansh")
def price_decrease_check(prices_list):
    if prices_list[-1]<prices_list[-2]:
        return True
    else:
        return False
count = 1
while True:
    
    current_price = check_price()
    if count>1:
        flag = price_decrease_check(prices_list)
        if flag>1:
            decrease = prices_list[-1]-prices_list[-2]
            message = "The price has decreased please check the item and it has decreased by {decrese} rupees" 
            send_email(message)
    time.sleep(1)
    count+=1
