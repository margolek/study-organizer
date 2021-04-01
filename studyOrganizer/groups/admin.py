from django.contrib import admin
from .models import Group, GroupContent, GroupComments

admin.site.register(Group)
admin.site.register(GroupContent)
admin.site.register(GroupComments)

