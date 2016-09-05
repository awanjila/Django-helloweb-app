from django.contrib import admin

# import your model
from collection.models import Thing
from collection.models import Social

#register it

class ThingAdmin(admin.ModelAdmin):
	model=Thing
	list_display =('name','description',)
	prepopulated_fields ={'slug':('name',)
			}
admin.site.register(Thing, ThingAdmin)

class SocialAdmin(admin.ModelAdmin):
	model=Social
	list_display=('network','username',)
admin.site.register(Social, SocialAdmin)