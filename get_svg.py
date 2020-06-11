import os
from os import listdir, makedirs
from os.path import isfile, join, exists
import base64
from google.cloud import firestore
from PIL import Image
from random import randint

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"MY CREDENTIALS"

startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{0}px" height="{1}px" viewBox="0 0 {0} {1}">"""


endSvgTag = """</svg>"""


def get_font_xml(font_name, font_file, file_type):
    font_dir = r"PATH TO FONT"
    font_xml = "@font-face {{ \nfont-family: \"{0}\"; src: url(\"data:application/x-font-{2};base64,{1}\");\n}}\n"
    font_file = open(join(font_dir, font_file), "rb")
    font_data = base64.b64encode(font_file.read()).decode('utf-8')
    return font_xml.format(font_name, font_data, file_type)


def font_embed():
    xml_data = []
    css_open = '<style type="text/css">\n'
    xml_data.append(css_open)
    xml_data.append(get_font_xml("Trampoline demo", "Trampoline.ttf", "ttf"))
    xml_data.append(get_font_xml("mama", "mama.otf", "otf"))
    xml_data.append(get_font_xml("Hello", "Hello.otf", "otf"))
    css_close = '</style>\n'
    xml_data.append(css_close)
    #print(xml_data)
    return xml_data


def get_student_data(student):
    db = firestore.Client()
    collection = db.collection(u'students')
    document = collection.document(student)
    doc_dat = document.get().to_dict()["updateData"]
    #print(doc_dat)
    if "prefName" not in doc_dat.keys():
        doc_dat["prefName"] = ""
    special_data = [doc_dat["name"], doc_dat["prefName"], doc_dat["otherName"], doc_dat["house"], doc_dat["snrQuote"],
                    doc_dat["igAcc"]]
    full_data = {}
    description = {"missText": "What will you miss the most about Harrow? : ",
                   "adviceText": "Any advice for your younger self? : ",
                   "embarrassingText": "What was your most embarrassing moment? : ",
                   "excuseText": "What was your best excuse for not doing homework? : ",
                   "highlightText": "What was the highlight of your senior year? : "}
    for each_key in doc_dat.keys():
        if each_key not in ["name", "prefName", "otherName", "house", "snrQuote", "date", "imageLinks", "igAcc"]:
            full_data[description[each_key]] = doc_dat[each_key]
    #print(full_data)
    return special_data, full_data


template_usage = {"So": 1, "S": 1, "B": 1, "N": 1, "K": 1, "C": 4}


def split_multi_lines(text, x_val, y_start):
    quote_lines = []
    line_num = 0
    for each_line in text.split("\n"):
        line = '<tspan x="' + str(x_val) + '" y="' + str(y_start + 52 * line_num) + '">' + each_line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") + '</tspan>'
        line_num += 1
        quote_lines.append(line)
    return "".join(quote_lines)


