from django.db import models
from django.db.models import TextField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable

from main.pages.medicine import MedicinePage
from main.shared_modules.pagination import generate_pages


class PrescriptionPage(Page):
    eng_name = TextField(verbose_name='英文名', default='')
    usage = RichTextField(verbose_name='用法', default='')
    function = RichTextField(verbose_name='功用', default='')
    cures = RichTextField(verbose_name='主治', default='')

    mandatory_panels = [
        FieldPanel('eng_name'),
        InlinePanel('composition', label='组成'),
        FieldPanel('usage'),
        FieldPanel('function'),
        FieldPanel('cures')
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(mandatory_panels, 'body')
    ]

    @property
    def get_composition_list(self):

        composition_list = []

        for composition in self.specific.composition.all():
            composition_list.append(composition.medicine_page.title)

        return composition_list


class PrescriptionComposition(Orderable):
    page = ParentalKey(PrescriptionPage, on_delete=models.CASCADE, related_name='composition')
    medicine_page = models.ForeignKey(
        MedicinePage,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel('medicine_page')
    ]


class PrescriptionHomePage(Page):

    subpage_types = [
        PrescriptionPage
    ]

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)

        all_items = self.get_children()

        context['pages'] = generate_pages(request, all_items)

        return context
