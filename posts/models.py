from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()


    def __str__(self):
        # return post.title for admin.lists
        return self.title

    def summary(self):
        return self.body[:45]  #pickup first 100 charactor


class MenuMaster(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # return post.title for admin.lists
        return self.name


class MenuDetail(models.Model):
    name = models.ForeignKey(MenuMaster, on_delete=models.CASCADE)
    nailist = models.CharField(max_length=30)
    money = models.IntegerField(default=0)

    def __str__(self):
        # return post.title for admin.lists
        return self.nailist
