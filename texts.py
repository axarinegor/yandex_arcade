import arcade
import pyglet

# Обычный пиксельный шрифт - Digital Upscaled Pixel
pyglet.font.add_file("data/Pixel_fonc.otf")
pixel_font = "Digital Upscaled Pixel"
BIG_SIZE = 30
MEDIUM_SIZE = 22
SMALL_SIZE = 16

LEVEL_1 = [arcade.Text(
            text="Управление",
            x=380,
            y=500,
            color=arcade.color.BLACK,
            font_size=MEDIUM_SIZE,
            font_name=pixel_font,
            bold=True
           ), 
            arcade.Text(
            text="A/D - Вперёд/Назад",
            x=380,
            y=435,
            color=arcade.color.BLACK,
            font_size=SMALL_SIZE,
            font_name=pixel_font
           ), 
            arcade.Text(
            text="SPACE - Прыжок",
            x=380,
            y=370,
            color=arcade.color.BLACK,
            font_size=SMALL_SIZE,
            font_name=pixel_font
           )]


LEVEL_2 = [arcade.Text(
            text="Прыжок веры",
            x=380,
            y=400,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]


LEVEL_4 = [arcade.Text(
            text="Углы",
            x=250,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]


LEVEL_12 = [arcade.Text(
            text="Как зовут создателя?",
            x=200,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]

LEVEL_7 = [arcade.Text(
            text="Темнота",
            x=400,
            y=500,
            color=arcade.color.BLACK,
            font_size=BIG_SIZE,
            font_name=pixel_font,
            bold=True
           )]