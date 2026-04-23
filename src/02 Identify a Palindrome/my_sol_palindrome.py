def is_palindrome(text):
  clean_str = "".join(char for char in text.lower() if char.isalnum())
  return clean_str == clean_str[::-1]
print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))
print(is_palindrome('hello world'))