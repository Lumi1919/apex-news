from django.contrib import admin
from .models import Post
from .models import Crew
from .models import Episode
from .models import Comment
from .models import GameComment



admin.site.register(Post)
admin.site.register(Crew)
admin.site.register(Episode)
admin.site.register(Comment)
admin.site.register(GameComment)


