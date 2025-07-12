from wagtail.blocks import (
    StreamBlock,
    StructBlock,
    ListBlock,
)
from wagtail.images.blocks import ImageBlock
from wagtail.blocks import ChoiceBlock


class TileBlock(StructBlock):
    images = ListBlock(ImageBlock(required=True), label="Images", max_num=10)
    transition = ChoiceBlock(
        choices=[
            ('fade', 'Fade'),
            ('slide-left', 'Slide Left'),
            ('slide-right', 'Slide Right'),
            ('slide-up', 'Slide Up'),
            ('slide-down', 'Slide Down'),
            ('flip-x', 'Flip X'),
            ('flip-y', 'Flip Y'),
        ],
        default='fade',
        label="Transition Effect"
    )

    class Meta:
        icon = "image"
        template = "mosaic/blocks/tile_block.html"


class TilesStreamBlock(StreamBlock):
    tile_block = TileBlock(label="Mosaic Tile")
