from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from collection.models import Post, Comment, Vote
from django.db.models import Count
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from random import randint
import datetime 

class Command(BaseCommand):
    def handle(self, *args, **options):
        # now do the things that you want with your models here
        password="Quizzles(11)"
        exp_posts=50
        exp_users=20
        avg_votes_per_post=5
        avg_comments_per_post=3

        # Post.objects.all().delete()

        rootExists=User.objects.filter(username="root").count()
        if(rootExists < 1):
            self.stdout.write("Creating root user")
            User.objects.create_superuser("root", "root@test.com", password)

        num_posts=Post.objects.all().count()
        num_users=User.objects.all().count()
        num_votes=Vote.objects.all().count()
        num_comments=Comment.objects.all().count()

        faker = Faker()

        self.stdout.write("Default password: " + password)
        self.stdout.write("Number of posts: " + str(num_posts))
        self.stdout.write("Number of votes: " + str(num_votes))
        self.stdout.write("Number of comments: " + str(num_comments))
        self.stdout.write("Number of users: " + str(num_users))

        if(num_users < exp_users):
            self.stdout.write("Creating " + str(exp_users-num_users) + " Users")
            for x in range(num_users+1,exp_users+1):
                username=faker.name().replace(" ",".")
                email=username+"@test.com"
                User.objects.create_superuser(username, email, password)
                self.stdout.write("   " + username)
            num_users=User.objects.all().count()

        if(num_posts < exp_posts):
            self.stdout.write("Creating " + str(exp_posts-num_posts) + " Posts")
            for x in range(num_posts+1,exp_posts+1):
                day_offset=randint(1,364)
                pub_date=timezone.now()-datetime.timedelta(days=day_offset)
                u=self.randomUser()
                title=faker.text()
                self.stdout.write("   [" + u.username + "] "+title)
                rec=Post()
                rec.author=u
                rec.title=title
                rec.text=faker.text()                
                rec.created_date=pub_date
                rec.published_date=pub_date
                rec.save()
            num_posts=Post.objects.all().count()
        
        self.stdout.write("Voting...")
        while(num_votes < avg_votes_per_post*num_posts):
            user=self.randomUser()
            post=self.randomPost()
            voted=Vote.objects.all().filter(post=post, author=user).count()
            if(post.author!=user and voted==0):
                rec=Vote()
                rec.author=user
                rec.post=post 
                rec.created_date=self.randomDate(post.created_date,timezone.now())
                rec.save()
                num_votes=Vote.objects.all().count()
                self.stdout.write(str(num_votes) + ": " + user.username + " voted for [" + post.title +"]")

        self.stdout.write("Commenting...")
        while(num_comments < avg_comments_per_post*num_posts):
            user=self.randomUser()
            post=self.randomPost()
            rec=Comment()
            rec.author=user
            rec.post=post 
            rec.contents=faker.text()
            rec.created_date=self.randomDate(post.created_date,timezone.now())
            rec.save()
            num_comments=Comment.objects.all().count()
            self.stdout.write(str(num_comments) + ": " + user.username + " commented on [" + post.title +"]")

    def randomUser(self):
        count = User.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return User.objects.all()[random_index]

    def randomPost(self):
        count = Post.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return Post.objects.all()[random_index]

    def randomDate(self, start_date, end_date):
        maxdelta=end_date - start_date
        offset_days=randint(0,maxdelta.days)
        offset_secs=randint(0,60*60*24)
        return start_date + datetime.timedelta(days=offset_days) + datetime.timedelta(seconds=offset_secs)
