message = input ("Please type a message: ")
print("You said '{}'".format(message))

message = input ("Please type a " + "comma separated list of values: ")
values =message.split(",")
print("The first two elements of your list are: {} and {}".format(values[0],values[1]))