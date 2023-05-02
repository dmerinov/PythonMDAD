import pandas as pd

from connection.EjemploIris import ejemplo_iris
from connection.Firebase import *


def init():
    products = obtain_products()
    print(products.values())

# ejemplo_iris()


if __name__ == '__main__':
    init()
