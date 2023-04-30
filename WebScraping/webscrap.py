from fileinput import filename
import requests as req
from bs4 import BeautifulSoup as soup

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

#getting the html page
r = req.get(url)

#storing the html content
htmlcontent = r.content

#parsing the html content
page_soup = soup(htmlcontent, 'html.parser')
# print(page_soup)

containers = page_soup.find_all("div", {"class": "_13oc-S"})
# print(len(containers))
# print(soup.prettify(containers[0]))

container = containers[0]
# print(container.div.img["alt"])

price = container.findAll("div", {"class": "col col-5-12 nlI3QM"})
# print(price[0].text)

ratings = container.findAll("div", {"class": "gUuXy-"})
# print(ratings[0].text)

filename = "products.csv"
f= open(filename,"w")

headers = "Product_Name, Pricing, Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class": "col col-5-12 nlI3QM"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "gUuXy-"})
    rating = rating_container[0].text

    # print("product_name: " + product_name)
    # print("price: " + price)
    # print("rating: " + rating)

    # string parsing 
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("r")
    add_rs_price = "Rs." + rm_rupee[1]
    split_price = add_rs_price.split('E')
    finalprice = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + finalprice + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + finalprice + "," + final_rating + "\n")

f.close()

