def get_cats_info(path):
  try:
    with open(path, encoding="utf-8") as file:
      cats=[]
      for line in file:
          try:
            catId,name,age=line.strip().split(',')
            cats.append({'id':catId, 'name':name, 'age':age})
          except ValueError:
            continue

    return cats
  
  except FileNotFoundError:
        print("Error: File not found.")
        return []
  except Exception as e:
        print(f"Error: {e}")
        return []    
    
cats_info = get_cats_info("2/cats.txt")
print(cats_info)