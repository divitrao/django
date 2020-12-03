from django.db import models

# Create your models here.
class news_for_admin(models.Model):

    image = models.ImageField(upload_to='image')
    content_of_news = models.TextField()
    news_about = models.TextField()
    link = models.CharField(max_length=100)
    site_name = models.CharField(max_length=30)
