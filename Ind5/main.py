import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
import os.path
from lxml import etree, objectify


def parse_painting_xml(xml_file):
    with open(xml_file) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)

    paintings = []
    for painting in root.getchildren():
        one_painting = []
        for elem in painting.getchildren():
            if not elem.text:
                one_painting.append("None")
            else:
                one_painting.append(elem.text)
        paintings.append(one_painting)

    return [tuple(i) for i in paintings]


def create_appt(data):  # Создаем изначальную структуру XML

    appt = objectify.Element("author")
    appt.id_aut = data["id_aut"]
    appt.last_name = data["last_name"]
    appt.first_name = data["first_name"]
    appt.date_birth = data["date_birth"]
    return appt


def create_xml():  # Создаем XML файл

    xml = '''<?xml version="1.0"?>
    <author_table>
    </author_table>
    '''

    root = objectify.fromstring(xml)

    appt = create_appt({"id_aut": "1",
                        "last_name": "Picasso",
                        "first_name": "Pablo",
                        "date_birth": "08-04-1973"}
                       )
    root.append(appt)

    appt = create_appt({"id_aut": "2",
                        "last_name": "Dali",
                        "first_name": "Salvador",
                        "date_birth": "11-05-1904"}
                       )
    root.append(appt)

    # удаляем все lxml аннотации.
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)

    # конвертируем все в привычную нам xml структуру.
    obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)

    try:
        with open("obj_xml", "wb") as xml_writer:
            xml_writer.write(obj_xml)
        print("Я открылся!")
    except IOError:
        print("Никогда не ошибается тот, кто ничего не делает.")
        pass


if not os.path.isfile('example.db'):
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE author
            (id_aut INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT,
            first_name TEXT,
            date_birth TEXT)''')

    cur.execute('''CREATE TABLE paintings
            (id_pai INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            show_date TEXT)''')

    cur.execute('''CREATE TABLE gallery
            (id_gallery INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            id_aut INTEGER,
            genre TEXT,
            id_pai INTEGER,
            publication TEXT,
            FOREIGN KEY (id_aut) REFERENCES author(id_aut),
            FOREIGN KEY (id_pai) REFERENCES paintings(id_pai))''')

    authors = [(1, 'Picasso', 'Pablo', '08-04-1973'),
               (2, 'Dali', 'Salvador', '11-05-1904'),
               (3, 'Claude', 'Monet ', '14-11-1840')]

    sql = '''INSERT INTO author(id_aut,last_name,first_name,date_birth) VALUES(?,?,?,?)'''
    con.executemany(sql, authors)

    paintings = [(1, 'Mona lisa', 'Moscow', '1812'),
                 (2, 'Girl in front of the mirror', 'London', '1984'),
                 (3, 'The Persistence of Memory', 'Moscow', '1996')]

    sql = '''INSERT INTO paintings(id_pai,name,country,show_date) VALUES(?,?,?,?)'''
    con.executemany(sql, paintings)

    gallery = [(1, 'Louvre', 1, 'Self-portrait', 1, '23-04-1973'),
               (2, 'Subway', 2, 'Hidden meaning', 2, '15-01-1920'),
               (3, 'London National Gallery', 3, 'Rethinking', 3, '28-10-2021')]

    sql = '''INSERT INTO gallery(id_gallery,name,id_aut,genre,id_pai,publication) VALUES(?,?,?,?,?,?)'''
    con.executemany(sql, gallery)

    xml_painting = parse_painting_xml("base_out.xml")  #
    con.executemany(sql, xml_painting)  #

    con.commit()

create_xml()  #

server_address = ("localhost", 7000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
http_server.serve_forever()
