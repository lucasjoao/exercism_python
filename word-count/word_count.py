# -*- coding: utf-8 -*-
def personal_replace(text):
  chars = ['_', ',', '.', ':', '!', '&', '@', '$', '^', '&', '%']
  aux_text = text
  for char in chars:
    aux_text = aux_text.replace(char, ' ')

  return aux_text

def word_count(text):
  fix_text = personal_replace(text.lower())
  word_list = fix_text.split()
  d = {}

  for word in word_list:
    if not word in d:
      d[word] = word_list.count(word)

  return d
