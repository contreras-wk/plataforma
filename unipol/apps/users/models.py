
from django.db import models
from django.utils import timezone


class Role(models.Model):
    """ Tipo Usuario """
    # id
    name = models.CharField(max_length=20, unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} | {self.name}'
    


class Permission(models.Model):
    """ Permisos para el usuario """
    # id 
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    register_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'{self.id} | {self.name}'


class User(models.Model):
    """ Usuarios """
    # id
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=12)
    email = models.EmailField()
    name = models.CharField(max_length=50, help_text="Entry name")
    last_name = models.CharField(max_length=50, help_text="Entry last name")
    mothers_last_name = models.CharField(max_length=50, help_text="Entry mothers last name")
    plate = models.IntegerField()
    status = models.BooleanField()
    register_date = models.DateField(default=timezone.now)

    permisisons = models.ManyToManyField(Permission, through='UserPermision')
    role = models.OneToOneField(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username} | {self.email}'


class Institution(models.Model):
    # id 
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    register_date = models.DateField(default=timezone.now)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.name}'


class UserPermision(models.Model):
    """ Relacion para los permisos de usuario """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.users} | {self.permission}'
    
