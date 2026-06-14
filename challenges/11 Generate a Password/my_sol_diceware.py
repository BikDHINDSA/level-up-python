import secrets
def load_wordlist(filepath):
  word_list=[]
  with open(filepath,'r',encoding='utf-8') as file:
    for line in file:
      parts = line.strip().split()
      if len(parts)>=2 and parts[0].isdigit():
        word_list.append(parts[1].strip())
  return word_list
WORDLIST = load_wordlist('diceware.wordlist.asc')
def generate_passphrase(num_int):
  return " ".join([secrets.choice(WORDLIST) for _ in range(num_int)])

if __name__ == '__main__':
    print(generate_passphrase(7))
    print(generate_passphrase(7))