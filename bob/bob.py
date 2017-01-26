#
# Skeleton file for the Python "Bob" exercise.
#

def hey(what):
  if what.isupper():
    return 'Whoa, chill out!'
  elif what.isspace() or what == '':
    return 'Fine. Be that way!'
  elif what.rstrip().endswith('?'):
    return 'Sure.'
  else:
    return 'Whatever.'
