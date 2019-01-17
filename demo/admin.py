from django.contrib import admin

from demo.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cliente, ClienteAdmin)
