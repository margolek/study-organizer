from django.contrib import admin
from .models import Group, GroupMember, GroupRequest

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupRequest)


