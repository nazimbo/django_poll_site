from django.contrib import admin
from .models import Question

# Register your models here.

# The following code registers the Question model with the admin site.
admin.site.register(Question)
