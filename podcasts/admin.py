from django.contrib import admin
from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("title","pub_date","episode_name")


    
# Register your models here.
