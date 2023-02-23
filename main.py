alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start_encryptor():
    direction = ""
    direction_flag = False
    while direction_flag is False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode" or direction == "decode":
            direction_flag = True


    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    alphabet_shifted = []

    for n in range(0, len(alphabet)):
        pos = n + shift
        if pos >= len(alphabet):
            pos -= len(alphabet)
        alphabet_shifted.append(alphabet[pos])
    reply = ""
    if direction == "encode":
        reply = ring(alphabet, alphabet_shifted, text)
    else:
        reply = ring(alphabet_shifted, alphabet, text)

    print(f"Here is your {direction}d result: {reply}!")
    go_again = input('Type "yes" if you want to go again. Otherwise type "no".\n')

    if go_again == "yes":
        start_encryptor()

def ring(list1, list2, msg):
    answer = []
    msg = list(msg)
    for n in range(0, len(msg)):
        if msg[n] in list1:
            indx = list1.index(msg[n])
            answer.append(list2[indx])
        else:
            answer.append(msg[n])
    return "".join(answer)


start_encryptor()
