import sys

def read_files(file_path):

    # This is will make sure the things we pass in are files, if not an error  will be thrown 
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('The file has not been found')

'''This function converts the passed in parameters and turns it into a list all lowercase'''
def convert_list(convert):

    # Turns parameter into a list
    new_list = lambda x: x.split(" ")

    # Turns each element in the list lowercase IF it is a string
    lower_list = lambda y: y.lower() if isinstance(y , str) else y

    # The return output
    return list(map(lower_list, (new_list(convert))))

'''This is where we actually send the list from both files to result.txt'''
def create_result_file(input_file, output_file):
    
    
    # We open the file with 'a' to append anything that is added to it.
    with open(output_file, 'a') as output_file:

        # since we have a list rather then a full string, we have to iterate over each item and add it to the file
        list(map(lambda item: output_file.write(str(item) + '\n'), input_file))


        



def main():
    if len(sys.argv) != 3:
        print('python {__.py} {__.txt} {__.txt}')
        return
    

    # This takes in the two files thru the command line 
    file_path_one = sys.argv[1]
    file_path_two = sys.argv[2]

    # This runs the function to return the contents of the file
    a1 = read_files(file_path_one)
    b1 = read_files(file_path_two)

    # This runs the function to convert the contents into a list and lowercases them.
    aa = convert_list(a1)
    bb = convert_list(b1)


    # This function will send the results to the designated file
    create_result_file(aa,'result.txt')
    create_result_file(bb,'result.txt')


    




if __name__ == '__main__':
    main()


