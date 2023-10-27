from django.contrib import admin
from .models import Post
from .models import Articles
from .models import A_voir
from .models import Episode
from .models import Album
from .models import Homme_de_la_semaine
from .models import Partenaires
from .models import Comment_Article


admin.site.register(Post)
admin.site.register(Articles)
admin.site.register(A_voir)
admin.site.register(Homme_de_la_semaine)
admin.site.register(Episode)
admin.site.register(Album)
admin.site.register(Partenaires)
admin.site.register(Comment_Article)


