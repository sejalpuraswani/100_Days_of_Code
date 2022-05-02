alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("\n****Encryption and Decryption Generator****\n")
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print("*********************************")
  print(f"Here's the {cipher_direction}d result: {end_text}")
  print("*********************************")

will_end = False
while not will_end:

   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   print("----------------------------------------")
   text = input("\nType your message you want to encrypt/decrypt:\n").lower()
   print("---------------------------------------")
   shift = int(input("\nhow many times you want to shift:\n"))
   print("----------------------------------------\n")


   shift %= 26

   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
   restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
   print("--------------------------------------")
   if restart == 'no':
     will_end = True
     print("\nGoodbye!")
