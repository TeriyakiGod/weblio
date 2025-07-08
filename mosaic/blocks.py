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

    def get_admin_display_title(self, value):
        image_count = len(value.get('images', []))
        if image_count == 1:
            return f"Mosaic Tile ({image_count} image)"
        return f"Mosaic Tile ({image_count} images)"


class TilesStreamBlock(StreamBlock):
    tile_block = TileBlock(label="Mosaic Tile")
