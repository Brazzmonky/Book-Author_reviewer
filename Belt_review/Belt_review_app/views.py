from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def home(request):
	return render(request, 'home.html')


def newUser(request):
	errors = User.objects.register_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		password=request.POST['password']
		pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		newUser=User.objects.create(user_name=request.POST['user_name'],alias=request.POST['alias'],email=request.POST['email'],password=pw_hash.decode())
		context={
		"users": User.objects.all()	
		}
		request.session['loggedinUserID'] = newUser.id
		return redirect('/Success')


def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		loggedinUser = User.objects.get(email=request.POST['email'])
		request.session['loggedinUserID'] = loggedinUser.id
		print(loggedinUser.user_name)	
		return redirect('/Success')


def Success(request):
	ordered_reviews=Review.objects.all().order_by('-created_at')[:3]
	context={
	"ordered_reviews": ordered_reviews,
	"all_users": User.objects.all(),
	"all_books": Book.objects.all(),
	"all_authors": Author.objects.all(),
	"all_reviews": Review.objects.all(),
	"loggedinUser": User.objects.get(id=request.session['loggedinUserID'])
	}
	return render(request, "Books.html",context)	


def logout(request):
	request.session.clear()
	return redirect("/")


def add_book_and_review(request):
	context={
	"all_users": User.objects.all(),
	"all_books": Book.objects.all(),
	"all_authors": Author.objects.all(),
	"all_reviews": Review.objects.all(),
	"loggedinUser": User.objects.get(id=request.session['loggedinUserID'])
	}
	return render(request, "add_book_and_review.html", context)	


def viewbook(request,bookid):
	book_to_display=Book.objects.get(id=bookid)
	reviews=Review.objects.filter(book=Book.objects.get(id=bookid))
	context={
	"all_reviews": Review.objects.all(),
	"reviews": reviews,
	"loggedinUser": User.objects.get(id=request.session['loggedinUserID']),
	"book_to_display": book_to_display,
	}

	return render(request, "show_book_and_reviews.html",context)


def newbookandreview(request):
	errors = Book.objects.book_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/add_book_and_review')
	else:
		print(request.POST)
		context={
		"all_users": User.objects.all(),
		"all_books": Book.objects.all(),
		"all_authors": Author.objects.all(),
		"all_reviews": Review.objects.all(),
		"loggedinUser": User.objects.get(id=request.session['loggedinUserID'])
	}
		loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
		author=Author.objects.get(id = request.POST['author'])
		new_book=Book.objects.create(title=request.POST['title'],author=author)
		new_review=Review.objects.create(rating=int(request.POST['rating']),comment=request.POST['comment'],user=loggedinUser,book=new_book)

	return redirect('/viewbook/' + str(new_book.id))


def addreview(request,bookid):
	errors =Review.objects.review_validator(request.POST)
	if len(errors) >0:
		for key, value in errors.items():
			messages.error(request,value)
		return redirect('/viewbook/' + str(bookid))
	else:
		context={
		"all_users": User.objects.all(),
		"all_books": Book.objects.all(),
		"all_authors": Author.objects.all(),
		"all_reviews": Review.objects.all(),
		"loggedinUser": User.objects.get(id=request.session['loggedinUserID'])
	}
		loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
		new_review=Review.objects.create(rating=int(request.POST['rating']),comment=request.POST['comment'],user=loggedinUser,book=Book.objects.get(id=bookid))
	return redirect('/viewbook/' + str(bookid))	

def viewuser(request,userid):
	user_to_display=User.objects.get(id=userid)
	reviews=Review.objects.filter(user=User.objects.get(id=userid))
	context={
	"user_to_display":user_to_display,
	"reviews":reviews,
	}
	return render(request, 'user_reviews.html', context)

def gohome(request):
	return redirect('/Success')


def boop(request,reviewid):
	loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
	review_to_delete=Review.objects.get(id=reviewid)
	review_to_delete.delete()
	return redirect("/viewbook/" + str(bookid))