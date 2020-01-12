from wagtail.core.models import Page

from main.pages.medicine import MedicineHomePage, MedicinePage
from main.pages.prescription import PrescriptionHomePage, PrescriptionPage


class HomePage(Page):
    subpage_types = [
        MedicineHomePage,
        PrescriptionHomePage
    ]
