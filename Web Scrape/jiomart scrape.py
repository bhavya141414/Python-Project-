
from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

import bs4

headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/83.0.4103.116 Safari/537.36'}

my_url = 'https://www.jiomart.com/c/groceries/dairy-bakery/dairy/62'



uclient = uReq(my_url)

page_html = uclient.read()

uclient.close()


bs41 = soup(page_html, 'html.parser')


containers = bs41.find_all('div', {'cat-item'})
#print(len(containers))


#print(soup.prettify(containers[0]))


for container in containers:
    p_name = container.find_all('span', {'class' : 'clsgetname'})
    productname = p_name[0].text

    o_p = container.find_all('span' , id = 'final_price' )
    offer_price = o_p[0].text

    a_p = container.find_all('strike', {'id' : 'price'})
    actual_price = a_p[0].text

    print('Product name is', productname)
    print('Product Mrp is', offer_price)
    print('Actual price is', actual_price)
    print()


   

  





