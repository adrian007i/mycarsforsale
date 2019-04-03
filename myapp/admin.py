from django.contrib import admin
from myapp.models import UserInfo,CarInfo,BlogTopics,Comments
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(CarInfo)
admin.site.register(BlogTopics)
admin.site.register(Comments)
