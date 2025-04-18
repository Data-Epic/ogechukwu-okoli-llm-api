import os
import re
from groq import Groq
from dotenv import load_dotenv
import httpx
import logging

load_dotenv()
logging.basicConfig(filename="Educationalassistant.log", level=logging.DEBUG, format="%(asctime)s -- %(message)s")
class EducationalCustomerAssistant:
    def __init__(self, api_key, model_name="deepseek-r1-distill-llama-70b"):
        self.client = Groq(api_key=api_key)
        self.model = model_name
        self.chat_history = [
            {
                "role": "system",
                "content": (
                    "You are a knowledgeable and professional university education assistant. "
                    "Respond in a clear, concise, and confident tone. Do not include internal thoughts "
                    "or mention the user’s question. Just answer directly, based only on the current conversation."
                )
            }
        ]

    def get_user_input(self):
        return input("You: ")

    def clean_response(self, response):
        #function to remove <think> tags and their contents
        response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)

        #function to remove indirect references to the user’s question
        response = re.sub(r'\b(the user|user) (asked|said|wants to know|mentioned)[^\.]*\.?', '', response, flags=re.IGNORECASE)

        return response.strip()

    def chat(self, user_input):
        self.chat_history.append({"role": "user", "content": user_input})
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.chat_history,
                max_tokens=500,
                temperature=1.2
            )
            logging.info(f"API Response: {response}")

            reply = response.choices[0].message.content
            cleaned_reply = self.clean_response(reply)
            self.chat_history.append({"role": "assistant", "content": cleaned_reply})
            print("Assistant:", cleaned_reply)

            logging.info(f"Customer query: {user_input}")
            logging.info(f"Assistant: {cleaned_reply}")


        except httpx.HTTPStatusError as http_err:
            status = http_err.response.status_code
            print(f"HTTP error: {status}")
            if status == 401:
                print("Invalid API key. Exiting...")
                return False
            elif status == 404:
                print("Model not found.")
            elif status == 429:
                print("Rate limit exceeded.")
            else:
                print(f"Response text: {http_err.response.text}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return True

if __name__ == "__main__":
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("GROQ_API_KEY not found in environment variables.")
    else:
        assistant = EducationalCustomerAssistant(api_key)

        print("Hello i am your educational assisstant for today.\nHow may i be of help to you")
        while True:
            user_input = assistant.get_user_input()
            if user_input.lower() == "stop":
                break
            continue_chat = assistant.chat(user_input)
            if not continue_chat:
                break
