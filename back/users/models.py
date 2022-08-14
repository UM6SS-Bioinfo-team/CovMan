from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_superuser (self,email, user_name, first_name, last_name, institut, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email,user_name,first_name,last_name,password,institut, **other_fields)

    def create_user(self,email,user_name, first_name, last_name, password, institut, **other_fields):
        if not email:
            raise ValueError(_('You must provide email adress'))

        email = self.normalize_email(email)
        user = self.model(email  = email, user_name = user_name, institut = institut, first_name = first_name, last_name = last_name, **other_fields)
        user.set_password(password)
        user.save()

        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    # id = models.IntegerField(primary_key=True)
    class Meta:
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')
    email = models.EmailField(_('Email address'), unique=True)
    institut = models.CharField(_('Institute'),max_length=250)
    identifier = models.CharField(_('identifiant'),blank=False,max_length=100,unique=True)
    department = models.CharField(_("department"),max_length=250, blank=True)
    user_name = models.CharField(_("username"),max_length=150, unique=True)
    first_name = models.CharField(_("first name"),max_length=150)
    last_name = models.CharField(_("last name"),max_length=150)
    last_login = models.DateTimeField(_("derniere date de connection"),default=timezone.now)
    start_date = models.DateTimeField(_("date d'ajout"),default=timezone.now)
    about = models.TextField(_('about'),max_length=500,blank=True)
    is_staff = models.BooleanField(_("membre d'equipe"),default=False)
    is_active = models.BooleanField(_("Compte active"),default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['institut','user_name', 'first_name','last_name']
    def __str__(self):
        return self.user_name



class Virus (models.Model):
    pass
class Patient (models.Model):
    pass
class Variants (models.Model):
    pass