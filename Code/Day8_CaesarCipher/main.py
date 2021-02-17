from art import logo 
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  cipher_text = ""
  for letter in text:
    if letter in alphabet:
      if direction == "encode":
        number = alphabet.index(letter) + shift
        if number > 25:
          number = -1 + shift
        new_message = alphabet[number]
        cipher_text += new_message
      elif direction == "decode":
        number = alphabet.index(letter) - shift
        if number > 25:
          number = -1 - shift
        new_message = alphabet[number]
        cipher_text += new_message
    else:
      cipher_text += letter
  print(f"The {direction}d message is: {cipher_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26
  caesar(text, shift, direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    should_continue = False
    print("Goodbye")

