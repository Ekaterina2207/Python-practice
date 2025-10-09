def Caesar_encode(user_input, shift):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    encode_message = ''
    for char in user_input:
        if char in alphabet:
            encode_message += alphabet[(alphabet.index(char)+shift)%len(alphabet)]
        elif not char.isalpha():
            encode_message += char
        elif char.isupper():
            char = char.lower()
            encode_message += alphabet[(alphabet.index(char)+shift)%len(alphabet)].upper()

    return encode_message

def Caesar_decode(user_input, shift):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    decode_message = ''
    for char in user_input:
        if char in alphabet:
            decode_message += alphabet[(alphabet.index(char)-shift)%len(alphabet)]
        elif not char.isalpha():
            decode_message += char
        elif char.isupper():
            char = char.lower()
            decode_message += alphabet[(alphabet.index(char)-shift)%len(alphabet)].upper()

    return decode_message

message = input('Введите сообщение для кодировки: ')
shift = int(input('Введите шаг кодировки (цифра от 1 до 33): '))
print(f'Зашифрованное сообщение: {Caesar_encode(message, shift)}')
print(f'Расшифрованное сообщение: {Caesar_decode(Caesar_encode(message, shift), shift)}')