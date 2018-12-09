from django.contrib import admin
from myapp.models import Post, Vote, Comment
# from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'text')
    #prepopulated_fields = {'slug': ('id',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Vote)
admin.site.register(Comment)


