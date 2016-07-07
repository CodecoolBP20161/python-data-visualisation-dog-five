from datamanager import DataManager
from graphics import Graphics
from PIL import ImageFont

import datetime

#function creates dict list for graphics.py
class DueDate:
    """This class will handle all DueDate stuff"""
    @classmethod
    def time_converter(cls, data_list):
        """Returns the delta to today in oordinal time"""
        new_list = [(x[0], (x[1] - datetime.datetime.now().date()).days) for x in data_list]
        return(new_list)

    @classmethod
    def make_dict(cls, new_list):
        return_list = []
        for i, elem in enumerate(new_list):
            return_list.append({
                                'xy': (0, i*20),
                                'fill': (111, 111, 111, 1),
                                'font': ImageFont.truetype("SourceSansPro-Regular.otf", 16),
                                'text': str(new_list[i][0])
                                })
        return(return_list)
