print("==========================Using brypt==========================")

import bcrypt

# Declaring our password
password = b'14-Abhijeet N'
# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password, salt)
# printing the salt
print("Salt :")
print(salt)
# printing the hashed
print("Hashed")
print(hashed)


print("==========================Using Hashlib==========================")
import hashlib
# Declaring Password
password = '14-Abhijeet N'
# adding salt as password
salt = "Big_hash"
# Adding salt at the last of the password
dataBase_password = password+salt
# Encoding the password
hashed = hashlib.md5(dataBase_password.encode())
# Printing the Hash
print(hashed.hexdigest())
