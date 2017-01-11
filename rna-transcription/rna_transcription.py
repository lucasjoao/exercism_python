def to_rna(text):
  complement = ''
  alphabet = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}

  for char in text:
    if char not in alphabet:
      return ''
    complement += alphabet[char]

  return complement
