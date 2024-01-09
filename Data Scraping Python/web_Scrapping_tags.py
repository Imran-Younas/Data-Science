from bs4 import BeautifulSoup
import requests
url = "https://www.flipkart.com/mobiles/~cs-lc6ah0kamu/pr?sid=tyy%2C4io&collection-tab-name=Poco+X3+Pro&sort=price_asc&param=245&otracker=clp_banner_1_7.bannerX3.BANNER_mobile-phones-store_JV8S45JL8Z4N&fm=neo%2Fmerchandising&iid=M_3e37b802-51db-426e-88f2-9cec6afd94c6_7.JV8S45JL8Z4N&ssid=jnh0p6gdpb0j2yv41626085659374"
response = requests.get(url)
#print(response) #check responce if it is = 200 its mean code are going well
#print(response.content) # to print html code 

htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

# print(soup.prettify())
# print(soup.title) # to print any title
# print (soup.title.soup) # print name of titile 
# print(soup.title.string) # to print string of any title
# print(soup.title.parent.name) # print parenr of title
# print(soup.p) #print paragraph 
# print(soup.find_all('p')) #print all paragraph 
# print(soup.a) #print ankar tags
# print(soup.find_all('a')) #print all ankar tags
# print(soup.find(id=""))

# for link in soup.find_all('a'):   # for get link 
#     print(link.get('href')) # for print link

# for image in soup.find_all('img'):   # for get image 
#     print(image.get('src')) # for print image

# product = soup.find_all('div')
# print(product)

# product = soup.find_all('div', class_= 'card-channels-icon align-left')
# print(product)  # find in div class data


