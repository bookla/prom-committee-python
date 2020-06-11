from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"MY CREDENTIALS"

print("Move working data")
name_from = input("From: ")
name_to = input("To: ")
db = firestore.Client()
collection = db.collection(u'working')
document = collection.document(name_from)
doc_data = document.get().to_dict()

document_new = collection.document(name_to)
input("THIS WILL REPLACE ANY OLD DATA FOR DESTINATION!")
document_new.set(doc_data)