def create(student_name, skip):
    global template_usage
    template_directory = r"PATH TO TEMPLATE"
    temp_directory = r"PATH TO TEMP"

    special, full = get_student_data(student_name)
    house = special[3]
    if template_usage[house] == 6:
        template_usage[house] = 0
    template_usage[house] += 1
    template_number = str(template_usage[house])
    template = house + "-" + template_number + ".png"
    file_name = join(template_directory, template)
    png_file = open(file_name, 'rb')
    template_im = Image.open(file_name)
    t_width, t_height = template_im.size

    write_data = []
    write_data.append(startSvgTag.format(str(t_width), str(t_height)))
    write_data += font_embed()

    template_data = base64.b64encode(png_file.read())
    png_file.close()
    template_xml = '<image xlink:href="data:image/png;base64,{0}" width="{1}" height="{2}" x="0" y="0"/>'.format(
        template_data.decode('utf-8'), str(t_width), str(t_height))
    write_data.append(template_xml)
    # Add Images


    image_directory = join(r"PATH TO INPUT", student_name)
    image_files = [f for f in listdir(image_directory) if isfile(join(image_directory, f))]
    for each_image in image_files:
        if "DS_Store" in each_image or "heic" in each_image.lower() or "temp" in each_image.lower():
            continue
        image_dir = join(image_directory, each_image)
        im = Image.open(image_dir)
        width, height = im.size
        aspect_ratio = height / width
        width = 1200
        height = 1200 * aspect_ratio
        im.thumbnail((width, height))
        img_format = each_image.split(".")[-1]
        temp_name = "temp." + img_format
        if img_format.upper() == "JPG":
            img_format = "JPEG"
        im.save(join(image_directory, temp_name), format=img_format)
        scaled_dir = join(image_directory, temp_name)
        image_file = open(scaled_dir, 'rb')
        image_data = base64.b64encode(image_file.read())
        image_xml = '\n<image xlink:href="data:image/{3};base64,{0}" width="{1}" height="{2}" x="0" y="0" preserveAspectRatio="xMidYMid meet" />\n'.format(image_data.decode('utf-8'), width, height, img_format)
        image_file.close()
        write_data.append(image_xml)

    text_start = '\n<text x="{2}" y="{3}" font-weight="{4}" font-family="{0}" font-size="{1}" opacity="1">'
    if special[1] != '':
        special_xml = text_start.format("Trampoline demo", "160", "300", "170", "bold") + special[1] + '</text>'
    else:
        special_xml = text_start.format("Trampoline demo", "160", "300", "170", "bold") + special[0] + '</text>'
    write_data.append(special_xml)
    nick_name_xml = text_start.format("mama", "80", "500", "280", "bold") + special[2].replace(",", ", ") + '</text>'
    write_data.append(nick_name_xml)
    ig_xml = text_start.format("Courier-Bold", "40", "450", "350", "bold") + "Instagram : " + special[5] + '</text>'
    write_data.append(ig_xml)
    quote_text = "\"" + special[4] + "\""
    quote_lines = []
    line_num = 0
    for each_line in quote_text.split("\n"):
        line = '<tspan x="500" y="' + str(2150 + 77 * line_num) + '">' + each_line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") + '</tspan>'
        line_num += 1
        quote_lines.append(line)
    quote_xml = text_start.format("Hello", "65", "500", "1800", "bold") + "".join(quote_lines) + '</text>'
    write_data.append(quote_xml)
    text_index = 0
    for description, each_value in {k: v for k, v in sorted(full.items(), key=lambda item: item[1])}.items():
        description_xml = text_start.format("Courier-Bold", "40", "200 ", str(450 + text_index * 350),
                                            "bold") + description + '</text>'
        write_data.append(description_xml)
        y_start = 450 + text_index * 350 + 60
        text_xml = text_start.format("Courier", "40", "200 ", y_start, "normal") + split_multi_lines(each_value, 200,
                                                                                                     y_start) + '</text>'
        write_data.append(text_xml)
        text_index += 1

    save_directory = temp_directory
    if not isfile(join(join(save_directory, house), student_name.replace(" ", "_") + ".svg")):
        save_directory = join(join(save_directory, "Late Responses"), house)
        if not exists(save_directory):
            makedirs(save_directory)
        save_directory = join(save_directory, "NEW-" + student_name.replace(" ", "_") + ".svg")
    else:
        save_directory = join(temp_directory, house)
        if not exists(save_directory):
            makedirs(save_directory)
        save_directory = join(save_directory, student_name.replace(" ", "_") + ".svg")
    write_data.append(endSvgTag)
    f = open(save_directory, 'w')
    f.writelines(write_data)
    f.close()
    print('Using ', template, ' for ', student_name.replace(" ", "_"), ".svg")


def generate_all(skip_existing, skip_late):
    db = firestore.Client()
    collection = db.collection(u'students')
    students = collection.list_documents()
    for each_student in students:
        if each_student.id == "Prototype User":
            continue
        if skip_existing:
            temp_directory = r"PATH TO OUTPUT"
            house_directory = join(temp_directory, each_student.get().to_dict()["updateData"]["house"])
            student_file = join(house_directory, each_student.id.replace(" ", "_") + ".svg")
            late_directory = join(join(temp_directory, "Late responses"), each_student.get().to_dict()["updateData"]["house"])
            late_file = join(late_directory, "NEW-" + each_student.id.replace(" ", "_") + ".svg")
            if isfile(student_file):
                print(each_student.id + " already exists. Skipping...")
                continue
            if skip_late and isfile(late_file):
                print(each_student.id + " already exists. Skipping...")
                continue
        create(each_student.id, skip_existing)


generate_all(skip_existing=True, skip_late=True)
