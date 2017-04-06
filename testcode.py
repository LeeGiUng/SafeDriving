#! /usr/bin/env python
########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '5ad85aabd47e44e0985c480d12b5b1ba',
}

params = urllib.urlencode({
    
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTeLsFoypwWt3WcoSdnwZ2E5MA1nNx7HOcExOudfnRWO5jVPYkkjw' }"

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
