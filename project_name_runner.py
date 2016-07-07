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
            print(font_size)
        x_random_list = []
        y_ranrom_list = []
        counter = 0
        for row in self.project:
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            x_random_list.append(x)
            y_ranrom_list.append(y)
            if x in x_random_list or y in y_ranrom_list:
                print("HAHOOOOOOOO!!!!!")
                while x not in x_random_list and y not  in y_ranrom_list:
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    counter += 1
            try:
                value = row[3].lstrip('#')
            except AttributeError:
                None
            rgb_code = [int(v, 16)*17 for v in (z for z in value)]
            rgb_code.append(1)

            append_dict = {'text':(row[0]), 'fill':tuple(rgb_code),
                           'font': ImageFont.truetype("SourceSansPro-Regular.otf",  font_size),
                             'xy': (x, y)}

            list_of_dict.append(append_dict)
        print(list(list_of_dict))
        print(counter)
        return list(list_of_dict)

valami = ProjctNumberRunner('project-names.sql')
pic = valami.dict_to_image()

Graphics.setup(mode="RGB", size=(1024, 1024), color="black")
Graphics.make_image(pic, 'project-fall.png')


'''
Just for test:
#valuta_change()
#sending(first)
#rgb_converter(first)
#dict_to_immge(first)
#print(valuta_change())
'''