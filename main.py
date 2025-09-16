
# main.py

from Chatbot.chatbot import Chatbot
from Calculator.calculator_chatbot import Calculator_Chatbot


def main(key, **kwargs):
    if key == "chatbot":
        chatbot  = Chatbot()
        output = chatbot.chatbot(kwargs.get("query"))
        return output
    
    elif key == "calculator":
        chatbot = Calculator_Chatbot()
        output = chatbot.calculator_chatbot(kwargs.get("query"))
        return output

key = "chatbot"
chatbot_query = "what is the answer of 2+2?"

# key = "calculator"
# calculator_query = "sin(2)"

output = main(key, query=chatbot_query)
print(output)