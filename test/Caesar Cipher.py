def Encrypt():
    initial_message = input("Enter the text to Encrypt: ")
    shift_num = int(input("Enter Shift Number: "))
    final_message = ""
    for i in initial_message:
        final_message += chr((ord(i) + shift_num))
    print(final_message)


def Decrypt():
    initial_message = input("Enter the text to Decrypt: ")
    shift_num = int(input("Enter Shift Number: "))
    final_message = ""
    for i in initial_message:
        final_message += chr((ord(i) - shift_num))
    print(final_message)


while True:
    choice = input("Enter 'encrypt' to Encrypt and 'decrypt' to Decrypt: ")
    if choice == "encrypt":
        Encrypt()
    elif choice == "decrypt":
        Decrypt()
    else:
        exit()
