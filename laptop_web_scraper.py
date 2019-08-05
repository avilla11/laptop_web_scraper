from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Laptops-Notebooks/SubCategory/ID-32'

#opening connection and grabbing page
uClient = uReq(my_url)

#oplacing conent onto a variable
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"

#places the scraped info into a csv file with headers
f = open(filename, "w")

headers = "product_brand, product_name, product_shipping, product_price\n"
 
f.write(headers)
 
 #tries to scrape info and if info does not exist it covers it with a try except
for container in containers:
    try:
        product_name = container.find("div", "item-info").div.a.img["title"]
    except Exception as e:
        product_brand = "NA"
    else:
        pass
    finally:
        pass
 	
 	#scrapes the item title
    title_container = container.findAll("a", {"class": "item-title"})
 
    product_brand = title_container[0].text
 
 	#scrapes the shipping cost
    shipping_container = container.findAll("li", {"class": "price-ship"})
 
    product_shipping = shipping_container[0].text.strip()

    #scrapes the shipping cost
    price_container = container.findAll("li", {"class": "price-current"})
 
    product_price = price_container[0].text
 
 	#prints the scraped info
    print("product_brand: " + product_brand)
    print("product_name: " + product_name)
    print("product_shipping: " + product_shipping)
    print("product_price: " + product_price)
 

    f.write(product_name.replace(",", "|") + "," + product_brand + "," + product_shipping + "\n")
 
f.close()