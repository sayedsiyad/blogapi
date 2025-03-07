from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Post(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")

    image=models.ImageField(upload_to="post_images",null=True)

    created_at=models.DateTimeField(auto_now_add=True)

    liked_by=models.ManyToManyField(User)

    def __str__(self):
        return self.title
    

class Comment(models.Model):

    post_object=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    message=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.message






