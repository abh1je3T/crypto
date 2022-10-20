"""
from caesarcipher import CaesarCipher

cipher = CaesarCipher('Abhijeet N',offset=7)
enc_cipher=cipher.encoded
print(enc_cipher)

dec_cipher=CaesarCipher(enc_cipher,offset=7)
print(dec_cipher.decoded)

"""
from caesarcipher import CaesarCipher

cipher = CaesarCipher('Abhijeet N',offset=7)
print(cipher.encoded)

message = cipher.encoded.upper() #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
   print('Hacking key #%s: %s' % (key, translated))
