from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"MY CREDENTIALS"

names = [] #NAMES TO CHECK

db = firestore.Client()
collection = db.collection(u'students')
student_in_database = collection.list_documents()
names_in_database = []
for student in student_in_database:
    names_in_database.append(student.id)
names_not_submitted = []
for each_name in names:
    if each_name.lower() not in names_in_database:
        names_not_submitted.append(each_name)

db = firestore.Client()
collection = db.collection(u'working')
working_in_database = collection.list_documents()
names_in_working = []
for student in working_in_database:
    names_in_working.append(student.id)
print(names_in_working)
names_not_recorded = []
for each_name in names:
    if each_name.lower() not in names_in_working:
        names_not_recorded.append(each_name)

names_no_record = []
names_awaiting_submission = []
for each_not_submitted in names_not_submitted:
    if each_not_submitted in names_not_recorded:
        names_no_record.append(each_not_submitted)
    else:
        names_awaiting_submission.append(each_not_submitted)

print("\nAwaiting Submission: ")
for each_waiting_submission in names_awaiting_submission:
    print(each_waiting_submission)
print("\n\nNo Record: ")
for each_no_record in names_no_record:
    print(each_no_record)