import requests
from bs4 import BeautifulSoup as bs



running = True

while running: 
    urlInput = input("Url adresini girin: ")

    if not urlInput.startswith("https:"):
        print("Lütfen geçerli bir url adresi girin")
        continue

    response = requests.get(urlInput)
   

    soup = bs(response.content, "html.parser")

    productTitle = soup.find("h1", class_ = "product-title")
    addBasketButton = soup.find("button", class_ = "add-to-basket")


    if addBasketButton != None:
        print(productTitle.text + " in Stock")
    else: 
        print(productTitle.text + " not in stock")



    


