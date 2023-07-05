#File Reading Project
#By Evan Perez
#ID: 24212505



def read_file(input_file):

    file = open(input_file, 'r')

    current_line = file.readline()

    while(current_line != ""):
        print(current_line)
        current_line = file.readline()

    file.close()



read_file('/Users/evanperez/Documents/GitHub/HW1---CSC113/data.txt')

