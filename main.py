from datamanager import DataManager
from graphics import Graphics
from PIL import ImageFont
from project_name_runner import ProjctNumberRunner
from due import DueDate

db = DataManager()
db.create_tables("base_data.sql")
pict_ready = 'Picture generating...'


start = input('''
1. project name picure
2. all clients picture
3. due picture
4. 10 bigger project picture
Q. To exit

Enter a number: ''')


def project_name_picture():
    data_list = ProjctNumberRunner('project-names.sql')
    return_list = data_list.dict_to_image()
    Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
    Graphics.make_image(return_list, "project-names.png")
    print(pict_ready)


def due_picture():
    data_list = db.run_query("due.sql")
    new_list = DueDate.time_converter(data_list)
    return_list = DueDate.make_dict(new_list)
    Graphics.setup(mode="RGBA", size=(1024, 1024), color="white")
    Graphics.make_image(return_list, "due.png")
    print(pict_ready)


if start == '1':
    project_name_picture()
elif start == '2':
    None
elif start == '3':
    due_picture()
elif start == '4':
    None
elif start == 'q':
    run = False



