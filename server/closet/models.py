from django.db import models
'''
class Closet(models.Model):

    COLOR = (
        ('Red','Red'), ('Pink','Pink'), ('Orange','Orange'), ('Yellow','Yellow'),
        ('Green','Green'), ('Blue','Blue'), ('Purple', 'Purple'), ('Black','Black'),
        ('Grey','Grey')
    )

    CATEGORY_CHOICES = (('상의','top'), ('반팔','short_shirt'), ('긴팔','long_shirt'),
                        ('민소매','sleeveless_shirt'), ('하의','bottom'), ('바지','pants'), 
                        ('치마','skirt'), ('원피스','dress')
    )

    user_id = models.CharField(max_length=10, blank=True)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    clothes_name = models.CharField('옷 이름', max_length=20, unique=True)

    clothes_category = models.CharField(max_length=10, blank=True, choices=CATEGORY_CHOICES)

    clothes_color = models.CharField(max_length=10, blank=True, choices=COLOR)

    clothes_image = models.ImageField()

    put_date = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.clothes_name
'''