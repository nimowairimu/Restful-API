# from django.test import TestCase
# from .models import Profile,Projects
# from django.contrib.auth.models import User


# class ProfileTest(TestCase):
#     def setUp(self):
#         self.nimo = User(username = 'nims',email = 'nimo@gmail.com')
#         self.nimo = Profile(user = Self.nimo,user = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='April,04.2021')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.nimo,Profile))

#     def test_save_profile(self):
#         Profile.save_profile(self)
#         all_profiles = Profile.objects.all()
#         self.assertTrue(len(all_profiles),0)

#     def test_delete_profile(self):
#         self.nimo.delete_profile()
#         all_profiles = Profile.objects.all()
#         self.assertEqual(len(all_profiles),0)

# class ProjectsTestCase(TestCase):
#     def setUp(self):
#         self.new_post = Projects(title = 'projectx',projectscreenshot = 'test.jpg',description = 'testD',user = 'nimo',projecturl = 'https://test.com',datecreated='April,04.2021')


#     def test_save_project(self):
#         self.new_post.save_project()
    #     pictures = Image.objects.all()
    #     self.assertEqual(len(pictures),1)

    # def test_delete_project(self):
    #     self.new_post.delete_project()
    #     pictures = Projects.objects.all()
    #     self.assertEqual(len(pictures),1)

