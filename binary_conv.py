# function to convert decimal to binary
def bin_conv(decimal):
    conv_list = []
    while decimal != 0:
        conv_list += str(decimal % 2)
        decimal = int(decimal / 2)

    return "".join(conv_list[::-1])


# Program info
print("This is a decimal to binary convertor!\n")
# Taking in the user input
user_input = int(input("Enter a number in decimal:"))

# calling the function and printing out the result:
print(bin_conv(user_input))

