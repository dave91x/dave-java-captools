
import re


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



def generate_uri_from_regex(uri):
  # "regex": "^/api/v1/batch-file/(?P<id>\\d+)/page/(?P<page>\\d+)/thumbnail/(?P<size>[^/]+)$",
  return uri


print generate_uri_from_regex("^/api/v1/batch-file/(?P<id>\\d+)/page/(?P<page>\\d+)/thumbnail/(?P<size>[^/]+)$")

