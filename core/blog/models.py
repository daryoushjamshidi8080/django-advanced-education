from django.db import models


# class post
class Post(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title


# class category
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:

        return f" category : '{self.name}'"
