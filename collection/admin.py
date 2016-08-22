from django.contrib import admin

# import your model
from collection.models import Thing

#register it

class ThingAdmin(admin.ModelAdmin):
	model=Thing
	list_display =('name','description',)
	prepopulated_fields ={'slug':('name',)
			}
admin.site.register(Thing, ThingAdmin)
