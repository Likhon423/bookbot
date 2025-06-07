import sys
from stats import find_num_words, count_char, sorted_dict

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def main():
  text = get_book_text(sys.argv[1])
  num_words = find_num_words(text)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  
  print(f"Found {num_words} total words")

  print("--------- Character Count -------")
  
  counted_char = count_char(text)

  sorted_char_count = sorted_dict(counted_char)

  for item in sorted_char_count:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["count"]}")

  print("============= END ===============")
main()
