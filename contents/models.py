from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.conf import settings
from users.models import User

# Create your models h
# 
# ere.

class TaggedFeed(TaggedItemBase):
    content_object = models.ForeignKey('Feed', on_delete=models.CASCADE)
    
class Feed(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()    # 글내용
    image = models.ImageField()  # 피드 이미지
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    
    
    ### 태그 추가 부분###
    tags = TaggableManager(through=TaggedFeed, blank=True)

    def __str__(self):
        return str(self.title)

class Comment(models.Model):

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'comment' )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Comment')
