import json

ct = 0
spt_ct = 0
jfile = open("./schema.json", 'r')
schema = json.load(jfile)

print schema['name']
print schema['endpoint']
print schema['version']

resources = schema['resources']

for r in resources:
    ct += 1
    if r['supported']:
        spt_ct += 1
        print "%s:  %s" % (r['display_name'], r['doc'])
        print "Allowed methods:  %s" % ", ".join(r['allowed_request_methods'])
        print

print
print "Total number of endpoints:  %s" % ct
print "Total number of supported endpoints:  %s" % spt_ct




