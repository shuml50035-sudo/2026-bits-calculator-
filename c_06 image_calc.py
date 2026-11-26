# ask user for width and loop until they
# enter a number that is more than zero
def int_check (question , low ):

    error = "please enter a number that is more than zero\n "
    while True:

            try:
                # ask user for a number

                response = int(input(question))

                # check that the number is more than zero
                else:
                print(error)

            except ValueError:
                print(error)
                if response >= low:
                  return response


# calculation how many bits are needed to represent an integer
def image_calc():
    width = int_check(  "width: ",  0)
    height = int_check( "height: " , 1 )

    # calculations the number of pixels and multiply by 24 to get the number of bit
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return
    answer = (f"Number of pixels : {width} x {height} = {num_pixels} "
              f"\n number of bits:{num_pixels} x 24 = {num_bits}")

    return answer


image_ans = image_calc()
print(image_ans)