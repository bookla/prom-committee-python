import os
import time
from os.path import exists, join, isfile
from os import makedirs
import urllib.request
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"MY CREDENTIALS"

def get_all():
    db = firestore.Client()
    collection = db.collection(u'students')
    students = collection.list_documents()
    directory = r"PATH TO INPUT FILE"
    for each_student in students:
        if each_student.id == "Prototype User":
            continue
        student_data = each_student.get().to_dict()["updateData"]
        images_list = student_data["imageLinks"]
        save_directory = join(directory, each_student.id)
        if not exists(save_directory):
            makedirs(save_directory)
        for image_url in images_list:
            if "serviceAdd" in image_url:
                file_name = image_url.split("/")[-1]
            else:
                cut_end = image_url.split("?alt")[0]
                file_name = cut_end.split("%2F")[1]
            if isfile(join(save_directory, file_name)):
                print("File Already Downloaded, skipping")
                continue
            while True:
                try:
                    urllib.request.urlretrieve(image_url, join(save_directory, file_name))
                    print("Downloaded : " + file_name)
                except Exception as e:
                    print(e)
                    print("Retrying...")
                    time.sleep(1)
                    continue
                break
        print("Completed Download for : " + each_student.id)


get_all()