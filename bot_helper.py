
def input_error(func):
    def Inner(task):
        try:
            res = func(task)
        except KeyError:
            return "Use valid task!"
        except ValueError:
            return "Write phone number"
        except IndexError:
            return "Give me name and phone please"
        return res
    return Inner        

def add_func(add_task):
    int(add_task[2])
    dict_contacts[add_task[1]] = add_task[2]

def change_func(change_task):
    int(change_task[2])
    if change_task[1] in dict_contacts.keys():
        dict_contacts[change_task[1]] = change_task[2]
    else:
        return "Use valid contact!"    
        
def phone_func(phone_task):
    return dict_contacts[phone_task[1]]

func = {"add": add_func, "change": change_func, "phone": phone_func}

def get_func(task):
    return func[task]
        
list_for_exit = ["good bye", "close", "exit"]
dict_contacts = {}

@input_error        
def task_handler(task):
    task = task.lower()
    
    if task in list_for_exit:
        return "!end this!"
    elif task == "show all":
        return dict_contacts
    elif task == "hello":
        return "How can I help You?"
    
    task_list = task.split()
    
    handler = get_func(task_list[0])
    return handler(task_list)

def main():
    while True:
        task = input(">>>")
        res = task_handler(task)
        
        if res == "!end this!":
            print("Good bye!")
            exit()
        elif res:
            print(res)

if __name__ == "__main__":
    print(main())