from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from datamanager import DataManager
from graphics import Graphics
from due import DueDate


db = DataManager()
db.create_tables("base_data.sql")
data_list = db.run_query("due.sql")
new_list = DueDate.time_converter(data_list)
return_list = DueDate.make_dict(new_list)




Graphics.setup(mode="RGBA", size=(13660, 7680), color=(255, 255, 255, 200))
Graphics.make_image(return_list, "due.png")


