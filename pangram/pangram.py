import string

def is_pangram(text):
  if (len(text) < 26):
    return False

  for s in string.ascii_lowercase:
    if not has_letter(text, s):
      return False

  return True

def has_letter(text, letter):
  if (text.count(letter) + text.count(letter.upper()) != 0):
    return True
  else:
    return False
