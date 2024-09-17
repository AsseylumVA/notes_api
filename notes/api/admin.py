from django.contrib import admin

from .models import Note


class NoteResource(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteResource)
