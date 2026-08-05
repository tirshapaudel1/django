from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.CharField(max_length=100, unique=True, blank=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug =self.title.lower().replace(' ','-')
            slug=base_slug
            counter =1
            while Post.objects.filter(slug=slug).exists():
                slug=f'{base_slug}-{counter}'
                counter +=1
            self.slug=slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title