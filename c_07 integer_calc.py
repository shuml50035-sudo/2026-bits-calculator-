# ask user for width and loop until they
# enter a number that is more than zero
def int_check (question , low ):

    error = "please enter a number that is more than zero\n "
    while True:

            try:
                # ask user for a number

                response = int(input(question))

                # check that the number is more than zero
                if response >= low:
                  return response
                else:
                    print(error)

            except ValueError:
                print(error)


# calculation how many bits are needed to represent an integer
def integer_calc():
    integer = int_check(  "integer: ",  0)

    #conver the integer to binary and work out the number of bit needed
    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bit = len (binary)


    # set up answer and return it
    answer = f"{integer} in binary is {binary}. we ned {num_bit} to represent it."
    return answer

# main routine here
integer_ans = integer_calc()
print(integer_ans)


