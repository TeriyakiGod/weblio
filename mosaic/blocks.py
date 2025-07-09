from wagtail.blocks import (
    StreamBlock,
    StructBlock,
    ListBlock,
)
from wagtail.images.blocks import ImageBlock


class TileBlock(StructBlock):
    images = ListBlock(ImageBlock(required=True), label="Images", max_num=10)

    class Meta:
        icon = "image"
        template = "mosaic/blocks/tile_block.html"


class TilesStreamBlock(StreamBlock):
    tile_block = TileBlock(label="Mosaic Tile")
