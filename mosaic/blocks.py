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
    link = URLBlock(
        required=False,
        label="Link URL",
        help_text="Optional link when tile is clicked"
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
    image_change_interval = ChoiceBlock(
        choices=[
            ('2s', '2 seconds'),
            ('3s', '3 seconds'),
            ('4s', '4 seconds'),
            ('5s', '5 seconds'),
            ('7s', '7 seconds'),
            ('10s', '10 seconds'),
            ('15s', '15 seconds'),
            ('20s', '20 seconds'),
            ('30s', '30 seconds'),
            ('1m', '1 minute'),
            ('random:3-7', 'Random (3-7s)'),
            ('random:4-10', 'Random (4-10s)'),
            ('random:5-15', 'Random (5-15s)'),
            ('random:10-20', 'Random (10-20s)'),
            ('random:15-30', 'Random (15-30s)'),
            ('random:30-60', 'Random (30-60s)'),
        ],
        default='5s',
        label="Image Change Interval",
        help_text="How often the images change"
    )
    images = ListBlock(ImageBlock(required=True), label="Images", max_num=10)

    class Meta:
        icon = "image"
        template = "mosaic/blocks/tile_block.html"


class TilesStreamBlock(StreamBlock):
    tile_block = TileBlock(label="Mosaic Tile")
