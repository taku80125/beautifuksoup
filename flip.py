from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys


my_url = 'https://www.99acres.com/rent-paying-guest-pg-in-koramangala-bangalore-south-ffid'

headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
print (response.getcode())
print (response.read())

uClient=uReq(my_url)

page_html=uClient.read()


uClient.close()
page_soup =soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "wrapttl"})
container = containers[0]

print(len(containers))

# print(soup.prettify(containers[23])) 
# price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
# print(price[0].text)

# #for name
# print(container.div.img["alt"])
# ratings = container.findAll("div", {"class": "niH0FQ"})

# # # container=containers[0]
# print(ratings[0].text)


# # creating file
# filename="products.csv"
# f=open(filename,"w")

# headers="Product_Name, Pricing, Rating\n"
# f.write(headers)

# for container in containers:
#     product_name=container.div.img["alt"]

#     price_container = container.findAll(
#         "div", {"class": "col col-5-12 _2o7WAb"})
#     price=price_container[0].text.strip()

#     rating_container = container.findAll("div", {"class": "niH0FQ"})
#     rating=rating_container[0].text


#     # print("product_name:" + product_name)
#     # print("price:"+ price)

#     # print("ratings:" + rating)

#     #string

#     trim_price=''.join(price.split(','))
#     rm_rupee=trim_price.split("₹")
#     add_rs_price ="Rs." + rm_rupee[1]
    
#     split_price=add_rs_price.split("E")
#     final_price=split_price[0]

#     split_rating = rating.split(" ")
#     final_rating=split_rating[0]

#     print(product_name.replace("," ,"|")+ "," + final_price + "," + final_rating + "\n")
#     f.write(product_name.replace(",", "|")+ "," +final_price + "," +final_rating + "\n")

# f.close()