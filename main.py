from connection.Firebase import *
from model.Product import ProductItem
import matplotlib.pyplot as plt


def init():
    products = obtain_products()
    # print(products.values())

    product_dict_list = list(products.values())
    print(product_dict_list)
    product_model_list = []

    for item in product_dict_list:
        # print(item.get("nombre"))
        # print(type(item))
        product_model_list.append(
            ProductItem(item.get("nombre"), item.get("stock"), item.get("tienda"), item.get("precio")))

    stock_location_graph(product_model_list)
    price_location_graph(product_model_list)


# ejemplo_iris():

def price_location_graph(product_model_list):
    x = []
    y = []

    for item in product_model_list:
        print(f'name: {item.name}')
        print(f'stock: {item.stock}')
        print(f'shop: {item.shop}')
        print(f'precio: {item.price}')
        print("---------------")
        x.append(item.shop)
        y.append(item.price)

    # plotting a bar chart
    plt.bar(x, y)

    # naming the x-axis
    plt.xlabel('localización')
    # naming the y-axis
    plt.ylabel('precio')
    # plot title
    plt.title('Comparativa Precio - Localización')

    # function to show the plot
    plt.show()


def stock_location_graph(product_model_list):
    x = []
    y = []

    for item in product_model_list:
        print(f'name: {item.name}')
        print(f'stock: {item.stock}')
        print(f'shop: {item.shop}')
        print(f'precio: {item.price}')
        print("---------------")
        x.append(item.shop)
        y.append(item.stock)

    # plotting the points
    # labels for bars
    tick_label = ['one', 'two', 'three', 'four', 'five']

    # plotting a bar chart
    plt.bar(x, y)

    # naming the x-axis
    plt.xlabel('localización')
    # naming the y-axis
    plt.ylabel('y - stock')
    # plot title
    plt.title('Comparativa Stock - Localización')

    # function to show the plot
    plt.show()


if __name__ == '__main__':
    init()
