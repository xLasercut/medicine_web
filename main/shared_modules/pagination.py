from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def generate_pages(request, all_items, items_per_page=10):
    paginator = Paginator(all_items, items_per_page)

    page = request.GET.get('page')

    try:
        # If the page exists and the ?page=x is an int
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If the ?page=x is not an int; show the first page
        pages = paginator.page(1)
    except EmptyPage:
        # If the ?page=x is out of range (too high most likely)
        # Then return the last page
        pages = paginator.page(paginator.num_pages)

    return pages
