from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'ULC_loyola_core.admin.MyAdminSite'
