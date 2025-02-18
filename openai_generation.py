import json
import os
from urllib import response
import openai
import requests
import re
# from openai import OpenAI
import openai
import time
from nltk.tokenize import word_tokenize
import base64
from mimetypes import guess_type



def openai_generate(input_prompt, model="gpt-3.5-turbo-1106", temperature=1, max_tokens=4090):
    print(f"model: {model}")
    API_KEY = ""  # Your key


    if model == "chatgpt":
        model = "gpt-3.5-turbo"
    elif model == "gpt4":
        response = "gpt-4"

    for _ in range(5):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": input_prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=1,
                # frequency_penalty=0,
                # presence_penalty=0,
                api_key=API_KEY,
                # api_base = API_BASE
            )
            break
        except Exception as e:
            print(["[OPENAI ERROR]: ", e])
            response = None
            time.sleep(5)
    if response != None:
    # print(response)
        response = response.choices[0].message.content
    return response
   

# Function to encode a local image into data URL 
def local_image_to_data_url(image_path):
    # Guess the MIME type of the image based on the file extension
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if none is found

    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"

    