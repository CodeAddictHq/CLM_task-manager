


tasks = {
}
def show():
  if not tasks:
    print(">>>> Empty tasks")
  else:
    print("title : tasks")
    for idx, i in enumerate(tasks):
      print(f"{idx+1}.{i} : {tasks[i]}")

def add(a):
  try:
    b = a.split("'")
    if len(b) != 5:
      print(">>>> Error")
    else:
      b.remove(b[0])
      b.remove(b[1])
      b.remove(b[-1])
      title = str(b[0])
      task = str(b[1])
      tasks[title] = task
      print(">>>> Task Added")
  except:
    print(">>>> Error")
  


  
def dlt(a):
  b = a.split("'")
  if len(b) == 3:
    b.remove(b[0])
    b.remove(b[-1])
    print(f">>>>{str(b[0])} Deleted")
    del tasks[b[0]]
  else:
    print(">>>> Error")
  
  
  
  
print("==============================")
print("CMDs,\n1. add 'title' 'task'     #adds task\n2. del 'title'           #deletes task\n3. list                   #shows tasks\n4. exit                   #exits ")
print("==============================")
print("Write your cmds below >>")
while True:
  
  
  a = str(input("//>>"))
  if a[0] == "a":
    add(a)
  elif a[0] == "d":
    dlt(a)
  elif a.strip() == "list":
    show()
  elif a.strip() == "exit":
    print(">>>> Exited from shell")
    break
  else:
    print(">>>> Invalid message")
