from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=48)
    text = models.TextField()
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return f"This is a post titled {self.title} from {self.pub_date} with {self.score} score"
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Comment to a post #{self.post.id} with {self.score} score"