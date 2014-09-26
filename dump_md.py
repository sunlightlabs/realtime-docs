# script for spitting out markdown dox from the iodocs stuff. 

import json

infile = "public/data/realtime.json"
outfile = "doc_fragment.md"

fh = open(outfile, 'w')

result = json.load(open(infile,'r'))

for endpoint in result['endpoints']:
    name = endpoint['name']
    #fh.write("###%s\n" % (name))
    
    methods = endpoint['methods']
    for method in methods:
        fh.write("\n##%s\n" % (method['URI']) )
        fh.write("%s \n" % (method['Synopsis']) )
        fh.write("\n###Parameters\n")
        
        for parameter in method['parameters']:
            fh.write("\n\n`%s` : %s" % (parameter['Name'], parameter['Description']))
    
    fh.write("\n")
             