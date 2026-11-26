# calculates number of bits needed to represent text in ascii
def calc_text_bits():
    pass

    #get text form user here
    response = input ("enter some text")

    # calculate bits needed
    num_chars = len (response)
    num_bit = num_chars * 8

    # set up answer and retrun
    answer = (f"{response} has {num_chars} characters."
              f" \n we need {num_chars} x 8 bits to repersent it which is {num_chars} bit")



#main Routine goes here
text_ans = calc_text_bits()e