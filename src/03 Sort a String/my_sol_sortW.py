def sort_words(text):
  return " ".join(sorted(text.split(),key=str.lower))