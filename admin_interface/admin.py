from django.contrib import admin
from admin_interface.models import *

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Research_paper)
admin.site.register(RequestLog)
admin.site.register(IssuedLog)

