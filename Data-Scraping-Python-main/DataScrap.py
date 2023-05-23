from bs4 import BeautifulSoup
import requests
url = "https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=sort%3Dpopularity&sid=tyy%2F4io&wid=1.productCard.PMU_V2_1"
response = requests.get(url)

htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
prices = []
images = []

a = open("Filpkart.txt", mode='w')

for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    tt = d.find('div', attrs={'class':'_4rR01T'})
    a.write("Phone Name: ")
    a.write(tt.string)
    a.write("\n")

    
    im = d.find('img', attrs={'class':'_396cs4 _3exPp9'})
    a.write("Phone Image Link: ")
    a.write(im.get('src'))
    a.write("\n")

    p = d.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    a.write("Phone Price: ")
    a.write(p.string)
    a.write("\n")

    a.write("----------------------------------")
    a.write("\n")
    a.write("\n")
  
  



     


      

  
