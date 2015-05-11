import re
import sys

# javadoc -d doc -private src/JavaCaptricityClient.java
# javadoc -d doc src/JavaCaptricityClient.java

d = { "a": 1, "b": 2, "c": 3}

print len(d)


sys.exit()

def param_typesetter(name):
    n = {'id': 'int', 'size': 'String'}
    if name == 'id' or re.search("_id", name):
        return n['id']
    else:
        return n.get(name, 'String')

def gen_param_list(params):
    final_params = []
    for p in params:
        b = param_typesetter(p) + " " + p
        final_params.append(b)
    return final_params

print "instance_set_id:  {}".format(param_typesetter("instance_set_id"))
print "id:  {}".format(param_typesetter("id"))
print "size:  {}".format(param_typesetter("size"))
print "bozo:  {}".format(param_typesetter("bozo"))

print
print

plist = ['id', 'instance_set_id', 'size', 'bozo']
print ", ".join(gen_param_list(plist))

# sys.exit()


# doc = "A list of batch files in the batch. See the batch file resource for an explanation of batch.\n    <p>The POST arguments are:</p>\n    <ul>\n        <li>batch (implicit): the batch is implied in the URL and is not required in the POST arguments.</li>\n        <li>file_name (optional): The name of this file. The name must be unique per batch. If not given, the name of the uploaded_file will be used.</li>\n        <li>uploaded_file: The file to be uploaded.</li>\n        <li>uploaded_with (optional): The method by which the file is uploaded. See the Batch File resource for explanation.</li>\n    </ul>"
#
#
# print doc
#
# print
#
# print len(doc)
#
# print
#
# lines = doc.splitlines()
#
# for line in lines:
#     print line.strip()



PARAM_BLOCKS = re.compile("(\(.*?\))")
PARAM_NAME = re.compile("<(.*?)>")
URI_CLEANUP = re.compile(' \+ "$')

def generate_uri_from_regex(uri):
  # "regex": "^/api/v1/batch-file/(?P<id>\\d+)/page/(?P<page>\\d+)/thumbnail/(?P<size>[^/]+)$",
  print uri
  param_list = []
  mod_uri = uri[1:-1]
  mod_uri = PARAM_BLOCKS.sub("_______", mod_uri)  # put 7 underscores in place of param blocks
  # param_setup.append()
  
  m = PARAM_BLOCKS.findall(uri)
  if m:
      # print len(m)
      for x in m:
          p = PARAM_NAME.search(x)
          if p:
              # print p.group(1)
              param_list.append(p.group(1))
  
  print param_list
  if len(param_list) > 0:
    for p in param_list:
      mod_uri = re.sub("_______", "\" + {} + \"".format(p), mod_uri, count=1)  # re.sub(pattern, repl, string, count=0, flags=0)
  
  mod2_uri = "https://shreddr.captricity.com" + mod_uri
  if URI_CLEANUP.search(mod2_uri):
    final_uri = URI_CLEANUP.sub("", mod2_uri)
  else:
    final_uri = mod2_uri + "\""
  
  return final_uri


x = generate_uri_from_regex("^/api/v1/batch-file/(?P<id>\\d+)/page/(?P<page>\\d+)/thumbnail/(?P<size>[^/]+)$")
print "String uri = \"" + x + ";\n"
print

y = generate_uri_from_regex("^/api/v1/batch-file/download/$")
print "String uri = \"" + y + ";\n"
print

z = generate_uri_from_regex("^/api/v1/batch-file/(?P<id>\\d+)/$")
print "String uri = \"" + z + ";\n"
print



