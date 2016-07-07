import random
from datamanager import DataManager
from PIL import ImageFont
from graphics import Graphics

# first = 'project-names.sql'
manager = DataManager()

class ProjctNumberRunner:
    USD_to_EUR = 0.902580
    GBP_to_EUR = 1.167715

    def __init__(self, sql_string):
        self.project = manager.run_query(sql_string)


    def valuta_change(self):
        valuta_list = []
        for row in self.project:
            if row[2] == 'USD':
                usd = row[1]
                x = (float(usd)*self.USD_to_EUR)
                x = round(x / 150)
                valuta_list.append(x)

            elif row[2] == 'GBP':
                gbp = row[1]
                y = (float(gbp) * self.GBP_to_EUR)
                y = round(y / 150)
                valuta_list.append(y)

            else:
                eur = row[1]
                z = float(eur)
                z = round(z/150)
                valuta_list.append(z)

        return valuta_list

    def dict_to_image(self):
        self.valuta_change()
        list_of_dict = []
        for i in self.valuta_change():
            font_size = i
        x = 0
        y = 200

        for row in self.project:

            try:
                value = row[3].lstrip('#')
            except AttributeError:
                None
            rgb_code = [int(v, 16)*17 for v in (z for z in value)]
            rgb_code.append(1)

            append_dict = {'text':(row[0]), 'fill':tuple(rgb_code),
                           'font': ImageFont.truetype("SourceSansPro-Regular.otf",  font_size),
                             'xy': (x, y)}
            for h in range(len(append_dict)):
                if y <= 1600:
                    x += 35
                    y += 35
                elif y >= 1400:
                    x -= 55
                    y -= 75

            list_of_dict.append(append_dict)
        print(list(list_of_dict))
        return list(list_of_dict)

# pl = ProjctNumberRunner('project-names.sql')
# manager.create_tables('base_data.sql')
valami = ProjctNumberRunner('project-names.sql')
pic = valami.dict_to_image()

Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
Graphics.make_image(pic, 'project-fall.png')

# print(pl.dict_to_image())
'''
Just for test:
#valuta_change()
#sending(first)
#rgb_converter(first)
#dict_to_immge(first)
#print(valuta_change())
'''