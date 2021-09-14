
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def markCompleted(index):
    print(f"{index} : {checklist[index]} √")

def listAllItems():
    if(len(checklist) > 0):
        for i in range(len(checklist)):
            print(f"{i} : {checklist[i]}")
    else:
        print("Checklist is empty")

def select(function_code):
    if(function_code == "C"):
        newItem = input("Input item to create: ")
        create(newItem)
    elif(function_code == "R"):
        index = int(input("Index to read: "))
        print(read(index))
    elif(function_code == "P"):
        listAllItems()
    elif(function_code == "M"):
        index = int(input("Enter index to mark as complete: "))
        markCompleted(index)
        destroy(index)
    elif(function_code == "Q"):
        return False
    elif(function_code == "H"):
        print("C : Create item\nR : Read Item\nP : Print all items\nM : Mark as complete\nQ : Quit")
    else:
        print("Unknown function code type H for help")
    return True

def run():
    running = True
    while(running):
        print(f"{CYAN}------------------")
        running = select(input(f"{BLUE}Enter a function code (H for help){GREEN}: ").upper())


CYAN = '\033[96m'
BLUE = '\033[94m'
GREEN = '\033[92m'
checklist = []
run()