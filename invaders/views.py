from django.shortcuts import render_to_response
from django.utils import simplejson
#from django.core import serializers
from psi.invaders.models import Nodes, Edges

def data(request):
    nodes = []
    edges = []
    
    for node in Nodes.objects.all():
      nodes.append({
       "id": node.pk,
         "type": node.get_type_display(),
       "data": {
          "name": node.name,
          "desc": node.description,
       },
      })

    for edge in Edges.objects.all():
        edges.append([edge.src.pk, edge.dest.pk])
        
    response = {
      "nodes": nodes,
      "edges": edges,
    }

    #TODO: use django serializer 
    #  (find out why 'str' object has no attribute '_meta' error shows up)
    #  return HttpResponse(simplejson.dumps(response),
    # mimetype="application/json")

    return render_to_response('index.html', {"data": simplejson.dumps(response)});