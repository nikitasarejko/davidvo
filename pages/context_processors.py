from .models import Page

def add_nav_links(request):
    nav_links = Page.objects.filter(is_in_navigation=True)

    return {
        "nav_links": nav_links
    }