"""Day 8 Project - Caesar Cipher

Shift every letter of a message forwards (encode) or backwards (decode) by
an agreed number of places. With a shift of 3, "a" becomes "d".
Target: https://appbrewery.github.io/python-day8-demo/

Build it in the course's three parts:

1. Write encrypt(original_text, shift_amount). For each letter, find its
   position with alphabet.index(letter), add the shift, and build the
   result. Print "Here's the encoded result: ...". Shifting "z" by 9 must
   wrap round to "i": use % len(alphabet).
2. Write decrypt(original_text, shift_amount), which shifts backwards. Then
   merge both into caesar(original_text, shift_amount, encode_or_decode).
   Decoding is encoding with the shift multiplied by -1. Flip the sign
   once, before the loop.
3. Import art and print art.logo. Keep characters that are not in the
   alphabet (spaces, digits, symbols) unchanged. Ask whether to go again,
   and print "Goodbye" when the answer is "no".

Run from this day's folder:
    python project/main.py
"""
import art

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]

# Write your solution below this line.


def caesar(original_text, shift_amount, encode_or_decode):
    result = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            new_position = alphabet.index(letter) + shift_amount
            result += alphabet[new_position % len(alphabet)]
        else:
            result += letter
    print(f"Here's the {encode_or_decode}d result: {result}")


print(art.logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")