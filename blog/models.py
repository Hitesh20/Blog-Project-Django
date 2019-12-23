from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Each class is going to be a seprate table in the database
class Post(models.Model):
    title = models.CharField(max_length=100)                      #title is attribute and charfield is field
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)      #1st argument is table name and 2nd argument is to tell that
                                                                    # is user gets deleted then post will also be deleted



    def __str__(self):                                            #Just like toString method in java
        return {self.title}

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        #return reverse('blog-home')
    '''
    def save(self, *args, **kwargs):                                #overriding this method... already exists at back end...
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''