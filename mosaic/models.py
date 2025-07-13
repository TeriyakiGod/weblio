from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from django.db import models
from mosaic.blocks import TilesStreamBlock


class MosaicPage(Page):

    content_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    layout = models.CharField(
        max_length=13,
        choices=[
            ('content-left', 'Content Left'),
            ('content-right', 'Content Right'),
        ],
        default='content-left',
        help_text="Choose the layout for the mosaic page."
    )
    tiles = StreamField(
        TilesStreamBlock(),
        blank=True,
        help_text="Use this section to create a mosaic layout with images.",
    )

    content_panels = Page.content_panels + [
        PageChooserPanel("content_page"),
        FieldPanel("layout"),
        FieldPanel("tiles"),
    ]
