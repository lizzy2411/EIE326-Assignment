Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def caesar_cipher(text, shift, mode='encrypt'):
...     result = ""
... 
...     if mode == 'decrypt':
...         shift = -shift
... 
...     for char in text:
...         if char.isalpha():
...             base = ord('A') if char.isupper() else ord('a')
...             # Shift character and wrap using modulo
...             shifted = (ord(char) - base + shift) % 26 + base
...             result += chr(shifted)
...         else:
...             # Keep non-alphabetic characters unchanged
...             result += char
... 
...     return result
... 
... # Example usage
... message = input("Enter your message: ")
... shift = int(input("Enter shift amount (e.g., 3): "))
... mode = input("Encrypt or Decrypt? ").strip().lower()
... 
... if mode in ['encrypt', 'decrypt']:
...     output = caesar_cipher(message, shift, mode)
...     print(f"\n{mode.title()}ed message: {output}")
... else:
...     print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
