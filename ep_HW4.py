#File Reading Project
#By Evan Perez
#ID: 24212505



def read_file(input_file):

    with open(input_file, 'r') as this_file:

        current_line = this_file.readline()

        while(current_line != ""):
            print(current_line)
            current_line = this_file.readline()

    this_file.close()



def append_file(input_file, string):

    with open(input_file, mode="r+") as this_file:

        this_file.read()

        print(string, file=this_file)

    this_file.close()





append_file('/Users/evanperez/Documents/GitHub/HW1---CSC113/data.txt', 'TESTING WRITING')

read_file('/Users/evanperez/Documents/GitHub/HW1---CSC113/data.txt')