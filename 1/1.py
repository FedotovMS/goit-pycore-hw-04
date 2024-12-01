
def total_salary(path):
  try:
    with open(path, encoding='utf-8') as file:
      salaries=[]
      for line in file:
        try:
          name,salary =line.strip().split(',')
          salaries.append(float(salary))
        except ValueError:
          continue

      if not salaries:
        return(0,0)
      
      total=sum(salaries)
      average = total / len(salaries)
     
      return total, average
  
  except FileNotFoundError:
        print("Error: File not found.")
        return (0, 0)
  except Exception as e:
        print(f"Error: {e}")
        return (0, 0)

total, average = total_salary("1/payslips.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
