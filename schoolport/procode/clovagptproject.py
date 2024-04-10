import requests
import uuid
import time
import json

api_url = 'https://ke2nxpisd9.apigw.ntruss.com/custom/v1/29650/883654b222243d4cf26e73008d4cede6516f34445504e6ff56e0c76b8adfc3f0/general'
secret_key = 'TFNoaXJ5SmRydWNPemhoSkxrdHd6RUNxakVtWHpwZGY='
image_file = ''

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000)),
    'lang' : 'ko'
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

result = response.json()
with open('result.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, indent="\t") 

#한글 깨짐 방지 코드 
with open('result.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, indent="\t", ensure_ascii=False)

#데이터 추출 코드
text = ""
for field in result['images'][0]['fields']:
    text += field['inferText']
    text += ' '
print(text)