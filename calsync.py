import os, requests, shutil

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
filename = os.path.basename(url)

data = requests.get(url, auth=(username, password), stream=True)
with open('/tmp/'+filename, 'wb') as f:
    data.raw.decode_content = True
    shutil.copyfileobj(data.raw, f)