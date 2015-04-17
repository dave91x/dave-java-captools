import os
import re
import json

ct = 0
spt_ct = 0
script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "schema.json"
abs_file_path = os.path.join(script_dir, rel_path)
schema_file = open(abs_file_path, 'r')
schema = json.load(schema_file)
output_file_path = os.path.join(script_dir, "../src/JavaCaptricityClient.java")
jfile = open(output_file_path, 'w')

REMOVE_SPACES_RE = re.compile(r"\s+")

def make_method_name(display_name):
  return REMOVE_SPACES_RE.sub("", display_name)

def generate_uri_from_regex(uri):
  return uri

print abs_file_path
print schema['name']
print schema['endpoint']
print "Version:  " + schema['version']
print output_file_path

jfile.write("package com.captricity.api;\n")
jfile.write("\n")
jfile.write("import java.io.File;\n")
jfile.write("import org.apache.http.Header;\n")
jfile.write("import org.apache.http.HttpEntity;\n")
jfile.write("import org.apache.http.entity.StringEntity;\n")
jfile.write("import org.apache.http.client.methods.CloseableHttpResponse;\n")
jfile.write("import org.apache.http.client.methods.HttpGet;\n")
jfile.write("import org.apache.http.client.methods.HttpPost;\n")
jfile.write("import org.apache.http.client.methods.HttpDelete;\n")
jfile.write("import org.apache.http.impl.client.CloseableHttpClient;\n")
jfile.write("import org.apache.http.impl.client.HttpClients;\n")
jfile.write("import org.apache.http.entity.mime.MultipartEntityBuilder;\n")
jfile.write("import org.apache.http.util.EntityUtils;\n")
jfile.write("import org.json.*;\n")
jfile.write("\n")
jfile.write("public class JavaCaptricityClient {\n")
jfile.write("  \n")
jfile.write("  private String apiToken;\n")
jfile.write("  \n")
jfile.write("  public CaptricityClient(String token) {\n")
jfile.write("    apiToken = token;\n")
jfile.write("  }\n")
jfile.write("  \n")
jfile.write("  private JSONArray makeGetArrayCall(String target) throws Exception {\n")
jfile.write("    CloseableHttpClient client = HttpClients.createDefault();\n")
jfile.write("    try {\n")
jfile.write("      HttpGet getRequest = new HttpGet(target);\n")
jfile.write("      getRequest.addHeader(\"Captricity-API-Token\", apiToken);\n")
jfile.write("      \n")
jfile.write("      CloseableHttpResponse response = client.execute(getRequest);\n")
jfile.write("      HttpEntity entity = response.getEntity();\n")
jfile.write("      if (entity != null) {\n")
jfile.write("        String json_string = EntityUtils.toString(entity);\n")
jfile.write("        return new JSONArray(json_string);\n")
jfile.write("      }\n")
jfile.write("    \n")
jfile.write("    } catch (Exception e) {\n")
jfile.write("      e.printStackTrace();\n")
jfile.write("    } finally {\n")
jfile.write("      client.close();\n")
jfile.write("    }\n")
jfile.write("    return new JSONArray();\n")
jfile.write("  }\n")
jfile.write("  \n")
jfile.write("  private JSONObject makeGetObjectCall(String target) throws Exception {\n")
jfile.write("    CloseableHttpClient client = HttpClients.createDefault();\n")
jfile.write("    try {\n")
jfile.write("      HttpGet getRequest = new HttpGet(target);\n")
jfile.write("      getRequest.addHeader(\"Captricity-API-Token\", apiToken);\n")
jfile.write("      \n")
jfile.write("      CloseableHttpResponse response = client.execute(getRequest);\n")
jfile.write("      HttpEntity entity = response.getEntity();\n")
jfile.write("      if (entity != null) {\n")
jfile.write("        String json_string = EntityUtils.toString(entity);\n")
jfile.write("        return new JSONObject(json_string);\n")
jfile.write("      }\n")
jfile.write("    \n")
jfile.write("    } catch (Exception e) {\n")
jfile.write("      e.printStackTrace();\n")
jfile.write("    } finally {\n")
jfile.write("      client.close();\n")
jfile.write("    }\n")
jfile.write("    return new JSONObject();\n")
jfile.write("  }\n")
jfile.write("  \n")


resources = schema['resources']

for r in resources:
  ct += 1
  
  if r['supported']:
    spt_ct += 1
    print "%s" % r['display_name']
    # print "%s:  %s" % (r['display_name'] , r['doc'])
    allowed_methods = r['allowed_request_methods']
    print "Allowed methods:  %s" % ", ".join(allowed_methods)
    print
    
    if 'GET' in allowed_methods:
      if r['is_list']:
        # do makeGetArrayCall
        jfile.write("  public JSONArray get" + make_method_name(r['display_name']) + "() throws Exception {\n")
        jfile.write("    String uri = \"https://shreddr.captricity.com/api/v1/\";\n")
        jfile.write("    JSONArray response = makeGetArrayCall(uri);\n")
      else:
        # do makeGetObjectCall
        jfile.write("  public JSONObject get" + make_method_name(r['display_name']) + "() throws Exception {\n")
        jfile.write("    String uri = \"https://shreddr.captricity.com/api/v1/\";\n")
        jfile.write("    JSONObject response = makeGetObjectCall(uri);\n")
      jfile.write("    return response;\n")  
      jfile.write("  }\n")
      jfile.write("  \n")
    
    if 'DELETE' in allowed_methods:
      

print
print "Total number of endpoints:  %s" % ct
print "Total number of supported endpoints:  %s" % spt_ct


# public JSONArray showBatches() throws Exception {
#   String batchesUri = "https://shreddr.captricity.com/api/v1/batch/";
#   JSONArray response = makeGetArrayCall(batchesUri);
#   return response;
# }

jfile.write("}\n")

schema_file.close()
jfile.close()
