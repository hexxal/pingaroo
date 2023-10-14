from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """
    Custom manager for User.
    """
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email, password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(TimestampedModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-Mail address', unique=True)
    name = models.CharField('Name', max_length=128, blank=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Staff status', default=False, help_text="Designates whether the user can log into this admin site.")

    USERNAME_FIELD = 'email'

    objects = UserManager()

class MonitorTarget(TimestampedModel):
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monitor_targets')

    def __str__(self):
        return self.url


class MonitorResult(TimestampedModel):
    target = models.ForeignKey(MonitorTarget, on_delete=models.CASCADE, related_name='results')
    is_down = models.BooleanField()
    latency = models.IntegerField(null=True)

    def __str__(self):
        return self.target.url
