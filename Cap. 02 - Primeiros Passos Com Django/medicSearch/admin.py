from django.contrib import admin
from .models import *
# Register your models here.

# Adds attr responsible for the apperance and behavior of the admin panel
class ProfileAdmin(admin.ModelAdmin):
    # Create a hierarquical filtering in the model Profile by creation date 
    date_hierarchy = 'created_at' 
    
    # Select which attributes will be displayed
    list_display = ('user', 'user__is_active', 'role', 'birth', 'specialitiesList', 'addressesList')
    
    # Enable edition link for the following attributes 
    lsit_display_links = ('user', 'role',)
    class Media:
        css = {
            'all': ('css/custom.css',),
        }
        js = ('js/custom.js',)
    # Cutomizes the representation of empty field
    empty_value_display = 'Vazio'

    # Creates a filter in the data based on the following attributes
    list_filter = ('user__is_active',)

    # Determines which field will be displayed in the form
    # fields = ('user', ('role',), 'image', 'birthday', 'specialities', 'addresses',)

    # It is the opposite from fields, therefore removing the fields included in the tuple
    exclude = ('favorites', 'created_at', 'updated_at')

    # Makes the field read-only in the creation and update form
    #readonly_fields = ('user',)

    # Enables the search by field in the admin profile list
    search_fields = ('user__username',)

    # Is similar to fields, however it is possible to group the fields to organize the data flow
    fieldsets = (
        ('Usuário',{
            'fields': ('user', 'birthday', 'image'),
        }),
        ('Função', {
            'fields': ('role',),
        }),
        ('Extras', {
            'fields': ('specialities', 'addresses'),
        }),
    )

    # Custom the display of a field
    def birth(self, obj:Profile):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
        
    birth.empty_value_display = '__/__/____'

    # Modeling ManyToMany relationships
    def specialitiesList(self, obj:Profile):
        return [sp.name for sp in obj.specialities.all()]
    def addressesList(self, obj:Profile):
        return [ad.name for ad in obj.addresses.all()]
    
    addressesList.empty_value_display = ''
    
# Note the argument ProfileAdmin bellow, is mandatory to include it in the register of the Profile model
admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)