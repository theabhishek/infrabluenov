from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Tile(models.Model):

    state_choice = (
    ("AN","Andaman and Nicobar Islands"),
    ("AP","Andhra Pradesh"),
    ("AR","Arunachal Pradesh"),
    ("AS","Assam"),
    ("BR","Bihar"),
    ("CG","Chandigarh"),
    ("CH","Chhattisgarh"),
    ("DN","Dadra and Nagar Haveli"),
    ("DD","Daman and Diu"),
    ("DL","Delhi"),
    ("GA","Goa"),
    ("GJ","Gujarat"),
    ("HR","Haryana"),
    ("HP","Himachal Pradesh"),
    ("JK","Jammu and Kashmir"),
    ("JH","Jharkhand"),
    ("KA","Karnataka"),
    ("KL","Kerala"),
    ("LA","Ladakh"),
    ("LD","Lakshadweep"),
    ("MP","Madhya Pradesh"),
    ("MH","Maharashtra"),
    ("MN","Manipur"),
    ("ML","Meghalaya"),
    ("MZ","Mizoram"),
    ("NL","Nagaland"),
    ("OR","Odisha"),
    ("PY","Puducherry"),
    ("PB","Punjab"),
    ("RJ","Rajasthan"),
    ("SK","Sikkim"),
    ("TN","Tamil Nadu"),
    ("TS","Telangana"),
    ("TR","Tripura"),
    ("UP","Uttar Pradesh"),
    ("UK","Uttarakhand"),
    ("WB","West Bengal"),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))


   
    tile_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100,blank=True)
    description = RichTextField(blank=True)
    tile_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    tile_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    tile_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    tile_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    tile_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    thickness = models.CharField(max_length=100,blank=True)
    body_style = models.CharField(max_length=100)
    surface = models.CharField(max_length=100,blank=True)
    usage = models.CharField(max_length=100,blank=True)
    interior = models.CharField(max_length=100,blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.tile_title

# Create your models here.

