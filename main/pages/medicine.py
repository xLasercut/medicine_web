from django.db import models
from django.db.models import TextField
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image

from main.shared_modules.pagination import generate_pages


class MedicinePage(Page):
    latin_name = TextField(verbose_name='拉丁名', default='')
    eng_name = TextField(verbose_name='英文名', default='')
    category = TextField(verbose_name='类别', default='')
    origin = RichTextField(verbose_name='来源', default='')
    production_region = RichTextField(verbose_name='产地', default='')
    features = RichTextField(verbose_name='性状', default='')
    quality_requirements = RichTextField(verbose_name='品质', default='')
    properties = RichTextField(verbose_name='性味', default='')
    functions = RichTextField(verbose_name='功效', default='')
    image = models.ForeignKey(
        Image,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    mandatory_panels = [
        FieldPanel('latin_name'),
        FieldPanel('eng_name'),
        FieldPanel('category'),
        FieldPanel('origin'),
        FieldPanel('production_region'),
        FieldPanel('features'),
        FieldPanel('quality_requirements'),
        FieldPanel('properties'),
        FieldPanel('functions'),
        ImageChooserPanel('image')
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(mandatory_panels, 'body')
    ]


class MedicineHomePage(Page):
    subpage_types = [
        MedicinePage
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        all_items = self.get_children()

        context['pages'] = generate_pages(request, all_items)

        return context
