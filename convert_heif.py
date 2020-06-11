from PIL import Image
import pyheif
import os
from os.path import join, isfile
from os import listdir
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"MY CREDENTIALS"


def convert_all():
    db = firestore.Client()
    collection = db.collection(u'students')
    students = collection.list_documents()
    for each_student in students:
        if each_student.id == "Prototype User":
            continue
        convert(each_student.id)


def convert(student_name):
    image_directory = join(r"PATH TO INPUT IMAGES", student_name)
    image_files = [f for f in listdir(image_directory) if isfile(join(image_directory, f))]
    # print(image_files)
    for file_name in image_files:
        if "heic" in file_name.lower():
            save_dir = join(image_directory, join(file_name.replace(".HEIC", ".JPG").replace(".heic", ".jpg")))
            if isfile(save_dir):
                print("Skipping : " + file_name + ", jpg version already exists")
                continue
            print(file_name)
            file_bytes = open(join(image_directory, file_name), "rb")
            i = pyheif.read_heif(file_bytes)
            image = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
            image.save(save_dir, format="JPEG")


convert_all()