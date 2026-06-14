def index_all(ml,target):
  indices = []
  for i,element in enumerate(ml):
    if element == target:
      indices.append([i])
    elif isinstance(element,list):
      for sub_index in index_all(element,target):
        indices.append([i]+sub_index)
  return indices