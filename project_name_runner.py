import random
from datamanager import DataManager
from PIL import ImageFont


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
        for row in self.project:
            x = random.randint(0, 700)
            y = random.randint(0, 1000)
            font_size = random.randint(15, 80)
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
        return list(list_of_dict)
