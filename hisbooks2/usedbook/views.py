from django.shortcuts import render
from django.db import connection
from .models import *
from django.core.files.storage import default_storage
from django.views.generic import TemplateView
import pandas as pd
from PIL import Image
import base64
from django import template
from io import BytesIO
register = template.Library()


# Create your views here.
def index4(request):
    
    return render(request, "index4.html")

def upload(request):
    print("Uploaded~")
    return render(request, "searchenter.html")


def complain(request):

    return render(request, "complain.html")

# def upload_post(request):
#     print("Where are you")
#     if request.method == 'POST':
#         book_title = request.POST['bookTitle']
#         price = request.POST['price']
#         course = request.POST['course']
#         quality = request.POST['quality']
#         description = request.POST['description']
#         # image = request.POST.get('frontImg', False)
#         image = request.FILES['frontImg']
#         buffer = BytesIO()
#         im = Image.open(image)
#         im.save(buffer, format='jpeg')
#         img_str = base64.b64encode(buffer.getvalue()) # base 64로 encode
#         # img_str = im.decode('UTF-8') # UTF-8로 decode
#         img_str = img_str.decode('UTF-8')
#         #img_df = pd.DataFrame({})

#     cursor = connection.cursor()

#     print("Price is " + price)

#     query = """
#     INSERT INTO Used_Book_Info (user_id, description, ISBN, price, date, quality, image) 
#     VALUES ('sua@handong.edu', '"""+ description + """', '9791156641131', """+ price + """, CURRENT_TIMESTAMP, """ + quality + """, '""" + img_str+"""');"""
    
#     print(query)
#     cursor.execute(query)

#     return render(request, 'index4.html')

class PostUpload(TemplateView):
    template_name="searchenter.html"

    def get(self, request):
        print("get!")
        return render(request, 'index4.html', {"did_search": False})
    def post(self, request):
        print("post..")
        print(request)
        if request.method == 'POST':
            book_title = request.POST['bookTitle']
            price = request.POST['price']
            course = request.POST['course']
            quality = request.POST['quality']
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

        cursor = connection.cursor()

        
        print("Price is " + price)

        query = """
        INSERT INTO Used_Book_Info (user_id, description, ISBN, price, date, quality, image) 
        VALUES ('sua@handong.edu', '"""+ description + """', '9791156641131', """+ price + """, CURRENT_TIMESTAMP, """ + quality + """, '""" + img_str+"""');"""
        
        print(query)
        cursor.execute(query)

        return render(request, 'index4.html', {"did_search": True})


# class CommentUpload(TemplateView):

#     def get(self, request):
#         return render(request, 'index4.html')
#     def post(self, request, usedbook_id):
#         if request.method == 'POST':
#             comment_content = request.POST['comment']
#         cur = connection.cursor()
#         query = """INSERT INTO UsedBook_Comment (user_id, usedbook_id, text, date)
#                     VALUES ("""+ request.id +""", """+ usedbook_id +""", """ + comment_content + """, CURRENT_TIMESTAMP);"""
#         cursor.execute(query)

#         return render(request, 'index4.html')

def create_comment(request, usedbook_id):
    print("CREATE COMMENT")
    if request.method == 'POST':
        comment_content = request.POST['comment']
        cur = connection.cursor()
        query = """INSERT INTO UsedBook_Comment (user_id, usedbook_id, text, date)
                    VALUES ("""+ request.id +""", """+ usedbook_id +""", """ + comment_content + """, CURRENT_TIMESTAMP);"""
        cur.execute(query)

    return render(request, 'index4.html')
        
        
def do_usedbooksearch(request, book_title):
    print("Hey!")
    if request.method == 'GET':
        book_title = request.GET['book_title']
        print("The book_title is "+book_title)

    cur = connection.cursor()
    # 책 제목 0, 가격 1, 상태 2, 사진 3, 내용 4, 말머리 5, 날짜 6, 유저 id 7, 컴플레인 개수 8, 게시글 id 9, 
    query ="""SELECT title, price, quality, UB.image, description, is_sold, date, U.user_id, complain_numbers, usedbook_id 
            FROM Book_Info B JOIN Used_Book_Info UB JOIN User_Info U
            ON B.ISBN = UB.ISBN AND U.user_id = UB.user_id AND B.title LIKE '%"""+ book_title+"""%';"""
    print(query)
    

    print("Book list")

    cur.execute(query)
    book_list = cur.fetchall()
    comment_list = []
    for entry in book_list:
        query2 ="""SELECT usedbook_id, user_id, comment_id, text, date
                    FROM UsedBook_Comment UC 
                    WHERE  usedbook_id='""" + entry[7] + """';"""
        cur.execute(query2)
        comments = cur.fetchall()
        comment_list.extend(comments)
    
    print(comment_list)

    return render(request, "index4.html", {"book_list" :book_list})
