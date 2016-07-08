from datamanager import DataManager
from graphics import Graphics
from PIL import ImageFont

manager = DataManager()


class BiggestEurProjects:

    def __init__(self, sql_string):
        self.project = manager.run_query(sql_string)

    def text_size(self):
        x = 0
        y = 0
        result = []
        font_size = 160
        for row in enumerate(self.project):
            print(row)
            if row[0] % 2 == 1:
                x = 500
            else:
                x = 0
            if row[0] != 0:
                y += 100
            font_size -= 10
            text_options = {
                'xy': (x, y),
                'fill': self.text_color(row[1][1]),
                'font': ImageFont.truetype("SourceSansPro-Regular.otf", font_size),
                'text': row[1][0]
            }
            result.append(text_options)

        return result

    def text_color(self, hexa):
        try:
            value = hexa.lstrip('#')
            colors = [int(v, 16)*17 for v in (x for x in value)]
            RGB_list = (0, colors[0], colors[1], colors[2])
            return RGB_list
        except AttributeError:
            RGB_list = (0, 255, 255, 255)
            return RGB_list


first = BiggestEurProjects('10-biggest-eur-projects-company.sql')
pic = first.text_size()

Graphics.setup(mode="RGBA", size=(1024, 1024), color="white")
Graphics.make_image(pic, "10-biggest-eur-projects-company.png")
