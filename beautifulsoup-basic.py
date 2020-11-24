import requests
from bs4 import BeautifulSoup

webURL = 'https://www.goldtraders.or.th'
r = requests.get(webURL)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text,'lxml')

def GoldPriceCheck():

    # PriceCheck = soup.find(id = 'DetailPlace_uc_goldprices1_lblAsTime').text
    # print(PriceCheck)

    print("Gold Price by GTA / ราคาทองตามประกาศของสมาคมค้าทองคำ")
    print( "ประจำวันที่ " + soup.find(id = 'DetailPlace_uc_goldprices1_lblAsTime').text)
    print("ทองคำแท่ง 96.5% ")
    print("ขายออก " + soup.find(id='DetailPlace_uc_goldprices1_lblBLSell').text + " บาท")
    print("รับซื้อ " + soup.find(id='DetailPlace_uc_goldprices1_lblBLBuy').text + " บาท")


GoldPriceCheck()