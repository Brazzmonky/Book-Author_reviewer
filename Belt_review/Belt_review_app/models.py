from __future__ import unicode_literals
from django.db import models
import re, bcrypt



class UserManager(models.Manager):
	def register_validator(self, postData):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors= {}
		validemail=User.objects.filter(email=postData['email'])
		if len(validemail) > 0:
			errors['email']="Email already in use. Please log in or choose another"
		if not EMAIL_REGEX.match(postData['email']):           
			errors['email'] = "Invalid email address!"	
		if len(postData ['user_name']) < 2:
			errors['user_name'] = "Required field, please input a name of at least 2 letters"
		if len(postData ['password']) < 8:
			errors['password']= "Required field, please input a password of at least 8 characters"
		if postData['password']	!= postData['confirmpw']:
			errors['confirmpw']= "Passwords must match"
		return errors


	def login_validator(self,postData):
		useremail=User.objects.filter(email=postData['email'])
		errors= {}
		if len(postData['email']) == 0:
			errors['emaillen']= "Required field please enter a valid email."
		if len(useremail) < 1:
			errors['email']="No Email matching that address, please register or try another Email."
		else:
			print(useremail)
			user=User.objects.get(email=postData['email'])	
			if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
				print("password match")
			else:
				errors['passwordfailed']= "Incorrect password, please try again."
				print("failed password")
		return errors	


class User(models.Model):
	user_name=models.CharField(max_length=255)
	alias=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects = UserManager()
	def __repr__(self):
		return f"class_name: {self.user_name} {self.alias} ({self.created_at}) ({self.updated_at})"



class AuthorManager(models.Manager):
	def author_validator(self,postData):
		errors= {}
		if len(postData['author_name']) < 5:
			errors['author_name']= "valid Author name Required, choose one from list or create one."
		return errors
		
class Author(models.Model):
	author_name=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects = AuthorManager()
	def __repr__(self):
		return f"class_name: {self.author_name} ({self.created_at}) ({self.updated_at})"



class BookManager(models.Manager):
	def book_validator(self,postData):
		errors={}
		if len(postData['title']) <3:
			errors['title']="Please enter a book title of at least 3 characters."
		return errors			

class Book(models.Model):
	title=models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="book", on_delete=models.CASCADE, default=None, null=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects=BookManager()
	def __repr__(self):
		return f"class_name: {self.title} {self.author} ({self.created_at}) ({self.updated_at})"


class ReviewManager(models.Manager):
	def review_validator(self,postData):
		errors={}
		if len(postData['comment']) <10:
			errors['comment']="please write a review of at least 10 characters."
		return errors	

class Review(models.Model):
	rating=models.IntegerField()
	comment=models.CharField(max_length=255)
	user=models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE, default=None, null=True)
	book = models.ForeignKey(Book, related_name="review", on_delete=models.CASCADE, default=None, null=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects=ReviewManager()
	def __repr__(self):
		return f" {self.rating} {self.author} {self.book} ({self.created_at}) ({self.updated_at})"
		