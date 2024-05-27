import sys


def run_exit(text):
    num=int(text)
    sys.exit(num)

def run_echo(text):
    print(text)


def main():
    valid_commands={"exit":run_exit,
                    "echo":run_echo,
                    }
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_string=input()
        index=input_string.find(" ")
        if index==-1:
            input_command=input_string
            input_text=""
        
        else:
            input_command=input_string[:index]
            input_text=input_string[index+1:]
        if input_command not in valid_commands:
            print(f"{input_command}: command not found")
        else:
            action_to_run=valid_commands[input_command]
            action_to_run(input_text)



if __name__ == "__main__":
    main()
