from wagtail.blocks import (
    StreamBlock,
    StructBlock,
    ListBlock,
    URLBlock,
    CharBlock,
    TextBlock,
    BooleanBlock,
)
from wagtail.images.blocks import ImageBlock
from wagtail.blocks import ChoiceBlock


class TileBlock(StructBlock):
    title = CharBlock(
        required=False,
        max_length=100,
        label="Title",
        help_text="Optional title text"
    )
    description = TextBlock(
        required=False,
        label="Description",
        help_text="Optional description text"
    )
    text_on_hover = BooleanBlock(
        required=False,
        default=False,
        label="Show text only on hover",
        help_text="If checked, title and description will only appear on hover. "
                  "If unchecked, they will always be visible when present."
    )
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
    link = URLBlock(
        required=False,
        label="Link URL",
        help_text="Optional link when tile is clicked"
    )
    images = ListBlock(ImageBlock(required=True), label="Images", max_num=10)

    class Meta:
        icon = "image"
        template = "mosaic/blocks/tile_block.html"


class TilesStreamBlock(StreamBlock):
    tile_block = TileBlock(label="Mosaic Tile")
