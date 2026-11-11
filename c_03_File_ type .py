# ask users for file type (integer / image / text / xxx
def get_filetype():

    while True:
            response = input("File type: ").lower()

            # check for 'i' or the exit
            if response == "xxx" or response == "i" :
               return response

            # check if it's an integer
            elif response in ['integer', 'int']:
                 return "integer"

            # check for an image
            elif response in ['image','picture','img','p']:
                return "image"

            # check for an image
            elif response in ["text",'txt','t']:
                return "text"
            # if the response is invalid output an error
            else:
                print("Please enter a vaild file type ")

# Main routine goes here
while True:
    file_type = get_filetype()
    # if user 'i' ask if they want an image/integer
    if file_type =="i":

        want_image = input("press <enter> for an integer or any key image")
        if want_image == "":
            file_type == "integer"
        else:
            file_type == "image"

    print (f"you chose {file_type} ")

    if file_type == "xxx":
        break