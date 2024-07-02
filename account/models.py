from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, phone, location, password=None, password2=None):
        """Creates and saves a User with the given email, name, tc, phone, location, and password"""
        if not email:
            raise ValueError('User must have an email address')
        if not phone:
            raise ValueError('User must have a phone number')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
            phone=phone,
            location=location,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, phone, location, password=None):
        """
        Creates and saves a superuser with the given email, name, tc, phone, location, and password.
        """
        user = self.create_user(
            email,
            name=name,
            tc=tc,
            phone=phone,
            location=location,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$')],
        unique=True,
        verbose_name='Phone Number',
        default='0000000000'  # Default value for existing rows
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    location = models.CharField(max_length=255, blank=True, null=True)  # New field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc', 'phone', 'location']

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


