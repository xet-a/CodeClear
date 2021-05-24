from django.db import models
from django.contrib.auth.models import User
#from django.db.models import F, Sum, Count, Case, When


# 옷장
class Closet(models.Model):

    COLOR = (
        ('Red','Red'), ('Pink','Pink'), ('Orange','Orange'), ('Yellow','Yellow'),
        ('Green','Green'), ('Blue','Blue'), ('Purple', 'Purple')
    )

    CATEGORY_CHOICES = (('상의','top'), ('반팔','short_shirt'), ('긴팔','long_shirt'),
                        ('민소매','sleeveless_shirt'), ('하의','bottom'), ('바지','pants'), 
                        ('치마','skirt'), ('원피스','dress')
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    clothes_num = models.AutoField()

    clothes_name = models.CharField('이름', max_length=20, unique=True)

    clothes_category = models.CharField(max_length=10, blank=True, choices=CATEGORY_CHOICES)

    clothes_color = models.CharField(max_length=10, blank=True, choices=COLOR)

    clothes_image = models.ImageField()

    put_date = models.DateField(auto_now_add=True)

    #사용 횟수(수정)
    #use_num = models.IntegerField(auto_created=0)

    #옷의 총 갯수(수정)
    #total_clothes_num = Model.objects.aggregate(total_clothes_num=Max('user_id'))



#카테고리
'''
class Category(models.Model):

    top = models.ImageField(help_text='상의')

    short_sleeved_shirt = models.ImageField(help_text='반팔')

    long_sleeved_shirt = models.ImageField(help_text='긴팔')

    sleeveless_shirt = models.ImageField(help_text='민소매')


    bottom = models.ImageField(help_text='하의')

    pants = models.ImageField(help_text='바지')

    skirt = models.ImageField(help_text='치마')


    dress = models.ImageField(help_text='원피스')
'''