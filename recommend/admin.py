from django.contrib import admin
from recommend.models import RecommendModel

# Register your models here.

admin.site.register(RecommendModel)

admin.site.site_header = "DELL SERVER BACKEND PANEL"


class RecommendModelAdmin(admin.ModelAdmin):
    list_display = ['user_id']
