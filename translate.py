import os
import json
from deep_translator import GoogleTranslator


class Translator:
    def translate(self, prompt):
        translator = GoogleTranslator(source='auto', target='en')
        return translator.translate(prompt)
        

# # Usage:
# translator = Translator()
# a = translator.translate("Ko'chada ketayotgan yolg'iz chol")
# print(a)