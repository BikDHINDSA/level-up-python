def count_words(filepath,top_n=20):
  from collections import Counter
  import re
  with open(filepath, 'r', encoding='utf-8')as file:
    text = file.read()
  words = re.findall(r"[0-9a-zA-Z-']+",text.lower())
  counts = Counter(words)
  print(f"The total number of words in {filepath}: {len(words)} words.\n")
  print(f"Top {top_n} most common words in this file:")
  print("Word\tCount")
  for word,count in counts.most_common(top_n):
    print(f"{word:<15}{count}")

if __name__ == '__main__':
    count_words('shakespeare.txt')
