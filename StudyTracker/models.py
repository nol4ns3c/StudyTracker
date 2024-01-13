from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CorrectAnswersReading(models.Model):
    Cambridge =models.CharField(max_length=20, null=True)
    Test=models.CharField(max_length=5, null=True)
    Correct = models.IntegerField
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
 

    
class CorrectAnswersListening(models.Model):
    Cambridge =models.CharField
    Test=models.CharField
    Correct = models.IntegerField
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
 



class Answer(models.Model):
    Type = models.CharField(max_length=20, choices=[("l","Listening"), ("r","Reading")])
    Cambridge =models.CharField(max_length=20, choices=[("Cambridge 1","Cambridge 1"),("Cambridge 2","Cambridge 2"),("Cambridge 3","Cambridge 3"),("Cambridge 4","Cambridge 4"),("Cambridge 5","Cambridge 5"),("Cambridge 6","Cambridge 6"),("Cambridge 7","Cambridge 7"),("Cambridge 8","Cambridge 8"),("Cambridge 9","Cambridge 9"),("Cambridge 10","Cambridge 10"),("Cambridge 11","Cambridge 11"),("Cambridge 12","Cambridge 12"),("Cambridge 13","Cambridge 13"),("Cambridge 14","Cambridge 14"),("Cambridge 15","Cambridge 15"),("Cambridge 16","Cambridge 16"),("Cambridge 17","Cambridge 17"),("Cambridge 18","Cambridge 18")])
    Test=models.CharField(max_length=20, choices=[("Test 1","Test 1"), ("Test 2","Test 2"), ("Test 3","Test 3"), ("Test 4","Test 4")])
    CorrectAnswers = models.TextField(max_length=700, null=True)
    models.ForeignKey(CorrectAnswers, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.Type + self.Cambridge + self.Test
    

class UserAccountManager(BaseUserManager): 
    def create_user(self, email, username, password):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email