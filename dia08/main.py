minus = 'abcdefghijklmnopqrstuvwxyz'
mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cypher(text, shift, encrypt):
   new_text = ''
   pos = 0
   for char in text:
      if char in minus or char in mayus:
        if char in minus:
            pos = minus.index(char)
        if char in mayus:
            pos = mayus.index(char)
        if encrypt:
           new_pos = (pos + shift) % 26
        else:            
           new_pos = (pos - shift) % 26
        if char in minus:
            new_text += minus[new_pos]
        if char in mayus:
            new_text += mayus[new_pos]
      else:
         new_text += char
   return new_text

while True:
    text = input('Enter text: ')
    shift = int(input('Enter shift: '))
    option = input('Encrypt or Decrypt? (E/D): ')
    if option.upper() == 'E':
        print(f"Encrypted text: {caesar_cypher(text, shift, True)}")
    elif option.upper() == 'D':
        print(f"Decrypted text: {caesar_cypher(text, shift, False)}")
    continue_option = input('Do you want to continue? (Y/N): ')
    if continue_option.upper() != 'Y':
        break
