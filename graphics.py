from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


# xy – Top left corner of the text.
# text – Text to be drawn. If it contains any newline characters, the text is passed on to multiline_text()
# fill – Color to use for the text.
# font – An ImageFont instance.
# spacing – If the text is passed on to multiline_text(), the number of pixels between lines.
# align – If the text is passed on to multiline_text(), “left”, “center” or “right”.







class Graphics:
    """Handles all image making things"""

    @classmethod
    def setup(cls, mode, size, color):
        cls.img = Image.new(mode, size, color)
        cls.draw = ImageDraw.Draw(cls.img)


    @classmethod
    def make_image(cls, options_list, file_name):
        for option in options_list:
            cls.draw.text(**option)
        cls.img.save(file_name)