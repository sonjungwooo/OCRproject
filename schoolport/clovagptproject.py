import requests
import uuid
import time
import json
from openai import OpenAI

api_url = ''
secret_key = ''
client = OpenAI(api_key='')
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

#데이터 추출 코드
text = ""
for field in result['images'][0]['fields']:
    text += field['inferText']
    text += ' '

#chatgpt 호출 및 실행
guide = "내가 코드를 한줄로 보낼거야 그러면 너가 이 코드를 실제 실행할 수 있는 코드블록 형태로 바꿔서 나한테 보내줄래?"
prompt_text = guide + "code : " + text
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content":prompt_text},
  ],
  max_tokens=1000
)

result = response.choices[0].message.content
print(result)