from datamanager import DataManager
from graphics import Graphics
from project_name_runner import ProjctNumberRunner


db = DataManager()
db.create_tables("base_data.sql")
data_list = ProjctNumberRunner('project-names.sql')
return_list = data_list.dict_to_image()

Graphics.setup(mode="RGB", size=(1024, 1024), color="white")
Graphics.make_image(return_list, "jani.png")