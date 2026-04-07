from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class APISmokeTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(id='marvel', name='Team Marvel')
        self.user = User.objects.create(id='ironman', username='ironman', email='ironman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(id='w1', name='Morning Cardio', description='Cardio for all')
        self.activity = Activity.objects.create(id='a1', user=self.user, type='run', duration=30)
        self.leaderboard = Leaderboard.objects.create(id='l1', user=self.user, score=100)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('teams', response.data)

    def test_teams(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)

    def test_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_activities(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, 200)

    def test_workouts(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
