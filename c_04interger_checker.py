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

 # Main routine  gose here
for item in range (0, 2):
    integer = int_check(  "integer: ",  0)
    print( integer )

print()

for item in range (0, 2):
    height = int_check( "height: " , 1 )
    print(height)