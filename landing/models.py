from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class LandingPage(Page):
    # Hero section fields
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Hero image for the landing page",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255,
        help_text="Hero text to display on the landing page"
    )

    # Content panels for the admin interface
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_image"),
                FieldPanel("hero_text"),
            ],
            heading="Hero section",
        ),
    ]

    template = "landing/landing_page.html"
