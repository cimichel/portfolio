from django.contrib import admin
from memetrivia.models import MemeTrivia


class MemeTriviaAdmin(admin.ModelAdmin):
    pass


admin.site.register(MemeTrivia, MemeTriviaAdmin)
