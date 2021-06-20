from django.db import models


class AlphaInfo(models.Model):
    isbn = models.OneToOneField('BookInfo', models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
    price = models.CharField(max_length=6)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Alpha_Info'


class AuthorInfo(models.Model):
    isbn = models.OneToOneField('BookInfo', models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
    author = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Author_info'
        unique_together = (('isbn', 'author'),)


class BookInfo(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=13)  # Field name made lowercase.
    title = models.CharField(max_length=60)
    edition = models.CharField(max_length=20, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    publisher = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Book_info'


class Classes(models.Model):
    professor = models.CharField(primary_key=True, max_length=50)
    course_name = models.CharField(max_length=100, blank=True, null=True)
    course_id = models.CharField(max_length=9)
    section_id = models.CharField(max_length=3, blank=True, null=True)
    have_book = models.IntegerField(blank=True, null=True)
    isbn = models.ForeignKey(BookInfo, models.DO_NOTHING, db_column='ISBN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'
        unique_together = (('professor', 'course_id'),)



class LibraryInfo(models.Model):
    isbn = models.OneToOneField(BookInfo, models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
    exist = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Library_Info'


class UsedbookComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    usedbook = models.ForeignKey('UsedBookInfo', models.DO_NOTHING, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UsedBook_Comment'


class UsedBookInfo(models.Model):
    usedbook_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isbn = models.ForeignKey(BookInfo, models.DO_NOTHING, db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    quality = models.IntegerField()
    semester = models.CharField(max_length=4, blank=True, null=True)
    is_sold = models.IntegerField()
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Used_Book_Info'


class UserInfo(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=150, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    total_sells = models.IntegerField(blank=True, null=True)
    complain_numbers = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User_Info'

# class Complaints(models.Model):
#     complain_id = models.AutoField(primary_key=True)
#     complaintee = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='complaintee', blank=True, null=True)
#     complainer = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='complainer', blank=True, null=True)
#     complain_text = models.TextField(blank=True, null=True)
#     date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Complaints'


# class Coursebookrelation(models.Model):
#     littleused = models.IntegerField(db_column='littleUsed', blank=True, null=True)  # Field name made lowercase.
#     used = models.IntegerField(db_column='Used', blank=True, null=True)  # Field name made lowercase.
#     oftenused = models.IntegerField(db_column='oftenUsed', blank=True, null=True)  # Field name made lowercase.
#     semester = models.CharField(primary_key=True, max_length=4)
#     isbn = models.ForeignKey(BookInfo, models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
#     course = models.ForeignKey(Classes, models.DO_NOTHING)
#     professor = models.ForeignKey(Classes, models.DO_NOTHING, db_column='professor')

#     class Meta:
#         managed = False
#         db_table = 'CourseBookRelation'
#         unique_together = (('semester', 'professor', 'course', 'isbn'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
# Create your models here.
