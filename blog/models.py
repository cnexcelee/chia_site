from django.db import models
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
	
	title = models.CharField(max_length = 150)

	body = models.TextField()

	timestamp = models.DateTimeField()

class BlogsPostAdmin(admin.ModelAdmin):
	"""docstring for BlogsPostAdmin"""
	list_display = ('title','timestamp')
		

admin.site.register(BlogsPost,BlogsPostAdmin)

