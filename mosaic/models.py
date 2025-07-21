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

    def get_context(self, request):
        context = super().get_context(request)
        
        # Add the selected content page to the context
        if self.content_page:
            selected_page = self.content_page.specific
            context['selected_page'] = selected_page
            context['selected_page_template'] = selected_page.get_template(request)
        else:
            context['selected_page'] = None
            context['selected_page_template'] = None
            
        return context
