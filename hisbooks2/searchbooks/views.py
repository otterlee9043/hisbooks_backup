from bs4.element import ProcessingInstruction
from django.shortcuts import render
from .forms import BookSearchForm
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
# Create your views here.
import ssl

context = ssl._create_unverified_context()

def booksearch(request):
    return render(request, "searchpage.html", {"searchfound": False})

def do_booksearch(request, title):
    if request.method == 'GET':
        title = request.GET['title']
    # print("The title is ", title)
    bookList = []
    bookList = crawler(title)
    onlinebookcrawler(title)
    search_new_book(title)
    return render(request, "searchpage.html", {"searchfound": True, "bookList": bookList})


def onlinebookcrawler(book_title):
    #import    
    #애플리케이션 클라이언트 id 및 secret
    client_id = "n801iJfrUIABguAAx8Cw"
    client_secret = "DR06T766QJ"
    #도서검색 url
    #디폴트(json) https://openapi.naver.com/v1/search/book?query=python&display=3&sort=count
    #json 방식 https://openapi.naver.com/v1/search/book.json?query=python&display=3&sort=count
    #xml 방식  https://openapi.naver.com/v1/search/book.xml?query=python&display=3&sort=count
    url = "https://openapi.naver.com/v1/search/book.json"
    option = "&display=3&sort=count"
    query = "?query="+urllib.parse.quote(book_title)
    url_query = url + query + option

    #Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    #검색 요청 및 처리
    response = urllib.request.urlopen(request, context = context)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error code:"+rescode)


def crawler(keyword): 
    book_list = []
    url = 'https://library.handong.edu/search/tot/result?st=KWRD&commandType=advanced&mId=&si=1&q='+ keyword +'&b0=and&weight0=&si=2&q=&b1=and&weight1=&si=3&q=&weight2=&_lmt0=on&lmtsn=000000000001&lmtst=OR&lmt0=m&_lmt0=on&_lmt0=on&_lmt0=on&lmt0=eb&_lmt0=on&inc=TOTAL&_inc=on&_inc=on&_inc=on&_inc=on&_inc=on&lmt1=TOTAL&lmtsn=000000000003&lmtst=OR&lmt2=TOTAL&lmtsn=000000000006&lmtst=OR&rf=&rt=&range=000000000021&cpp=10&msc=500'
    html = requests.get(url) 
    soup = BeautifulSoup(html.text, "html.parser")
    span_enabled = soup.find_all("li", {"class": "items"}) 
    limit = 2
    limit_index = 0
    for found_element in span_enabled:
        # print("@@@@@@@@@@@@@@@@@@@@@@Tis a new book@@@@@@@@@@@@@@@@@@@@@@")
        if found_element.find_all("span", {"class": "availableBtn enabled"}):
            book_info_list = []
            if limit_index > limit:
                print("Break: more than 3 searches")
                break
            limit_index = limit_index + 1
            _href = found_element.find("a", href=True)
            book_href = 'https://library.handong.edu/' + _href['href']
            book_info_list.append(book_href)
            small_html = requests.get(book_href)
            small_soup = BeautifulSoup(small_html.text, "html.parser")
            div_title = small_soup.find_all("div", {"class": "profileHeader"})
            for element in div_title:
                title = element.find("h3").text
                author = element.find("p").text
                book_info_list.append(title)
                book_info_list.append(author)
            book_list.append(book_info_list)

        else :
            print("You may not borrow")
    return book_list

def search_new_book(title):
    #애플리케이션 클라이언트 id 및 secret
    client_id = "n801iJfrUIABguAAx8Cw"
    client_secret = "DR06T766QJ"
    
    #도서검색 url
    url = "https://openapi.naver.com/v1/search/book.json"
    option = "&display=3&sort=count"  
    query = "?query=" + urllib.parse.quote(title)
    url_query = url + query + option
    
    # Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    
    # 검색 요청 및 처리
    response = urllib.request.urlopen(request, context = context)
    rescode = response.getcode()
    if(rescode == 200):
        return response.read().decode('utf-8')
    else:
        print("Fail")
        return None
        
 
#검색 결과 항목 정보 출력하기
def showitem(item):
    print("사진:"+item['image'])
    print("제목:"+item['title'])
    print("작가:"+item['author'])
    print("가격:"+item['discount'])
    print("설명:"+item['description'])
    print("================")

#프로그램 진입점
def search(keyword):
    #검색 질의 요청
    res = search_new_book(keyword)
    if(res == None):
        print("검색 실패!!!")
        exit()
    #검색 결과를 json개체로 로딩
    jres = json.loads(res)
    if(jres == None):
        print("json.loads 실패!!!")
        exit()
 
    #검색 결과의 items 목록의 각 항목(post)을 출력
    for post in jres['items']:
        showitem(post)
 


def index(request):
    return render(request, "hisbooks_templates/index.html", {})

def index2(request):
    return render(request, "hisbooks_templates/index2.html", {})

def index3(request):
    return render(request, "hisbooks_templates/index3.html", {})

