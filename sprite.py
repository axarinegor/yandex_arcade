from pathlib import Path

import arcade
from attrs import frozen

from vector import Vector2Int

SPRITES_FOLDER = Path("data")


@frozen
class Sprite:
    @classmethod
    def load_raw_image(cls, path: Path | str, pivot: Vector2Int = Vector2Int.zero()) -> "Sprite":
        path = SPRITES_FOLDER / path
        if not path.exists():
            raise FileNotFoundError(
                f"❌ Спрайт не найден: '{path}'\n"
                f"Ожидалось: '{SPRITES_FOLDER}' содержит файлы изображений.\n"
                f"Текущая рабочая папка: {Path.cwd()}"
    )

        image = arcade.load_texture(path)
        return cls(image, Vector2Int(*image.size), pivot)

    _image: arcade.Texture
    _shape: Vector2Int
    _pivot: Vector2Int = Vector2Int.zero()

    @property
    def shape(self) -> Vector2Int:
        return self._shape

    def get(self) -> arcade.Texture:
        return self._image

    def blit_at(self, position: Vector2Int) -> None:
        screen_position = position - self._pivot
        arcade.draw_texture_rect(self._image, arcade.rect.XYWH(*screen_position.tuple, *self.shape.tuple))

    def with_pivot(self, pivot: Vector2Int) -> "Sprite":
        return Sprite(self._image, self._shape, pivot)

    def with_pivot_from_ratios(self, ratio_x: float, ratio_y: float) -> "Sprite":
        pivot_x = int(self.shape.x * ratio_x)
        pivot_y = int(self.shape.y * ratio_y)
        pivot = Vector2Int(pivot_x, pivot_y)

        return Sprite(self._image, self._shape, pivot)

    def reshape(self, shape: Vector2Int) -> "Sprite":
        pivot_x = int(self._pivot.x * (shape.x / self.shape.x))
        pivot_y = int(self._pivot.y * (shape.y / self.shape.y))
        pivot = Vector2Int(pivot_x, pivot_y)

        return Sprite(self._image, shape, pivot)

    def resize(self, ratio: float) -> "Sprite":
        shape = self.shape.scale_rounded(ratio)
        return self.reshape(shape)