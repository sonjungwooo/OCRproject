# OCR과 LLM을 활용한 손코딩 이미지의 텍스트 포멧 변환 프로젝트

>Snap, Convert, Run: Automated Code Digitization via Clova OCR & GPT-4
>>Paper2Code

## Introduction
 While studying Python and exploring various engines, I often ran into a frustrating limitation: it is difficult to practice coding when you don't have access to a computer. I wanted to find a way to study anytime, anywhere—whether I was commuting, taking a break, or stuck in a situation without a keyboard, a computer, or the ability to copy text. Whenever I couldn't run code directly, I found myself wishing for a tool that could take a photo or screenshot of handwritten or uncopyable code and instantly convert it into an executable format. Driven by this idea, I decided to take on the challenge of developing this program.

## Main Body
 To bring this idea to life, I utilized **OCR (Optical Character Recognition)** and **LLM-based text generation and correction technologies**.

 First, when a photo of handwritten code is taken, the system needs to detect the text within the image. This is achieved using OCR technology, which converts image-based text into a machine-readable format. However, OCR alone has limitations; it merely detects raw text without understanding line breaks, spacing, or the broader context of the sentences. To bridge this gap and reconstruct the OCR output into actual, working code, I needed a way to account for the unique context of programming. I solved this by leveraging **ChatGPT-4**, a leading Large Language Model (LLM).

### 1. OCR

1-1. What is OCR?
 OCR is a technology that converts text images into machine-readable text formats. For example, when scanning forms or receipts, computers typically save the scans as image files, which do not allow users to edit, search, or count words using a text editor. However, OCR transforms these images into text documents, allowing the contents to be stored as usable text data.

1-2. Applying OCR to Handwritten Code (Using NAVER Clova)
(Insert Photo Here)

### 2. LLM
2-1. What is an LLM (Large Language Model)?
 An LLM is a large-scale AI model designed to understand language structure and grammar while performing natural language processing tasks, such as predicting the next word or generating sentences within a given context. Trained on massive amounts of text data, these models can generate coherent, context-aware responses to various questions and prompts. The defining characteristics of LLMs lie in their scale and their ability to learn from vast linguistic datasets. By leveraging advanced deep learning techniques, LLMs can analyze patterns, extract meaning, and generate human-like text with remarkable accuracy. They excel in language translation, full-text generation, summarization, sentiment analysis, and Q&A systems. ChatGPT is one such prominent example of an LLM.

2-2. ChatGPT
 ChatGPT is a GPT-based large language model (LLM) chatbot developed by OpenAI. It interacts in a conversational format, offering surprisingly human-like responses. ChatGPT utilizes RLHF (Reinforcement Learning from Human Feedback), an additional training layer that incorporates human feedback to align the model with user instructions and ensure satisfying outputs. LLMs operate by predicting subsequent words and sentences based on a sequence of tokens, empowering users to write everything from short paragraphs to multi-page documents.

 Therefore, in this project, I used ChatGPT-4—one of the most powerful LLMs available—to take the handwritten code extracted by Clova OCR and reconstruct it into structured, executable code blocks by factoring in the context of programming.

***ChatGPT-4 Prompt Engineering Example:***

“I will provide you with a list of words that look like Python code.”

“Please convert these given characters into actual, executable Python code, taking programming context into account.”

“If you notice any typos or syntax errors that would cause the code to fail during execution, please correct them proactively.”

(Insert Example Photo Here)


## Conclusion
 Through this research, I explored various technologies and combined them to build a functional solution to a real-world problem. By learning how to work with OCR and LLMs, I strengthened my ability to leverage IT technologies to solve practical challenges. Furthermore, I learned the importance of the "Divide and Conquer" approach when tackling complex problems—breaking a massive challenge down into smaller, manageable units and seamlessly integrating them into a final solution.


``` 
+-------------------+      +-------------------+      +-----------------------+      +--------------------+
|  Input Image      | ---> |  Naver Clova OCR  | ---> |  GPT-4 Prompt Engine  | ---> |  Executable Code   |
| (Handwritten Code)|      | (Text Extraction) |      | (Context Correction)  |      |  (Python Syntax)   |
+-------------------+      +-------------------+      +-----------------------+      +--------------------+
```


