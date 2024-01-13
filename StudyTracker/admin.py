from django.contrib import admin
from .models import CorrectAnswersReading
from .models import CorrectAnswersListening
from .models import Answer



admin.site.register(CorrectAnswersReading)
admin.site.register(CorrectAnswersListening)
admin.site.register(Answer)

# Register your models here.
