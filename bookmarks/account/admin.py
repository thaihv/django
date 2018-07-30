from django.contrib import admin
from .models import Profile
from .forms import ProfileEditForm

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #form = ProfileEditForm
    list_display = ['user', 'date_of_birth', 'gender','photo']