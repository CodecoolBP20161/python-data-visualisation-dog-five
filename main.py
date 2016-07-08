from datamanager import DataManager
from graphics import Graphics
from PIL import ImageFont
from project_name_runner import ProjctNumberRunner

db = DataManager()
db.create_tables("base_data.sql")

# text_options1 = {
#     'xy': (4, 5),
#     'fill': (0, 111, 255, 1),
#     'font': ImageFont.truetype("SourceSansPro-Regular.otf", 16),
#     'text': 'test1'
# }
#
# text_options2 = {
#     'xy': (104, 105),
#     'fill': (0, 111, 255, 1),
#     'font': ImageFont.truetype("SourceSansPro-Regular.otf", 160),
#     'text': 'test2'
# }
#
# options_list = [text_options1, text_options2]
#
# Graphics.setup(mode="RGBA", size=(1024, 1024), color="white")
#
# Graphics.make_image(options_list, "out.png")


def project_name_picture():
    data_list = ProjctNumberRunner('project-names.sql')
    return_list = data_list.dict_to_image()
    Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
    Graphics.make_image(return_list, "jani2.png")

project_name_picture()