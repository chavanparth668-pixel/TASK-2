
numberList = []
def showmenu():
    print("""
    1.Add
    2.Update
    3.Delete
    4.Exit or Quit
    5.View
    """)
def askuser():
    choice = input("Enter Choice : ")
    return choice
def add():
    username = input("Enter Username : ")
    usernumber = input("Enter Usernumber : ")
    contact = {
        "NAME" : username,
        "NUMBER" : usernumber
        }
    numberList.append(contact)
    print("contact save :) ")
def update():
    i = 0
    for contact in numberList:
        print(i, "- ",contact) 
        i+=1
    select = int(input("select contact"))
    username = input("Enter username : ")
    usernumber = input("Enter usernumber : ")
    contact = {
        "NAME" : username,
        "NUMBER" : usernumber
        }
    numberList[select] = contact








def delete():
    i = 0
    for contact in numberList:
        print(i, "- ",contact)
        i+=1
    select = int(input("select contact"))
    numberList.pop(select)



def view():
    print(numberList)



while True:
     showmenu()
     ch = askuser()
     match(ch):
          case '1':
              add()
          case '2':
              update()
          case '3':
              delete()
          case '4':
              exit or quit()
          case '5':
              view()
          case '6':
              print("invalid choice")
                         
                              
