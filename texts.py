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