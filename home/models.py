from django.db import models


class Post(models.Model):
    intro = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField()
    image2 = models.ImageField()
    author = models.CharField(max_length=255)
    author_image = models.ImageField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return f"Comment by {self.name}"


class Crew(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    country = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Episode(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Game_comment(models.Model):
    pronostic = models.CharField(max_length=255)

    def __str__(self):
        return self.pronostic