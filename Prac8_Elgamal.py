from elgamal.elgamal import Elgamal

msg=b'14-Abhijeet N'
pb_k,pv_k=Elgamal.newkeys(16)
print(pb_k)
print(pv_k)
Enc_msg=Elgamal.encrypt(msg,pb_k)


print(Enc_msg)

Dec_msg=Elgamal.decrypt(Enc_msg,pv_k)
print(Dec_msg)

