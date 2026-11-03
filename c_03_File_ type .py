# ask users for file type (integer / image / text / xxx
def get_filetype():
    response = input ("File type: ").lower()


    # check for 'i' or the exit
    if response == "xxx" or response == "i" :
       return response

    # check if it's an integer
    elif response in ['integer', 'int']:
         return "integer"

    # check for an image
    elif response in ['image' ,'picture' , 'img']:
        return "image"

    # check for an image
    elif response in ["text",'txt' 't']:
        return "text"
    # if the response is invalid output an error
    else:
        print ("Please enter a vaild file type ")

# Main routine goes here
while True:
    file_type = get_filetype()
    print (f"you chose {file_type} ")

    if file_type == "xxx":
        break