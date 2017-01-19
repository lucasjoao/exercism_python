def distance(first_strand, second_strand):
  if len(first_strand) != len(second_strand):
    raise ValueError()

  hamming_distance = 0
  for i in range(len(first_strand)):
    if first_strand[i] != second_strand[i]:
      hamming_distance += 1

  return hamming_distance
