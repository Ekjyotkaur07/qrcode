import qrcode

def gen_qr():
    print("QR CODE GENERATOR")

    data = input("Enter data: ")
    filename = input("Enter filename: ")

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename + ".png")

    print("QR Code Generated Successfully")


gen_qr()
