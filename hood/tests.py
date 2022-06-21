from django.test import TestCase
from .models import Profile,Neighbourhood,Post,Business
from django.contrib.auth.models import User
from hood.views import profile
import datetime

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Hood", hood_location= "Mombasa", admin = self.user,hood_description='area', hood_photo="hood.jpg")
        self.neighbourhood.save()
        self.profile = Profile(id=4,idNo=39607876,email='Hood@g.com', profile_pic='profile.jpg', bio='Hood profile',neighbourhood=self.neighbourhood,
                                    user=self.user)
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class NeighbourhoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Hood", hood_location= "Mombasa", admin = self.user,hood_description='area', hood_photo="hood.jpg")
        self.neighbourhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_hood(self):
        self.neighbourhood.save_hood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_hood(self):
        self.neighbourhood.delete_hood()
        testsaved = Neighbourhood.objects.all()
        self.assertFalse(len(testsaved) > 0)

class PostTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Hood", hood_location= "Mombasa", admin = self.user,hood_description='area', hood_photo="hood.jpg")
        self.neighbourhood.save()
        self.post = Post(user=self.user,title="hotel sarova",image="post.jpg" ,content ="my post", timestamp=datetime.datetime,neighbourhood=self.neighbourhood)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.objects.all()
        self.assertFalse(len(post) > 0)

class BusinessTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.neighbourhood =  Neighbourhood(hood_name = "Hood", hood_location= "Mombasa", admin = self.user,hood_description='area', hood_photo="hood.jpg")
        self.neighbourhood.save()
        self.biz = Business(user=self.user,business_name="hotel sarova", business_hood=self.neighbourhood,business_email="hotelsarova@gmail.com", business_desc="hotel management")
        self.biz.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.biz,Business))

    def test_save_business(self):
        self.biz.save_business()
        biz = Business.objects.all()
        self.assertTrue(len(biz) > 0)

    def test_delete_hood(self):
        self.biz.delete_business()
        biz = Business.objects.all()
        self.assertFalse(len(biz) > 0)