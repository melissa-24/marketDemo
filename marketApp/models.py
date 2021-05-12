from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['firstName']) < 2:
            errors['firstName'] = 'First Name must be at least 2 characters'

        if len(form['lastName']) < 2:
            errors['lastName'] = 'Last Name must be at least 2 characters'

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email Address already in use'

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'

        if len(form['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    objects = UserManager()

    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    shopName = models.CharField(max_length=45)
    shopDescription = models.TextField()
    shopOwner = models.ForeignKey(User, related_name='store', on_delete=models.CASCADE)

class Product(models.Model):
    itemName = models.CharField(max_length=45)
    itemDescription = models.TextField()
    itemPrice = models.CharField(max_length=45)
    itemImg = models.CharField(max_length=255)
    itemCount = models.IntegerField()
    itemShop = models.ForeignKey(Shop, related_name='theShop', on_delete=models.CASCADE)

class Category(models.Model):
    catName = models.CharField(max_length=45)
    assignedCat = models.ManyToManyField(Product, related_name='categories')
