
def input_error(func):
    def Inner(task):
        try:
            res = func(task)
        except TypeError:
            return "Use valid task!"
        except ValueError:
            return "Write phone number"
        except IndexError:
            return "Give me name and phone please"
        return res
    return Inner        

@input_error 
def add_func(add_task):
    int(add_task[2])
    dict_contacts[add_task[1]] = add_task[2]

@input_error 
def change_func(change_task):
    int(change_task[2])
    if change_task[1] in dict_contacts.keys():
        dict_contacts[change_task[1]] = change_task[2]
    else:
        return "Use valid contact!"    
        
@input_error 
def phone_func(phone_task):
    return dict_contacts[phone_task[1]]

@input_error 
def show_func(task):
    return dict_contacts

@input_error 
def exit_func(task):
    return "!end this!"    

func = {add_func: ["add", "+"], change_func: ["change", "edit"], phone_func: ["phone"], 
        show_func: ["show", "show all"], exit_func: ["exit", "good", "buy", "close"]}

@input_error 
def get_func(task):
    for k, v in func.items():
        if task in v:
            return k
        
list_for_exit = ["good bye", "close", "exit"]
dict_contacts = {}

@input_error        
def task_handler(task):
    task = task.lower()
    
    if task == "hello":
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