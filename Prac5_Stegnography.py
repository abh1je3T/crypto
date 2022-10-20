from stegano import lsb
secret = lsb.hide("./Files/img.png", "14-Abhijeet N")
secret.save("./Files/steg_op.png")

clear_message = lsb.reveal("./Files/steg_op.png")
print(clear_message)