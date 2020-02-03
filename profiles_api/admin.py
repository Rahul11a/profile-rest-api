from django.contrib import admin
# Because of this registration  the PROFILES_API came up in the browser
from profiles_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
