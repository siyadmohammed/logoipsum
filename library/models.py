from django.db import models

# Create your models here.
class author1(models.Model):
    SERIAL_N0= models.AutoField(primary_key=True)
    AUTHOR_NAME = models.CharField(max_length=20, null=True)
    USER_NAME= models.CharField(max_length=20, null=True)
    EMAIL= models.EmailField(null=True)



class book1(models.Model):
    BOOK_NAME = models.CharField(max_length=20, null=True)
    AUTHOR_NAME= models.CharField(max_length=20, null=True)
    BOOK_ID = models.AutoField(primary_key=True, unique=True)
    CREATED_AT = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.CREATED_AT)

