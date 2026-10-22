# generates headings (eg:----heading----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# display instruction
def instruction():
    statement_generator("instructions", "-")


# main routine goes here
want_instructions = input('press <enter> to read the instructions'
                          'or any key to continue ')

if want_instructions == "":
    instruction()

print ("program continues")