# faqs/admin.py
from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_hi', 'question_bn')  # Displaying questions in different languages in the list view

admin.site.register(FAQ, FAQAdmin)
