#!/usr/bin/env python3
import art
restart = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  if cipher_direction == "decode": shift_amount *= -1
  message = ""
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      message += alphabet[new_position]
    else:
      message += char
  print(f"Message: {message}")
  
print(art.logo)
while(restart):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text,shift,direction)
  restart_text = input("continue? 'y' or press 'enter' to end.\n")
  if not restart_text == 'y':
    restart = False
  