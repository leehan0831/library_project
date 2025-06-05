import firebase_admin
from firebase_admin import credentials, db

# Use your actual downloaded Firebase private key JSON
cred = credentials.Certificate("firebase_key.json")

firebase_admin.initialize_app(cred, {
    'databaseURL':'https://library-project-9561c-default-rtdb.firebaseio.com/'  
})
dbref = db.reference("BooksList")
dbref.push( { "ID": 1, "Book_Title": "Tom and jelly", "Author_Name": "Lee", "Genre": "Drama" } )
dbref.push( { "ID": 2, "Book_Title": "Marry", "Author_Name": "Han", "Genre": "Drama" } )

print(dbref.get())