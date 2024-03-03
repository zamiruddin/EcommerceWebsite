from django.db import models

from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:

        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])
    
class Product(models.Model):

    #FK

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris libero purus, convallis id ligula et, aliquam imperdiet magna. Donec nec dignissim urna. Sed laoreet quis ligula vitae convallis. Donec vel lobortis dui. Etiam leo nunc, consequat a cursus vitae, dapibus pretium nulla. Phasellus tristique nibh quis auctor blandit. Donec in pharetra sem. In efficitur ipsum in metus porta egestas. Nam enim lectus, efficitur vel nisi et, sodales commodo nisi. Nulla cursus gravida ipsum. Aenean pretium in nisl at congue.')

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    image = models.ImageField(upload_to='images/')

    class Meta:

        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])




