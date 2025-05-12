import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.set_value(value)

    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    def get_value(self):
        return self._value

    # Use a property for the value so any assignment will go through the setter
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.set_value(value)

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        return len([s for s in sentences if s.strip()])
