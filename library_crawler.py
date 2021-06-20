# from re import T
# from bs4 import element
# from bs4.element import PYTHON_SPECIFIC_ENCODINGS, ProcessingInstruction
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def crawler(keyword): 
    url = 'https://library.handong.edu/search/tot/result?st=KWRD&si=TOTAL&websysdiv=tot&q=' + keyword +'&x=0&y=0'
    html = requests.get(url) 
    soup = BeautifulSoup(html.text, "html.parser")
    span_enabled = soup.find_all("li", {"class": "items"}) 
    for found_element in span_enabled:
        print("@@@@@@@@@@@@@@@@@@@@@@Tis a new book@@@@@@@@@@@@@@@@@@@@@@")
        if found_element.find_all("span", {"class": "availableBtn enabled"}):
            book_info = [element.text for element in found_element.find_all("dd", {"class": "info"})]
            print(book_info)
            _href = found_element.find("a", href=True)
            book_href = 'https://library.handong.edu/' + _href['href']
            print(book_href)
            ##
            imageSoup = BeautifulSoup(urlopen(book_href) , "html.parser")
            imagecontainer = imageSoup.find_all("dd", {"class": "bookImg"})
            print(imagecontainer)
            images = imageSoup.find_all("img", {"id": "coverimage"})
            print(images)
            # for image in images:
            #     # print(image['src'])
            #     image_href = 'https://library.handong.edu/' + image['src']
            #     print(image_href)

        else :
            print("You may not borrow")
        # print("@@@@@@@@@@@@@@@@@@@@@@Whole info@@@@@@@@@@@@@@@@@@@@@@")
        # print(found_element)
        # break

crawler('Data structure')