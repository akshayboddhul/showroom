import sys
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO


class Product(models.Model):
    CATEGORY = (
        ('Towel', 'Towel'),
        ('Chaddar', 'Chaddar'),
        ('Bedsheet', 'Bedsheet'),
        ('Home Decor', 'Home Decor'),
        ('Kids', 'Kids'),
        ('Saree', 'Saree'),
        ('Dress Material', 'Dress Material'),
        ('Other', 'Other')
    )
    MATERIAL = (
        ('Cotton', 'Cotton'),
        ('Turkish', 'Turkish'),
        ('Polyster', 'Polyster'),
        ('Mix', 'Mix'),
        ('Other', 'Other')
    )
    title = models.CharField(max_length=200, blank=False)
    size = models.CharField(max_length=255)
    material = models.CharField(
        max_length=255, choices=MATERIAL, null=True, blank=True)
    category = models.CharField(max_length=255, choices=CATEGORY)
    main_photo = models.ImageField(
        upload_to='photos/', blank=True, default="b&b-logo.jpg")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        kwargs['force_insert'] = True
        im = Image.open(self.main_photo)
        output = BytesIO()
        im = im.resize((300, 300))
        im.save(output, format='jpeg', quality=80)
        output.seek(0)
        self.main_photo = InMemoryUploadedFile(output, 'ImageField', "%s.jpeg" % (str(self.title) + '_' + self.category).split(
            '.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Product, self).save()
