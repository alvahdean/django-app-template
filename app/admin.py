from django.contrib import admin
from collection.models import Post
from collection.models import Comment
from collection.models import Vote
# from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'text')
    #prepopulated_fields = {'slug': ('id',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Vote)
admin.site.register(Comment)


