from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

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


    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100, default = "1")
    transmission = models.CharField(max_length=100, default = "1")
    interior = models.CharField(max_length=100, default = "1")
    miles = models.IntegerField(default = "1")
    doors = models.CharField(choices=door_choices, max_length=10, default = "1")
    passengers = models.IntegerField(default = "1")
    vin_no = models.CharField(max_length=100,default = "1")
    milage = models.IntegerField(default = "1")
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
