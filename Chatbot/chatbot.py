# chatbot.py

from Model.model import Model
from Chatbot.prompt import Prompt


class Chatbot:

    def chatbot(self, query):
        model = Model()
        output = model.model(Prompt.prompt, query)
        return output
