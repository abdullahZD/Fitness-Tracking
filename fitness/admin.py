from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Workout, FitnessGoal, Notification, Profile



# Custom admin class for Workout model
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise_type', 'duration', 'intensity_level', 'date_time')
    list_filter = ('user', 'intensity_level', 'date_time')
    search_fields = ('user__username', 'exercise_type')
    date_hierarchy = 'date_time'
    ordering = ('-date_time',)


# Register the CustomUser model with its default admin class
admin.site.register(CustomUser, UserAdmin)


# Register other models with custom or default admin classes
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(FitnessGoal)
admin.site.register(Notification)
admin.site.register(Profile)
