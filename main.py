from datamanager import DataManager
from graphics import Graphics
from PIL import ImageFont
from project_name_runner import ProjctNumberRunner
from due import DueDate
from biggest_eur_projects_company import BiggestEurProjects
import all_clients

db = DataManager()
db.create_tables("base_data.sql")
pict_ready = 'Picture generating...'


start = input('''
1. project name picure
2. all clients picture
3. due picture
4. 10 bigger project picture

Enter a number: ''')


def project_name_picture():
    data_list = ProjctNumberRunner('project-names.sql')
    return_list = data_list.dict_to_image()
    Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
    Graphics.make_image(return_list, "project-names.png")
    print(pict_ready)


def all_clients_picture():
    clients_rgb = all_clients.hex_to_rgb(all_clients.clients, all_clients.clients_colors)
    all_clients.rgb_dic(clients_rgb)
    dic_list = all_clients.rgb_dic(clients_rgb)
    Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
    Graphics.make_image(dic_list, 'all_clients.png')


def biggest_picture():
    data_list = BiggestEurProjects('10-biggest-eur-projects-company.sql')
    return_list = data_list.text_size()
    Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
    Graphics.make_image(return_list, "biggest-project.png")
    print(pict_ready)


def due_picture():
    data_list = db.run_query("due.sql")
    new_list = DueDate.time_converter(data_list)
    return_list = DueDate.make_dict(new_list)

    Graphics.setup(mode="RGBA", size=(1024, 1024), color=(255, 255, 255, 200))
    Graphics.make_image(return_list, "due.png")


if start == '1':
    project_name_picture()
elif start == '2':
    all_clients_picture()
elif start == '3':
    due_picture()
elif start == '4':
    biggest_picture()
elif start == 'q':
    run = False



