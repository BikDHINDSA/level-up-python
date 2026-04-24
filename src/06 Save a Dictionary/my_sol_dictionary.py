import os
import json
def save_dict(data,filepath):
  with open(filepath,'w') as f:
    json.dump(data,f,indent=4)
def load_dict(filepath):
  with open(filepath,'r') as f:
    return json.load(f)
# if __name__ == '__main__':
#     save_dict({1: 'a', 2: 'b', 3: 'c'}, 'level_up_python/testing_my_code.json')
#     print(load_dict('level_up_python/testing_my_code.json'))
print(f"Current User: {os.getlogin()}")
print(f"Current Directory: {os.getcwd()}")