import pyAesCrypt

# custom encryption/decryption buffer size (default is 64KB)
bufferSize = 128 * 1024
password = "Pass@123"
# encrypt
pyAesCrypt.encryptFile(".\Files\data.txt", "data.txt.aes", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)
