from datamanager import DataManager
from graphics import Graphics
from PIL import ImageFont
import random

import datetime

#function creates dict list for graphics.py
class DueDate:
    """This class will handle all DueDate stuff"""
    @classmethod
    def time_converter(cls, data_list):
        """Returns the delta to today"""
        new_list = [(x[0], (x[1] - datetime.datetime.now().date()).days) for x in data_list]
        #print(a)
        #new_list = [x for x in a if 0 < x[1]]
        return(new_list)

    @classmethod
    def make_dict(cls, new_list):
        return_list = []
        size_list = []

        min_days = min([x[1] for x in new_list])
        max_days = max([x[1] for x in new_list])

        for i, elem in enumerate(new_list):
            k = (new_list[i][1] - min_days) / (max_days - min_days)
            font_size = int(50 * k)
            font = ImageFont.truetype("SourceSansPro-Regular.otf", font_size)
            text = str(new_list[i][0])
            x, y = font.getsize(text)
            size_list.append((x,y))
            r = int(255 * (1 - k))
            g = int(255 * k)
            b = random.randint(0, 255)
            o = int(50 + 150 * k)
            fill = (r, g, b, o)
            return_list.append({
                                #'xy': xy,
                                'fill': fill,
                                'font': font,
                                'text': text
                                })

        xy_list = []
        bad_xy = set()

        size_list.reverse()

        for i, size in enumerate(size_list):
            new_xy = set()

            while True:
                new_x = random.randint(0, 13660 - size_list[i][0])
                new_y = random.randint(0, 7680 - size_list[i][1])

                for j in range(new_x, new_x + size_list[i][0]):
                    for k in range(new_y, new_y + size_list[i][1]):
                        new_xy.add((j, k))

                if new_xy & bad_xy <= set():
                    break

            for j in range(new_x, new_x + size_list[i][0] + 1):
                for k in range(new_y, new_y + size_list[i][1] + 1):
                    bad_xy.add((j, k))

            xy_list.append((new_x, new_y))

        return_list.reverse()
        for i, xy in enumerate(xy_list):
            return_list[i].update({'xy': xy_list[i]})

        return(return_list)
