from django.contrib import admin
from .models import Content,Comments,Super,Like,Dislike

admin.site.register(Content)
admin.site.register(Comments)
admin.site.register(Super)
admin.site.register(Like)
admin.site.register(Dislike)

