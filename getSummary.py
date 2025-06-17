import requests
import os
import json
from pypdf import PdfReader

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
TEXT = []


def main():
    docs_dir = os.curdir+"/docs"
    for file in os.listdir(docs_dir):
        filename = os.fsdecode(file)
        readPdf(filename)
        send_request(filename)


def send_request(file_name):
    print("[...] SENDING REQUEST...")
    response = requests.post(
        url=API_URL,

        headers = {
            "Authorization" : f"Bearer {API_KEY}",
        },

        data = json.dumps({
            "model" : "deepseek/deepseek-chat:free",
            "messages" : [
                {
                    "role" : "user",
                    "content" : f"{TEXT}+\nProvide a summary as well as explenations of all the concepts for the provided material WITHOUT omitting any important details so it can be used to practice for exams, provide ONLY the summary with its explenations",
                }
            ],
        }),
    )

    response_parsed = response.json()["choices"][0]["message"]["content"]
    with open(f"summaries/{file_name}_summary.txt", "w", encoding="utf-8") as summaryFile:
        print(response_parsed, file=summaryFile)
    
    print("[+] SUMMARY WRITTEN AND IMAGES GENERATED TO FOLDER !")
    TEXT.clear()


def readPdf(file_name):
    print("[...] READING PDFS...")
    filedir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(filedir, f"docs/{file_name}")
    
    reader = PdfReader(filepath)
    
    for page in reader.pages:
        text = page.extract_text()
        TEXT.append(text)

        for count, image in enumerate(page.images):
            if not os.path.exists(f"{os.curdir}/img/{file_name.replace(".", "_")}"):
                os.makedirs(f"{os.curdir}/img/{file_name.replace(".", "_")}")
            with open(f"img/{file_name.replace(".", "_")}/{count}_{image.name}", "wb") as imgfile:
                imgfile.write(image.data)


if __name__ == "__main__":
    main()