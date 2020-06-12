from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.admin import AdminSite
from django.contrib import admin

from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('GUCE')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Administration de l\'InfoCentre du GUCE')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('')
    #logout_template = "/logout"
admin_site = MyAdminSite(name='my_project_admin')
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)
