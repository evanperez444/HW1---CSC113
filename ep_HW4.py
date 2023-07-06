#File Reading Project
#By Evan Perez
#ID: 24212505


#Operating System library allows us to manipulate files and their paths
import os

#reads a file and prints the contents out
def read_file(input_file):

    #exception handling, makes sure file exists
    handle_exception(input_file)

    print("-----------------------------------------")
    #opens file for reading
    with open(input_file, 'r') as this_file:

        #for every line in the file, print
        for l in this_file:
            print(l)

    #close the file
    this_file.close()
    print("-----------------------------------------")


#appends a string to a file
def append_file(input_file, string):

    # exception handling, makes sure file exists
    handle_exception(input_file)

    #opens the file to not only read, but edit it as well
    with open(input_file, mode="r+") as this_file:

        #reads initial contents
        this_file.read()

        #appends string to existing contents
        print(string, file=this_file)

    #close the file
    this_file.close()


    print("//////////////")
    print("New string " + string + "appended to file")
    print("//////////////")





#copy the contents of a file and create a new file with '_copy' added to it that contains the same content of the original file
def copy_file(input_file):

    # exception handling, makes sure file exists
    handle_exception(input_file)

    #takes the input file path split up into parts and assigns it to a variable
    base = os.path.splitext(input_file)

    #makes a new output file name with the first part of the input path and add '_copy.txt' to it
    output_file = os.path.join(str(base[0]) + '_copy.txt')

    #reads the contents of the input file and writes into the new output file
    with open(input_file, 'r') as this_file, open(output_file, 'w') as other_file:

        #goes through every line of the input file and writes it into the new one
        for l in this_file:
            other_file.write(l)

    #closes file
    this_file.close()

    print("//////////////")
    print("File copied")
    print("//////////////")


#deletes a file
def delete_file(input_file):
    #exception handling, makes sure file exists
    handle_exception(input_file)

    #removes the file from directory
    os.remove(input_file)
    print("//////////////")
    print("File removed")
    print("//////////////")


#handles exception where file does not exists
def handle_exception(input_file):
    path = input_file

    #if the path does not exist in the directory, let the user know
    if os.path.exists(path) == False:
        print("-----------------------------------------")
        print("File not found")
        print("-----------------------------------------")
        #terminates program
        exit()

#reads a file, then appends a string, then reads new file
read_file('data.txt')
append_file('data.txt', 'NEWlY APPENDED TEXT ')
read_file('data.txt')

#copies a file and then reads its contents
copy_file('data.txt')
read_file('data_copy.txt')

#copies a file and reads it's contents, then deltes that file and tries to delete it
copy_file('data_copy.txt')
read_file('data_copy_copy.txt')
delete_file('data_copy_copy.txt')
read_file('data_copy_copy.txt')
