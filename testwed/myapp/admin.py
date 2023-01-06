from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')#讓文章在顯示的時候除了title之外，還可以有張貼的日期和時間

admin.site.register(Post,PostAdmin)