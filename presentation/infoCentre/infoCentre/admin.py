from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.admin import AdminSite
from django.contrib import admin

from django.utils.translation import ugettext_lazy
from presentation.models import Kibana_frame
from presentation.models import Parent_frame
#,Parent_kibana_frame

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('GUCE')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Administration de l\'InfoCentre du GUCE')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('')
    #logout_template = "/logout"
#class FrameInline(admin.TabularInline):
#    model = Parent_kibana_frame
#    extra = 1

class KibanaFrameAdmin(admin.ModelAdmin):
    fields = ['code', 'description']
    list_display = ('code',  'description')
    #filter_horizontal = ('parents_frame',)
    search_fields = ['code']
    #inlines = [FrameInline]



class ParentFrameAdmin(admin.ModelAdmin):
    fields= ['code', 'nom', 'description','kibanas_frame']
    list_display = ('code','nom', 'description')
    search_fields = ['code']

    

admin_site = MyAdminSite(name='my_project_admin')

admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)

admin_site.register(Kibana_frame, KibanaFrameAdmin)
admin_site.register(Parent_frame,ParentFrameAdmin)

