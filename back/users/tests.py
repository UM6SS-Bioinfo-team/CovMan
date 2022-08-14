from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTest(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'test@covman.ma',
            'user_name',
            'first_name',
            'last_name',
            'local',
            'password'
        )
        self.assertEqual(super_user.email, 'test@covman.ma')
        self.assertEqual(super_user.user_name, 'user_name')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertEqual(super_user.last_name, 'last_name')
        self.assertEqual(super_user.institut, 'local')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user),'user_name')
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', first_name='first_name', password='password', is_superuser=False, institut='local',last_name='last_name')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', first_name='first_name', password='password', is_staff=False,institut='local',last_name='last_name')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', user_name='username1', first_name='first_name', password='password', is_superuser=True,institut='local',last_name='last_name')
    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            email = 'test@covman.ma',
            user_name = 'user_name',
            first_name = 'first_name',
            last_name = 'last_name',
            password = 'password',
            institut = 'local'
        )
        self.assertEqual(user.email, 'test@covman.ma')
        self.assertEqual(user.user_name, 'user_name')
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.last_name, 'last_name')
        self.assertEqual(user.institut, 'local')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertEqual(str(user),'user_name')
        with self.assertRaises(ValueError):
            db.objects.create_user(
                email ='',
                user_name = 'user_name',
                first_name = 'first_name',
                last_name = 'last_name',
                password = 'password',
                institut = 'local'
                )