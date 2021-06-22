from django.shortcuts import redirect, render
from django.db import connection
from .models import *
from django.urls import reverse
from django.views.generic import TemplateView
from PIL import Image
import base64
from io import BytesIO
from django.shortcuts import render
from django.db import connection
import requests
from bs4 import BeautifulSoup
import json
import re
import urllib.request

# Create your views here.
def index4(request):
    
    return render(request, "index4.html")

def upload(request):
    print("Uploaded~")
    return render(request, "searchenter.html")


def complain(request, complaintee, complainer):
    print(complainer)
    query = """INSERT INTO Complaints (complaintee, complainer, date) 
                VALUES ('""" + complaintee+ """', '""" + complainer + """', CURRENT_TIMESTAMP);"""
    cur = connection.cursor()
    print(query)
    cur.execute(query)
    
    # return render(request, "index4.html")
    return redirect("index4")

def book_sold(request, post_id):
    print(post_id)
    query = """UPDATE Used_Book_Info SET is_sold = true WHERE usedbook_id =""" + post_id + """;""" 
    print("QUERY!")
    print(query)

    cur = connection.cursor()
    cur.execute(query)
    
    return redirect("index4")




class PostUpload(TemplateView):
    def get(self, request):
        print("get!")
        return render(request, 'index4.html', {"searched": False})
    def post(self, request):
        print("post..")
        print(request)
        book_title = request.POST['bookTitle']
        price = request.POST['price']
        course = request.POST['course']
        section = request.POST['section']
        quality = request.POST['quality']
        year = request.POST['year']
        semester = request.POST['semester']
        description = request.POST['description']
        # image = request.POST.get('frontImg', False)
        image = request.FILES['frontImg']
        buffer = BytesIO()
        im = Image.open(image)
        im.save(buffer, format='jpeg')
        img_str = base64.b64encode(buffer.getvalue()) # base 64로 encode
        # img_str = im.decode('UTF-8') # UTF-8로 decode
        img_str = img_str.decode('UTF-8')
        #img_df = pd.DataFrame({})
        print(request.user)
        
        cursor = connection.cursor()
        # course_string = course + "-"+ section
        # query_test = \
        # """
        # SELECT course_id
        # FROM Classes
        # WHERE course_id = '""" + course_string + """';
        # """
        
        # test_result = cursor.execute(query_test)
        # print(test_result) 
        # if test_result == 0: # 과목코드가 자 
        #     print("NO CLASS!")
        #     return redirect('upload')

        # else:
        #     query_test2 = \
        #     """
        #     SELECT *
        #     FROM CourseBookRelation
        #     WHERE course_id ='""" + course +"""' AND section_id = '""" + section +""";
        #     """

        #     # 과목코드와 학기를 가지고 교수님 찾기
        #     query_professor = \
        #         """
        #         SELECT professor FROM Classes 
        #         WHERE  course_id = '""" + course + """' AND section_id = """ + section
            
        #     # 책의 ISBN
        #     query_ISBN = """SELECT ISBN 
        #                     FROM Book_Info
        #                     WHERE title LIKE '%""" + book_title +"""%'"""


        #     if cursor.execute(query_test2) == None:
        #         query_insert = \
        #             """
        #             INSERT INTO CourseBookRelation (semester, ISBN, course_id, section_id, professor)
        #             VALUES (""" + semester + """, (""" + query_ISBN + """) , '""" + course + """' , '""" + section + """', (""" + query_professor + """)))
        #             """
                
            
        query1 = """
        INSERT INTO Used_Book_Info (user_id, description, ISBN, price, date, quality, image, semester) 
        VALUES ('"""+request.user.username+"""', '"""+ description + """', '9788979143171', """+ price + """, CURRENT_TIMESTAMP, """ + quality + """, '""" + img_str+"""','""" + semester +"""');"""
        
        # print(query)
        cursor.execute(query1)

        return render(request, 'index4.html', {"searched": False})



def do_usedbooksearch(request, book_title):
    print("Hey!")
    if request.method == 'GET':
        book_title = request.GET['book_title']
        print("The book_title is "+book_title)

    cur = connection.cursor()

    
    # 책 제목 0, 가격 1, 상태 2, 사진 3, 내용 4, 말머리 5, 날짜 6, 유저 id 7, 컴플레인 개수 8, 게시글 id 9, 
    query ="""SELECT title, price, quality, UB.image, description, is_sold, date, U.user_id, complain_numbers, usedbook_id 
            FROM Book_Info B JOIN Used_Book_Info UB JOIN User_Info U
            ON B.ISBN = UB.ISBN AND U.user_id = UB.user_id AND B.title LIKE '%"""+ book_title+"""%'
            ORDER BY date DESC;"""
    print(query)
    
    print("Book list")

    cur.execute(query)
    book_list = cur.fetchall()
    
    if not book_list:
        print("Empty")
        searched = False
        book_title = None
    else:
        # print(book_list)
        book_title = book_list[0][0]
        searched = True

        
    print("searched is " + str(searched))

    return render(request, "index4.html", {"searched": searched, "book_list" :book_list, "book_title": book_title})

