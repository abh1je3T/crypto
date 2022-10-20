import hashlib
import hmac

key = "Secret Key"
message = "14-Abhijeet N"
h = hmac.new(key.encode(), message.encode(), hashlib.sha512).hexdigest()

print("HMAC Code for Verification of Msg:",h)