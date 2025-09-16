# calculator_chatbot.py

from Model.model import Model
from Chatbot.prompt import Prompt


class Calculator_Chatbot:

    def calculator_chatbot(self, query):
        model = Model()
        output = model.model(Prompt.prompt, query)
        return output
