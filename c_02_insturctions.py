# generates headings (eg:----heading----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")
#display instructions
def instruction():
    statement_generator("instructions", "-")

# main routine gose here
want_instructions = input("press <enter> to read the read instructions"" or any key to continue ")


if want_instructions =="":
    instruction()

    print ("program continues")

