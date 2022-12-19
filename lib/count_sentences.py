#!/usr/bin/env python3

class MyString:
  def __init__(self, value=None):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self,value):
    if type(value) == str:
      self._value = value.strip()
    else:
      print("The value must be a string.")

  value = property(get_value, set_value,)

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")
  def is_exclamation(self):
    return self._value.endswith("!")
  def is_empty(self):
    return not self._value

  def count_sentences(self):
    if self.is_empty():
      return 0
    split_value = self._value.split(" ")
    count = 0
    for string in split_value:
      self._value = string
      if self.is_sentence() or self.is_question() or self.is_exclamation():
        count += 1  
    self._value = " ".join(split_value)
    return count
