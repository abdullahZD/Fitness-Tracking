from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model




#User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    


#Profile Model
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"   
    


#Workout Model
class Workout(models.Model):
    INTENSITY_LEVEL_CHOICES = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
        ('Intense', 'Intense'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()  # in minutes
    intensity_level = models.CharField(max_length=20, choices=INTENSITY_LEVEL_CHOICES)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}'s Workout on {self.date_time}"




#Fitness Goal Model
class FitnessGoal(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=255)
    target_value = models.FloatField()
    target_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s {self.goal_type} Goal"



#Notification Model
class Notification(models.Model):
    sender = models.ForeignKey(get_user_model(), related_name='sent_notifications', on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), related_name='received_notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification from {self.sender.username} to {self.receiver.username}"