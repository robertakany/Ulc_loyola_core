from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _


class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = _('Loyola site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = _('Loyola admin')

    # Text to put at the top of the admin index page.
    index_title = _('Administration')


admin.site.site_header = 'Loyola'
