# Webchat-Gemini-llamaindex-Fastapi
## Gemini
Google's Gemini LLM stands out as a multimodal maestro, excelling in understanding not just text, but also images, audio, and video. It boasts state-of-the-art performance, exceeding benchmarks in various tasks and offering advanced reasoning abilities. Choose from different tiers like Pro, Ultra, or even the experimental 1.5 Pro, and delve into its potential for generating text, translating languages, and tackling complex problems – all while its capabilities continue to evolve.
# How to run the Gemini on Colab ?
```bash
upload the gemini_llamaindex.ipynb file on your colab which is located in the <research> folder .
```
```bash
create a folder named "data" and upload your text file in that folder.
```
```bash
add your google api key.
```
```bash
Thats it! Run all the cell and get your answer.
```

# How to run the Chatbot on your local system?
### STEPS:

Clone the repository

```bash
https://github.com/Yashmori09/Webchat-Gemini-llamaindex-Fastapi.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv <folder path> <virtual env name>
```

```bash
<virtual env name>\Scripts\activate.bat
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
```bash
create a .env file and add your GOOGLE_API_KEY='Your key' in same format
```
```bash
# Finally run the following command
python -m uvicorn main:app --reload
```

Now,
```bash
open up you local host and port
```
