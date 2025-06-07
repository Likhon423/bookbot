def find_num_words(text):
  tot_words = text.split()
  return len(tot_words)

def count_char(text):
  char_count = {}
  for c in text:
    c_lowered = c.lower()
    if c_lowered in char_count:
      char_count[c_lowered] += 1
    else:
      char_count[c_lowered] = 1

  return char_count

def sort_on(dict):
    return dict["count"]

def sorted_dict(dict):
  keyed_dict = []

  for ch in dict:
    keyed_dict.append({"char": ch, "count": dict[ch]})

  keyed_dict.sort(reverse=True, key=sort_on)
  return keyed_dict
