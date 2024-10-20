from django.contrib import admin

from myApp.models import *


admin.site.register(customUser)
admin.site.register(viewersProfileModel) 
admin.site.register(creatorProfileModel) 
admin.site.register(RecipeModel) 