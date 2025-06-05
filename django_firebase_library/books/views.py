from django.shortcuts import render, redirect
from django.apps import apps
import firebase_admin
from firebase_admin import credentials, db
from .forms import BookForm  

def connectDB():
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase_key.json") 
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://library-project-9561c-default-rtdb.firebaseio.com/"
        })
    return db.reference("BooksList")

def booklist(request):
    books = []
    dbconn = connectDB()
    tblBooks = dbconn.get()

    if tblBooks:
        for key, value in tblBooks.items():
            books.append({
                "id": value.get("ID"),
                "title": value.get("Book_Title"),
                "author": value.get("Author_Name"),
                "genre": value.get("Genre")
            })

    return render(request, 'bookslist.html', {'books': books})

def addbook(request):
    if request.method == 'GET':
        return render(request, 'addbook.html')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            title = form.cleaned_data.get("title")
            author = form.cleaned_data.get("author")
            genre = form.cleaned_data.get("genre")
            dbconn = connectDB()
            dbconn.push({
                "ID": id,
                "Book_Title": title,
                "Author_Name": author,
                "Genre": genre
            })
        return redirect('BooksList')

def updatebook(request, id):
    br = []
    dbconn = connectDB()
    tblBooks = dbconn.get()

    if tblBooks and request.method == 'GET':
        for key, value in tblBooks.items():
            if value["ID"] == id:
                global updatekey
                updatekey = key
                br.append({
                    "id": value["ID"],
                    "title": value["Book_Title"],
                    "author": value["Author_Name"],
                    "genre": value["Genre"]
                })
        return render(request, 'addbook.html', {'book': br[0]})
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            author = form.cleaned_data.get("author")
            genre = form.cleaned_data.get("genre")
            updateitem = dbconn.child(updatekey)
            updateitem.update({
                "ID": id,
                "Book_Title": title,
                "Author_Name": author,
                "Genre": genre
            })
        return redirect('BooksList')

def deletebook(request, id):
    dbconn = connectDB()
    tblBooks = dbconn.get()
    if tblBooks:
        for key, value in tblBooks.items():
            if value["ID"] == id:
                deletekey = key
                delitem = dbconn.child(deletekey)
                delitem.delete()
                break
    return redirect('BooksList')