def popup_booksearch(request, course_info):
    print("course_info in popup_booksearch:")
    print(course_info)
    return render(request, "popups/coursebook.html", {"course_info":course_info})

def do_popup_booksearch(request, title):
    print("You are in do_popup_booksearch")
    if request.method == 'GET':
        title = request.GET.get('title')
    book_list_prejson = []
    book_list_prejson = onlinecrawler(title)
    book_list = json.loads(book_list_prejson)
    print(book_list)
    return render(request, "popups/coursebook.html", {"book_list": book_list})


class Insert_bookinfo(TemplateView):
    template_name="coursebook.html"
    print("You are in Insert_boookinfo")

    def get(self, request, title, course_info):
    # def get(self, request, title):
        print("within get of Insert_bookinfo")
        if request.method == 'GET':
            title = request.GET.get('title')
        book_list_prejson = []
        book_list_prejson = onlinecrawler(title)
        book_list = json.loads(book_list_prejson)
        print("course info in Insert bookinfo")
        print(course_info)
        return render(request, "popups/coursebook.html", {"book_list": book_list, "course_info": course_info})

    def post(self, request, course_info, title):
        cursor = connection.cursor()
        course_id = ''
        section_id=''
        professor_name = ''
        boook_isbn = ''
        if request.method == 'POST':
            boook_isbn = request.POST.get('isbn')
        print("POST boook_isbn is:", boook_isbn)

        if course_info:
            course_info = course_info.strip(")(")
            stripped_course_info = course_info.split(",")
            print("course info in POST: ")
            course_id = eval(stripped_course_info[2])
            course_id = course_id.replace("'","")
            section_id = eval(stripped_course_info[3])
            section_id = section_id.replace("'","")
            professor_name = eval(stripped_course_info[0])
            professor_name = professor_name.replace("'","")
            print(course_id)
            print(section_id)
            print(professor_name)
        print("****************************************")
        json_data = onlinecrawler(boook_isbn)
        # json_data = json.dumps(onlinecrawler(boook_isbn)) 
        loaded_json = json.loads(json_data)

        # loaded_json = json.load(json_data)
        print("loopint through json data")
        print("type is:")
        this_isbn = loaded_json[0]['isbn']
        this_isbn = this_isbn.replace("'","")
        this_title = loaded_json[0]['title']
        this_title = this_title.replace("'","")
        print(this_title)
        this_publisher = loaded_json[0]['publisher']
        this_publisher = this_publisher.replace("'","")
        print(this_publisher)
        qry_bookInsert = """INSERT INTO Book_info(ISBN, title, publisher) VALUES ('"""+ this_isbn + """', '""" + this_title + """','""" + this_publisher + """');"""
        cursor.execute(qry_bookInsert)
        print(qry_bookInsert)

        qry_coursebook = \
        """INSERT INTO CourseBookRelation ( ISBN, professor, course_id, section_id ) 
        VALUES( (SELECT ISBN FROM Book_info WHERE Book_info.ISBN = '""" + this_isbn +"""'), 
                (SELECT professor FROM Classes WHERE professor = '"""+ professor_name +"""' AND course_id = '""" + course_id + """' AND section_id IN ('"""+ section_id+"""', '0"""+ section_id+"""')), 
                (SELECT course_id FROM Classes WHERE professor = '"""+ professor_name +"""' AND course_id = '""" + course_id + """' AND section_id IN ('"""+ section_id+"""', '0"""+ section_id+"""')), 
                (SELECT section_id FROM Classes WHERE professor = '"""+ professor_name +"""' AND course_id = '""" + course_id + """' AND section_id IN ('"""+ section_id+"""', '0"""+ section_id+"""')));"""
        print(qry_coursebook)
        # cursor.execute(qry_coursebook)
        response = redirect('/courses/')
        return response


def onlinecrawler(title):
    #검색 질의 요청
    res = searchbook(title)
    if(res == None):
        print("검색 실패!!!")
        exit()
    #검색 결과를 json개체로 로딩
    jres = json.loads(res)
    if(jres == None):
        print("json.loads 실패!!!")
        exit()
    thislist = list()
    for post in jres['items']:
        post['title'] = re.sub('(<([^>]+)>)', '', post['title'])
        post['author'] = re.sub('(<([^>]+)>)', '', post['author'])
        post['isbn'] = re.sub('(<([^>]+)>)', '', post['isbn'])
        post['publisher'] = re.sub('(<([^>]+)>)', '', post['publisher'])
        thislist.append({"image": post['image'], "title": post['title'],"author": post['author'],"publisher": post['publisher'],"price": post['discount'],"isbn": post['isbn'][-13:], "link": post['link']})
    json_list = json.dumps(thislist, ensure_ascii=False)
    return json_list    
 
def searchbook(title):
    #애플리케이션 클라이언트 id 및 secret
    client_id = "n801iJfrUIABguAAx8Cw"
    client_secret = "DR06T766QJ"
    
    #도서검색 url
    url = "https://openapi.naver.com/v1/search/book.json"
    option = "&display=3&sort=count"    
    query = "?query="+urllib.parse.quote(title)
    url_query = url + query + option
    
    #Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    
    #검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        return response.read().decode('utf-8')
    else:
        return None