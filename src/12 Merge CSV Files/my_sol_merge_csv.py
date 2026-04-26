import csv
def merge_csv(file_paths,output_path):

  all_rows = []
  all_fields = []

  for file_path in file_paths:
    
    with open(file_path,'r',newline ='',encoding ='utf-8') as file:
      reader = csv.DictReader(file,delimiter=',')
      
      for field in reader.fieldnames:
        if field not in all_fields:
          all_fields.append(field)

      for row in reader:
        all_rows.append(row)
  all_fields = list(all_fields)

  if "Name" in all_fields:
    all_fields.remove("Name")
    all_fields.insert(0,"Name")

  with open(output_path,'w',newline='',encoding='utf-8') as file:
    writer = csv.DictWriter(file,fieldnames = all_fields)
    writer.writeheader()
    for row in all_rows:
      writer.writerow(row)

if __name__ == "__main__":
  merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
