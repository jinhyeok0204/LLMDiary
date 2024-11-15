from django.db import models
from accounts.models import Person, User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_publisher = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='posts')
    post_write_date = models.DateField(auto_now_add=True)
    post_content = models.TextField()

    def __str__(self):
        return f"Post by {self.post_publisher.name} on {self.post_write_date}"


class PostComment(models.Model):
    post_comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_comment_write_date = models.DateField(auto_now_add=True)
    post_comment_contetnt = models.TextField

    def __str__(self):
        return f"Comment by {self.user.id.name} on {self.post_comment_write_date}"