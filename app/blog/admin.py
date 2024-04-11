from django.contrib import admin
from .models import Post

# Register your models here.
# Post table will now be visible in the admin gui
admin.site.register(Post)
