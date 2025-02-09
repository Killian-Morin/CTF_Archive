import requests
import http.client as http_client
import logging
from print_color import print

http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Server URL: http://chals.bitskrieg.in:3009/
# Endpoints:
# 	POST /qchannel - Initialize quantum channel
# 	GET /entangle - Generate authentication token
# 	POST /qproc - Process quantum WASM modules
# 	GET /vault/{something} - Restricted flag storage

baseUrl = "http://chals.bitskrieg.in:3009/"

r = requests.get(baseUrl + "entangle")

token = r.text#.removeprefix('{').removesuffix('}')

print(token, color='blue')

r = requests.post(baseUrl + "qproc", data=token)

print(r, r.text)
