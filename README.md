# OCR과 LLM을 활용한 손코딩 이미지의 텍스트 포멧 변환 프로젝트

>OCRproject Made With ClovaOCR && ChatGPT

## 서론
 평소 파이썬과 여러가지 엔진들을 다뤄보며 공부하다가 컴퓨터가 없는 상황에서 코드를 작성할 없기 때문에 코딩 공부를 하기가 어렵다는 점이 있었다. 하지만 이동을 하거나 자투리 시간에 컴퓨터를 사용하지 않고도 언제 어느 상황에서든 공부를 할 수 있도록 하고 싶었다. 따라서 컴퓨터가 없는 상황이나 키보드가 없는 상황, 복사를 하고 싶지만 하지 못하는 상황 등 여러가지 코드를 실행할 수 없는 상황에 손코딩을 사진으로 찍거나 아니면 코딩된 것을 캡쳐하여, 실행 할 수 있는 코드로 인식 및 변환해주는 프로그램이 있으면 좋겠다고 생각해서 개발에 도전해보았다.

## 본론
 이번 프로젝트에서는 상기 아이디어를 구현하기 위해서 ‘OCR’과 ‘LLM을 통한 문장 생성 및 교정’ 기술을 사용했다. 먼저 손코딩을 사진으로 찍으면 그 사진 속의 손코딩 텍스트를 검출하는 기능이 필요하다. 이는 텍스트 이미지를 기계가 읽을 수 있는 텍스트 포맷으로 변환하는 광학 문자 인식(OCR) 기술을 통해서 구현할 수 있다. 하지만 OCR을 통해서 이미지를 검출한다고 해도 OCR은 단순히 텍스트만을 검출하기 때문에 문장을 형성하는 칸, 줄, 맥락을 고려할 수 없었다. 따라서 OCR을 통해 검출한 텍스트를 실제 작동 가능한 코드로 재구성하기 위해서는 코딩이라는 특수한 맥락을 고려해서 텍스트를 재구성 및 교정할 필요성이 존재했고 이를 대표적인 LLM인 ChatGPT4를 활용해서 해결해보았다.

### 1. OCR

1-1. OCR이란?
 광학 문자 인식(OCR)은 텍스트 이미지를 기계가 읽을 수 있는 텍스트 포맷으로 변환하는 기술을 말한다. 예를 들어 양식 또는 영수증을 스캔하는 경우 컴퓨터는 스캔본을 이미지 파일로 저장한다. 이미지 파일에서는 텍스트 편집기를 사용하여 단어를 편집, 검색하거나 단어 수를 계산할 수 없다. 그러나 OCR을 사용하면 이미지를 텍스트 문서로 변환하여 내용을 텍스트 데이터로 저장할 수 있다.

1-2 손코딩 OCR 적용(네이버 클로바 사용)
사진
### 2. LLM
2-1. LLM(Large Language Model)이란?
 LLM은 언어의 구조와 문법을 이해하고, 주어진 문맥 속에서 다음 단어나 문장을 생성하는 등의 자연어 처리 작업을 수행하는 대규모 인공지능 모델을 뜻한다. 이러한 모델들은 방대한 양의 텍스트 데이터로 훈련되어, 다양한 질문과 프롬프트에 대해 일관되며 맥락에 부합한 응답을 생성할 수 있다. LLM의 주요 특징은 그들의 크기와 대량의 언어 데이터로부터 학습할 수 있는 능력이다. 고급 딥러닝 기술을 활용함으로써, LLM은 패턴을 분석하고 의미를 추출하며, 놀라운 정확도로 인간과 유사한 텍스트를 생성할 수 있다. LLM은 언어 번역, 전체 텍스트 생성 및 요약, 감정 분석, 그리고 질문-답변 시스템에서 뛰어난 성능을 보이며 우리가 알고 있는 ChatGPT 또한 이러한 LLM의 한 종류이다.


2-2. ChatGPT
 ChatGPT란 OpenAI가 개발한 GPT기반의  대형 언어 모델(large language model, LLM) 챗봇을 말한다. ChatGPT는 대화 형태로 상호작용을 하며 놀라울 정도로 인간과 대화하는 것과 같은 반응을 제공하는 능력을 가지고 있다. ChatGPT는 인간 피드백형 강화학습 (Reinforcement Learning Human Feedback, RLHF)을 사용하는데, 이는 사용자의 지시를 따르고 만족스러운 반응을 생성하는 능력을 만들기 위해 인간 피드백을 사용하는 추가 훈련 계층이다. 대형 언어 모델(LLM)은 문장의 일련의 단어로 다음 단어를 예측하고 다음 문장을 예측한다. 이 기능을 통해 사용자들은 단락 뿐만 아니라 여러 페이지의 콘텐츠를 작성할 수 있다. 따라서 이번 프로젝트에서는 LLM 중 가장 성능이 좋은 Chat GPT 4를 활용해 CLOVA OCR을 통해서 추출한 손코딩 정보를, 코딩이라는 맥락을 고려해 새로운 코딩 블록 형태로으로  재구성해보았다.

ChatGPT4 Prompt Engineering 예시

1. 파이썬 코딩처럼 생긴 단어를 나열해서 너에게 줄게
2. 제공받은 글자를 코딩 문맥을 고려해서 실제 작동할 수 있는 파이썬 코드로 변환해서 줘
3. 그런데 변환 과정에서 실제 코드를 실행했을 때 오류가 나거나 오타인 것 같은 글자는 너가 바꿔서 줘



예시 사진


## 결론 
 리서치를 통해 여러 기술을 탐색하고 이를 조합하여 문제를 해결하기 위해 코드를 직접 구현해보았다. 이 과정에서 OCR과 LLM에 대한 학습을 통해 IT 기술을 활용하여 현실의 문제를 해결하는 능력을 키울 수 있었다. 또한, 복잡한 문제를 해결할 때는 Divide and Conquer 방식을 통해 큰 문제를 작은 단위로 분해하여 해결하고, 이를 통합해 나가는 과정에서의 중요한 노하우를 배울 수 있었다.
 
