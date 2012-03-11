from django.db import models

class Nodes(models.Model):
    TYPE_CHOICES = (
      (1, u'Person'),
      (2, u'Project'),
      (3, u'Collective'),
    )
    
    type = models.PositiveIntegerField(choices=TYPE_CHOICES, blank = True, null = True)
    icon = models.ImageField(upload_to='psi_alpha_icons', blank = True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank = True)

    def __unicode__(self):
      return self.name

class Edges(models.Model):
    src = models.ForeignKey(Nodes,related_name='src')
    dest = models.ForeignKey(Nodes,related_name='dest')

    def edge_types(self):
      return '%s - %s' % (self.src.get_type_display(), self.dest.get_type_display())
  
    def __unicode__(self):
      return '%s - %s' % (self.src.name, self.dest.name)

