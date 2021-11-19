from django.contrib import admin
from .models import movie, cast, review, IdNumber

class MovieAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    search_fields = ('name',)
    list_display = ('name', 'likes', 'watch_count', 'show_rate')
    readonly_fields = ('show_rate', )

    def show_rate(self, obj):
        if obj.watch_count:
            return '{} %'.format(100 * (obj.likes / obj.watch_count))
        return 0
    show_rate.short_description = 'Rate'

    fieldsets = (
        ['main', {'fields':['name', 'description']}],
        ['stat', {'fields':['likes', 'watch_count', 'show_rate']}],
        ['actors', {'fields' :['actors']}]
    )

# Register your models here.
admin.site.register(movie, MovieAdmin)
admin.site.register(cast)
admin.site.register(review)
admin.site.register(IdNumber)