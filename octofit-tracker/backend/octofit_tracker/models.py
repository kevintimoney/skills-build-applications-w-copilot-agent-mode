from djongo import models
from django.contrib.auth.models import AbstractUser



class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=50)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, to_field='id', db_column='team_id', on_delete=models.SET_NULL, null=True, blank=True)


class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    user = models.ForeignKey(User, to_field='id', db_column='user_id', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()


class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    user = models.ForeignKey(User, to_field='id', db_column='user_id', on_delete=models.CASCADE)
    score = models.IntegerField()
