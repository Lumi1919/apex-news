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

class Articles(models.Model):
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
    author_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Evenements_Jour(models.Model):
    categorie = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

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



class Actu(models.Model):
    title = models.CharField(max_length=255)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3= models.ImageField(null=True, blank=True)
    video = models.FileField(upload_to='static', null=True, blank=True)
    author = models.CharField(max_length=255)
    author_image = models.ImageField()

    def __str__(self):
        return self.title


class Societe(models.Model):
    title = models.CharField(max_length=255)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Culture(models.Model):
    title = models.CharField(max_length=255)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class People(models.Model):
    title = models.CharField(max_length=255)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class International(models.Model):
    title = models.CharField(max_length=255)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Comment_Actu(models.Model):
    actu = models.ForeignKey(Actu, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

id_choice = {
    ('sorties', 'sorties'),
    ('spectacles', 'spactacles'),
    ('visites', 'visites'),
    ('coup de coeur', 'coup de coeur'),

}

class Activite(models.Model):
    i_d = models.CharField(max_length=250, blank=True, null=True, choices=id_choice)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Politique(models.Model):
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Event(models.Model):
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True) 
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


sport_choice = {
    ('basket', 'basket'),
    ('foot', 'foot'),
    ('lamb', 'lamb'),
    ('tennis', 'tennis'),
    ('autres', 'autres'),

}

class Sport(models.Model):
    i_d = models.CharField(max_length=250, blank=True, null=True, choices=sport_choice)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

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


class Breaking(models.Model):
    categorie = models.CharField(max_length=255)
    legende = models.CharField(max_length=255, null=True, blank=True)
    legende2 = models.CharField(max_length=255, null=True, blank=True)
    legende3 = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    body1 = models.TextField(null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Partenaires(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

