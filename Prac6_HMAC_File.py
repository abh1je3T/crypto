import hmac,hashlib

f = open('./Files/msg.txt', 'rb')
try:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest = hmac.new(b'14-Abhijeet', block, hashlib.sha256).hexdigest()
finally:
    f.close()

print(digest)
