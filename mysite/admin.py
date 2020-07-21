'''from django.contrib import admin
from .models import Usuario, Perfil, UsuarioPossuiPerfil

class PerfilInline(admin.TabularInline):
    model = UsuarioPossuiPerfil
    extra = 1

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (PerfilInline,)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Perfil)
admin.site.register(UsuarioPossuiPerfil)
'''
