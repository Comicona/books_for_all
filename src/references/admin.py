from django.contrib import admin
from references import models

class ReferencesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name','description']

admin.site.register(models.Author, ReferencesAdmin)
admin.site.register(models.Series, ReferencesAdmin)
admin.site.register(models.Genre, ReferencesAdmin)
admin.site.register(models.Publisher, ReferencesAdmin)
admin.site.register(models.Category, ReferencesAdmin)
admin.site.register(models.Format, ReferencesAdmin)
