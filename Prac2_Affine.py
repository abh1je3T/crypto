def encAffine(msg, key_a, key_b):
    enc_str = ""
    for i in toupper:
        enc_num = ((key_a * (ord(i) - 65) + key_b) % 26)
        enc_str += chr(enc_num + 65)
    return enc_str


def decAffine(encMsg, key_a, ey_b):
    inv_kA = pow(key_a, -1, 26)
    dec = ""
    for i in encMsg:
        dec_txt = (inv_kA * ((ord(i) - 65) - key_b) % 26)
        dec += chr(dec_txt + 65)
    return dec


msg = "AbhijeetNaikwadi"
toupper = msg.upper()
key_a = 3
key_b = 1
enc_affine = encAffine(toupper, key_a, key_b)
print(enc_affine)
dec_affine = decAffine(enc_affine, key_a, key_b)
print(dec_affine)
