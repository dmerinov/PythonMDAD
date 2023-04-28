import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def connect():
    credential = credentials.Certificate("C:\\Users\\wotan\\Desktop\\PythonMDAD\\connection\\firestoreKey.json")
    firebase_admin.initialize_app(credential)

    db = firestore.client()
    return db


def obtain_products():
    instance = connect()

    products = instance.collection('productos').get()
    my_dict = {el.id: el.to_dict() for el in products}
   # print(my_dict)

    return my_dict
