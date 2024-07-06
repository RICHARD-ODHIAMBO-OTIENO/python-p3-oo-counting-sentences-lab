#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value if isinstance(value, str) else ''
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            self._value = ''
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]+', self.value)
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)