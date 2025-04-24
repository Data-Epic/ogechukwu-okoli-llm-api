# importing necessary libraries for my script
import os
import re
from groq import Groq
from dotenv import load_dotenv # loading api-key
import httpx # library for handling errors
import logging # library for handling logs

load_dotenv()
logging.basicConfig(filename="Educationalassistant.log", level=logging.DEBUG, format="%(asctime)s -- %(message)s") # cration of the log file as well as appending the message request to groq api
class EducationalCustomerAssistant:# class for main script building named Educationalcuatomerassistant
    def __init__(self, api_key, model_name="deepseek-r1-distill-llama-70b"):#initializaing instances ; api_key and llm model
        self.client = Groq(api_key=api_key)
        self.model = model_name
        self.chat_history = [  # chat history is a list describing system content as university application assistant
            {
                "role": "system", # system role
                "content": ( # content
                    "You are a knowledgeable and professional university education assistant. "
                    "Respond in a clear, concise, and confident tone. Do not include internal thoughts "
                    "or mention the user’s question. Just answer directly, based only on the current conversation."
                )
            }
        ]
    #   function for getting user input described as "You"
    def get_user_input(self):
        return input("You: ") # outputting You
    # cleaning customer response to remove <think> and user using re.sub which substitutes <think> with ""(nothing) an empty string
    def clean_response(self, response):
        #function to remove <think> tags and their contents
        response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)

        #function to remove indirect references to the user’s question
        response = re.sub(r'\b(the user|user) (asked|said|wants to know|mentioned)[^\.]*\.?', '', response, flags=re.IGNORECASE)

        return response.strip()
    # function ddescrining chat between the user and the virtual assiatant
    def chat(self, user_input):
        self.chat_history.append({"role": "user", "content": user_input})# The user's input is appended to chat history allowing the groq api to provide detailed responses based on previous inputs
        # try excep block for handling erros
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.chat_history,
                max_tokens=1000,
                temperature=1.2
            )
            logging.info(f"API Response: {response}") # output of the api responses

            reply = response.choices[0].message.content #ouput from the user's question to the llm
            cleaned_reply = self.clean_response(reply) # cleaned response removing unneccessry words or sentences.
            self.chat_history.append({"role": "assistant", "content": cleaned_reply}) # appending the virtual assistant's response to chat_history
            print("Assistant:", cleaned_reply) # priting the assistant's response

            logging.info(f"Customer query: {user_input}") # adding customer or user query to the log file
            logging.info(f"Assistant: {cleaned_reply}") # adding assisstant's to the log file

            """
                The httpx library is utilised for handling http errors i.e errors with codes 401,404,429 500 etc
            """
        except httpx.HTTPStatusError as http_err:
            status = http_err.response.status_code
            print(f"HTTP error: {status}")
            if status == 401:
                print("Invalid API key. Exiting...")
                return False
            elif status == 404:
                print("Model not found.")
            elif status == 429:
                print("Rate limit exceeded.You have sent too many requests")
            else:
                print(f"Response text: {http_err.response.text}")
        except Exception as e: # line of code for handling errors that occured suddenly and cannot be accounted for using the httpx library
            print(f"Unexpected error: {e}")
        return True
# main block of code to urn the file
if __name__ == "__main__":
    api_key = os.getenv("GROQ_API_KEY") # loading the api_key stored secretly in the .env file

    if not api_key:# handling error just incase my api key is not in the .env file
        print("GROQ_API_KEY not found in environment variables.")
    else: # calling the class EducationalCustomerAssistant
        assistant = EducationalCustomerAssistant(api_key)
    #    Print statement for welcoming the intending user
        print("Hello i am your educational assisstant for today.\n\nHow may i be of help to you\nIf you no longer wish to continue, input `stop`")
        #while loop for handling the user input and assistant's output
        while True:
            user_input = assistant.get_user_input()
            if user_input.lower() == "stop": # line of code to stop quering the api
                break
            continue_chat = assistant.chat(user_input)
            if not continue_chat:
                break
