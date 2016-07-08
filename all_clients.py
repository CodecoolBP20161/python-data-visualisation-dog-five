from PIL import ImageFont
from datamanager import DataManager
from graphics import Graphics
from due import DueDate
import psycopg2
import getpass
import os
from operator import add
import random


manager = DataManager()
manager.create_tables('base_data.sql')

clients = manager.run_query('all-client-at-once.sql')
clients_colors = manager.run_query('all-client-at-once-color.sql')

Class AllClients:
    '''Generate picture of all clients'''
    def hex_to_rgb(clients, clients_colors):
        clients_rgb = sorted([list(tup) for tup in clients_colors], key=lambda tup: tup[0])
        for element in clients_rgb:
            if element[1] is not None:
                element[1] = element[1].lstrip("#")
                element[1] = [int(v, 16)*17 for v in (char for char in element[1])]
            else:
                element[1] = [255, 255, 255]
        # print(clients_rgb)
        return clients_rgb


def rgb_dic(clients_rgb):
    name_list = []
    dic_list = []
    for i in clients_rgb:
        x = random.randint(0, 1024)
        y = random.randint(0, 1024)
        z = random.randint(15, 150)

        if i[0] not in name_list:
            name_list.append(i[0])
            dic_list.append({
                            'xy': (x, y),
                            'font': ImageFont.truetype("SourceSansPro-Regular.otf", y),
                            "text": i[0],
                            "fill": tuple(i[1])
                            })
    print(dic_list)
    return dic_list


clients_rgb = hex_to_rgb(clients, clients_colors)
rgb_dic(clients_rgb)
dic_list = rgb_dic(clients_rgb)
Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
Graphics.make_image(dic_list, 'all_clients.png')
