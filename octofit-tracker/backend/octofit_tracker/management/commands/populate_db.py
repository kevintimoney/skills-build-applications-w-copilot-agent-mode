from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        User = get_user_model()
        # Clear existing data in safe order

        # Drop collections directly to avoid Djongo PK issues
        from django.db import connection
        db = connection.cursor().db_conn
        db.drop_collection('octofit_tracker_team')
        db.drop_collection('octofit_tracker_user')
        db.drop_collection('octofit_tracker_activity')
        db.drop_collection('octofit_tracker_workout')
        db.drop_collection('octofit_tracker_leaderboard')


        # Create Teams with string IDs

        marvel = Team.objects.create(id='marvel', name='Team Marvel')
        dc = Team.objects.create(id='dc', name='Team DC')

        # Create Users with string IDs
        users = [
            User(id='ironman', email='ironman@marvel.com', username='ironman', team=marvel),
            User(id='captain', email='captain@marvel.com', username='captain', team=marvel),
            User(id='batman', email='batman@dc.com', username='batman', team=dc),
            User(id='superman', email='superman@dc.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password')
            user.save()

        # Create Activities with string IDs
        Activity.objects.create(id='a1', user=users[0], type='run', duration=30)
        Activity.objects.create(id='a2', user=users[1], type='cycle', duration=45)
        Activity.objects.create(id='a3', user=users[2], type='swim', duration=60)
        Activity.objects.create(id='a4', user=users[3], type='yoga', duration=20)

        # Create Workouts with string IDs
        Workout.objects.create(id='w1', name='Morning Cardio', description='Cardio for all')
        Workout.objects.create(id='w2', name='Strength Training', description='Strength for all')

        # Create Leaderboard with string IDs
        Leaderboard.objects.create(id='l1', user=users[0], score=100)
        Leaderboard.objects.create(id='l2', user=users[1], score=90)
        Leaderboard.objects.create(id='l3', user=users[2], score=95)
        Leaderboard.objects.create(id='l4', user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (should be in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100)
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
# class Leaderboard(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.IntegerField()
