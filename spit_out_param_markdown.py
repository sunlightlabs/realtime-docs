# introspect the django rest framework
from api.serializers import *

from api.urls import router

# find all the apis
apis = []
for apimethod in router.registry: 
 apis.append({'url':apimethod[0], 'class':apimethod[1]})

outfile = "return_fragment.md"
fh = open(outfile, 'w')

# the classes are viewset classes
for a in apis:
 url = a['url']
 print "\n\nProcessing %s" % url
 fh.write("\n\n###%s return values\n" % (url))
 this_model = a['class'].serializer_class.Meta.model
 return_fields = a['class'].serializer_class.Meta.fields
 for r in return_fields:
  try: 
   field = this_model._meta.get_field_by_name(r)
   print "name: %s help_text: %s" % (field[0].name, field[0].help_text)
   fh.write("\n\n`%s` : %s" % (field[0].name, field[0].help_text))
  except:
   print "name: %s -- needs text" % (r)
   fh.write("\n\n`%s` : " % (r))
   
   
