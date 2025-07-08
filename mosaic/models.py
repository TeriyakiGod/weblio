from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from mosaic.blocks import TilesStreamBlock


class MosaicPage(Page):

    tiles = StreamField(
        TilesStreamBlock(),
        blank=True,
        help_text="Use this section to create a mosaic layout with images.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("tiles"),
    ]
