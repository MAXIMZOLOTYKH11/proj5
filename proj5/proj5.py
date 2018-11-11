# Project_5
# Maxim Zolotykh

file = input('Enter name of file: ')
while True:
    try:
        input_file = open (file,'r')
    except FileNotFoundError:
            print('File {} not faund.'.format(file))
            file_str = input('Enter name of file: ')
    else:
        with open('input.txt', 'r') as f_in:
            with open('output.txt', 'w') as f_out:
                information = ""
                for line in f_in:
                    information += line
                people, frogs, little, S, jump = information.split()
                try:
                    int(people) / int(frogs - little)
                except ZeroDivisionError:
                    print("Egor went home!", file=f_out)
                except ValueError:
                    print("Enter the number!", file=f_out)
                else:
                    if int(S) > int(jump):
                        print("Frogs doesn't jump!", file=f_out)
                    elif int(S) <= int(jump):
                        if int(frogs) >= int(people):
                            print("Frogs will be enough for everyone", file=f_out)
                        else:
                            print("Frogs enough for", int(people), "people")

