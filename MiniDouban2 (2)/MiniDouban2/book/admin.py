from django.contrib import admin
from .models import Book, ReviewBook
# Register your models here.
# admin.site.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title','description')
#     search_fields = ['title', 'description']
#     list_editable = ('description',)
# admin.site.register(Book,BookAdmin)
admin.site.register(Book)
admin.site.register(ReviewBook)