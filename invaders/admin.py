from django.contrib import admin
from psi.invaders.models import Nodes, Edges

#def set_node_as_person(modeladmin, request, queryset):
#    queryset.update(type=1)
#    set_node_as_person.short_description="Mark as people"
    

class NodesAdmin(admin.ModelAdmin):
    list_display = ('type', 'icon', 'name', 'description')
    search_fields = ('type', 'name', 'description')

#    actions = [set_node_as_person]

class EdgesAdmin(admin.ModelAdmin):
    list_display = ('src', 'dest', 'edge_types', '__unicode__')
    
    class Meta:
        verbose_name_plural = "Edges"
    

admin.site.register(Nodes, NodesAdmin)
admin.site.register(Edges, EdgesAdmin)
