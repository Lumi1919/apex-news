from django.contrib import admin
from .models import Post
from .models import Articles
from .models import People
from .models import A_voir
from .models import Breaking
from .models import Evenements_Jour
from .models import Event
from .models import Episode
from .models import Comment
from .models import Activite
from .models import Album
from .models import Actu
from .models import Homme_de_la_semaine
from .models import Partenaires
from .models import Comment_Article


admin.site.register(Post)
admin.site.register(Articles)
admin.site.register(Evenements_Jour)
admin.site.register(Activite)
admin.site.register(People)
admin.site.register(A_voir)
admin.site.register(Breaking)
admin.site.register(Event)
admin.site.register(Homme_de_la_semaine)
admin.site.register(Episode)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Actu)
admin.site.register(Partenaires)
admin.site.register(Comment_Article)


