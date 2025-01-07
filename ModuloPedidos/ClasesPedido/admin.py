from django.contrib import admin
from .models import Mesero,PersonalCocina,Cliente,ItemPedido,Pedido,Historial,Restaurante,Plato,Menu,Mesa,RegistroHistorico
# Register your models here
class MeseroAdmin(admin.ModelAdmin):
    list_display = ('nombre','cedula','telefono','identificacion','esta_ocupado')
    list_editable = ('cedula','telefono')
admin.site.register(Mesero,MeseroAdmin)
class PersonalCocinaAdmin(admin.ModelAdmin):
    list_display = ('nombre','cedula','telefono','identificacion','esta_cocinando')
    list_editable = ('cedula','telefono')
admin.site.register(PersonalCocina, PersonalCocinaAdmin)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','cedula','telefono','direccion','historial','mesa')
    list_editable = ('cedula','telefono','direccion')
admin.site.register(Cliente,ClienteAdmin)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido','cliente','plato','cantidad','observacion')
    list_editable = ('plato','cantidad','observacion')
admin.site.register(ItemPedido,ItemPedidoAdmin)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero','cliente','fecha_actual','informacion','mesa','estado')
    list_editable = ('mesa','estado')
admin.site.register(Pedido,PedidoAdmin)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id','cliente')
admin.site.register(Historial,HistorialAdmin)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre','registro_historico','menu')
    list_editable = ('menu',)
admin.site.register(Restaurante,RestauranteAdmin)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio')
    list_editable = ('precio',)
admin.site.register(Plato,PlatoAdmin)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(Menu,MenuAdmin)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero','capacidad','disponible')
    list_editable = ('capacidad',)
admin.site.register(Mesa,MesaAdmin)
class RegistroHistoricoAdmin(admin.ModelAdmin):
    list_display = ('id','restaurante')
admin.site.register(RegistroHistorico,RegistroHistoricoAdmin)
