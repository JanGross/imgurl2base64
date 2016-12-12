import requests, base64, sys  
from io import BytesIO

try:  
    url=sys.argv[1]
except IndexError:  
    url="https://i.stack.imgur.com/r390N.png"

buffered = BytesIO(requests.get(url).content)  
img_base64 = base64.b64encode(buffered.getvalue())  
print(img_base64.decode())  
