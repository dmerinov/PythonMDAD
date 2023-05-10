import firebase_admin
import csv
import sys
from pathlib import Path
from firebase_admin import credentials
from firebase_admin import firestore


def connect():
    # Torre
    #credential = credentials.Certificate("C:\\Users\\dmerinov-lt\\PycharmProjects\\PythonMDAD\\connection\\firestoreKey.json")
    # Portatil
    credential = credentials.Certificate('connection/firestoreKey.json')

    firebase_admin.initialize_app(credential)

    db = firestore.client()
    return db


def obtain_products():

    #filepath_torre = 'C:\\Users\\wotan\\Desktop\\PythonMDAD\\csvOutput\\file.csv'
    filepath_portatil = 'csvOutput/filePortatil.csv'

    FIELDS = ['nombre', 'stock', 'tienda', 'precio']
    instance = connect()
    writer = csv_writer(open(filepath_portatil, 'w'), FIELDS)
    # writer = csv_writer(sys.stdout, FIELDS)
    writer.writeheader()

    for snapshot in instance.collection('productos').get():
        data = snapshot.to_dict()
        writer.writerow(data)
    products = instance.collection('productos').get()
    my_dict = {el.id: el.to_dict() for el in products}
    # print(my_dict)

    return my_dict


def csv_writer(file, fields):
    """Generate CSV writer"""
    return csv.DictWriter(file, fields)
