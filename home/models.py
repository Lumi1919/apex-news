from django.db import models




class Post(models.Model):
    intro = models.CharField(max_length=255, null=True, blank=True)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    author_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


article_choice = {
    ('breaking', 'breaking'),
    ('actualite', 'actualite'),
    ('societe', 'societe'),
    ('culture', 'culture'),
    ('sport', 'sport'),
    ('politique', 'politique'),
    ('international', 'international'),
    ('spiritualite', 'spiritualite'),
    ('evenement', 'evenement'),
    ('activite', 'activite'),
    ('event', 'event'),
    ('video', 'video'),
    ('homme_de_la_semaine', 'homme_de_la_semaine'),
    ('business', 'business'),
    ('pub', 'pub'),

}
class Articles(models.Model):
    article_categorie = models.CharField(max_length=250, blank=True, null=True, choices=article_choice)
    intro = models.CharField(max_length=255, null=True, blank=True)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    videoLink = models.CharField(max_length=255, null=True, blank=True)
    post_views = models.IntegerField(null=True, blank=True, default=0)
    comments_num = models.IntegerField(null=True, blank=True, default=0)
    

    def __str__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()
    author = models.CharField(max_length=255)
    author_image = models.ImageField()

    def __str__(self):
        return self.title


class Homme_de_la_semaine(models.Model):
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    author_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment_Article(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ("publish",)
        
    def __str__(self):
        return '%s - %s' % (self.article.title, self.name) 
    

video_categorie_choice = {
    ('sport', 'sport'),
    ('societe', 'societe'),
    ('culture', 'culture'),
    ('activite', 'activite'),
}

class A_voir(models.Model):
    categorie = models.CharField(max_length=255, choices=video_categorie_choice)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    videoLink = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class Partenaires(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
