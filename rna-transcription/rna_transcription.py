def to_rna(text):
  complement = ''
  char_complement = ''
  for char in text:
    char_complement = transcript(char)
    if char_complement is '':
      return ''
    complement += char_complement

  return complement

def transcript(char):
  alphabet = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
  if char not in alphabet:
    return ''

  return alphabet[char]
