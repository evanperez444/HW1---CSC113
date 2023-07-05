#File Reading Project
#By Evan Perez
#ID: 24212505
import os


def read_file(input_file):
    handle_exception(input_file)

    with open(input_file, 'r') as this_file:

        current_line = this_file.readline()

        while(current_line != ""):
            print(current_line)
            current_line = this_file.readline()

    this_file.close()



def append_file(input_file, string):
    handle_exception(input_file)

    with open(input_file, mode="r+") as this_file:

        this_file.read()

        print(string, file=this_file)

    this_file.close()


def copy_file(input_file):
    handle_exception(input_file)

    base = os.path.splitext(input_file)

    output_file = os.path.join(str(base[0]) + '_copy.txt')

    with open(input_file, 'r') as this_file, open(output_file, 'w') as other_file:

        for l in this_file:
            other_file.write(l)

    this_file.close()


def delete_file(input_file):
    handle_exception(input_file)
    os.remove(input_file)


def handle_exception(input_file):
    path = input_file
    if os.path.exists(path) == False:
        print("File not found")
        exit()


