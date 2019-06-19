import firebase_admin
from firebase_admin import credentials
import pyrebase





def store(name,path):

	config = {
	"apiKey": "apiKey",
	"authDomain": "drivemimic.firebaseapp.com",
	"databaseURL": "https://drivemimic.firebaseio.com",
	"storageBucket": "drivemimic.appspot.com",
	
	}

	firebase = pyrebase.initialize_app(config)
	storage=firebase.storage()
	loc="files/"+str(name)
	new_path="../drive/media/"+str(path)
	storage.child(str(loc)).put(str(new_path))
	
	

# def url(name,token):
# 	config = {
# 	"apiKey": "apiKey",
# 	"authDomain": "drivemimic.firebaseapp.com",
# 	"databaseURL": "https://drivemimic.firebaseio.com",
# 	"storageBucket": "drivemimic.appspot.com",
	
# 	}

# 	firebase = pyrebase.initialize_app(config)
# 	storage=firebase.storage()
# 	loc="files/"+str(name)
# 	storage.child(str(loc)).get_url
# 	req_url=storage.child(str(loc)).get_url(token['downloadTokens'])

# 	return req_url


#store("test6","../../drive/media/71u1wFeO9-L._SL1152_.jpg")