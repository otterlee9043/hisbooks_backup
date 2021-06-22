from django.db import models


# class Advertisements(models.Model):
#     owner = models.CharField(max_length=40, blank=True, null=True)
#     ad_image = models.CharField(max_length=200, blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Advertisements'


# class AlphaInfo(models.Model):
#     isbn = models.OneToOneField('BookInfo', models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
#     stock = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Alpha_Info'


# class BookInfo(models.Model):
#     isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=13)  # Field name made lowercase.
#     title = models.CharField(max_length=60)
#     author = models.CharField(max_length=60)
#     image = models.CharField(max_length=100, blank=True, null=True)
#     publisher = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'Book_info'


# class Classes(models.Model):
#     professor = models.CharField(primary_key=True, max_length=50)
#     course_name = models.CharField(max_length=100, blank=True, null=True)
#     course_id = models.CharField(max_length=9)
#     section_id = models.CharField(max_length=3)
#     have_book = models.IntegerField(blank=True, null=True)
#     isbn = models.ForeignKey(BookInfo, models.DO_NOTHING, db_column='ISBN', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Classes'
#         unique_together = (('professor', 'course_id', 'section_id'),)


# class Complaints(models.Model):
#     complain_id = models.AutoField(primary_key=True)
#     complaintee = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='complaintee', blank=True, null=True)
#     complainer = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='complainer', blank=True, null=True)
#     date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Complaints'


# class Coursebookrelation(models.Model):
#     littleused = models.IntegerField(db_column='littleUsed', blank=True, null=True)  # Field name made lowercase.
#     used = models.IntegerField(db_column='Used', blank=True, null=True)  # Field name made lowercase.
#     oftenused = models.IntegerField(db_column='oftenUsed', blank=True, null=True)  # Field name made lowercase.
#     year = models.CharField(max_length=4)
#     semester = models.CharField(primary_key=True, max_length=4)
#     isbn = models.ForeignKey(BookInfo, models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
#     course = models.ForeignKey(Classes, models.DO_NOTHING)
#     section = models.ForeignKey(Classes, models.DO_NOTHING)
#     professor = models.ForeignKey(Classes, models.DO_NOTHING, db_column='professor')

#     class Meta:
#         managed = False
#         db_table = 'CourseBookRelation'
#         unique_together = (('semester', 'year', 'professor', 'course', 'section', 'isbn'),)


# class LibraryInfo(models.Model):
#     isbn = models.OneToOneField(BookInfo, models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
#     exist = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Library_Info'


# class UsedBookInfo(models.Model):
#     usedbook_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     isbn = models.ForeignKey(BookInfo, models.DO_NOTHING, db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
#     price = models.IntegerField(blank=True, null=True)
#     date = models.DateTimeField(blank=True, null=True)
#     quality = models.IntegerField()
#     year = models.CharField(max_length=4, blank=True, null=True)
#     semester = models.CharField(max_length=4, blank=True, null=True)
#     is_sold = models.IntegerField()
#     image = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Used_Book_Info'


# class UserInfo(models.Model):
#     user_id = models.CharField(primary_key=True, max_length=20)
#     complain_numbers = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'User_Info'