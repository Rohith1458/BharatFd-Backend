# faqs/models.py
from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    # Basic fields for question and answer
    question = models.TextField()
    answer = RichTextField(blank=True,null=True)

    # Language-specific translations for the question
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translated_question(self, lang='en'):
        """
        Retrieve the translated question based on the language.
        Fallback to the default (English) if translation is not available.
        """
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        
        # If the translation exists for the requested language, return it
        return translations.get(lang, self.question)  # Default to English if translation is not found

    def __str__(self):
        return self.question
