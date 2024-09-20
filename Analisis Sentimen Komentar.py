# Author: samflew (raiyan)
# Date: 09/20/24 (September 20 2024)
# Description: Program ini akan menganalisa sentimen (baik/buruk) suatu komentar terhadap produk yang telah dibeli oleh user.

# https://github.com/samflew
# https://instagram.com/samflew

produk_yang_dibeli = input("Apa produk yang baru kamu beli? ")
komentar_produk_yang_dibeli = input(f"Apa komentar mu tentang produk {produk_yang_dibeli} yang baru kamu beli ?")

def analisa_komentar(komentar):
    hasil = []
    for komen in komentar.split(" "):
        if "buruk" in komen and not "buruk" in hasil:
            hasil.append("buruk")
        elif "baik" in komen and not "baik" in hasil:
            hasil.append("baik")

    if len(hasil) == 1 and "baik" in hasil:
        return "1baik"
    elif len(hasil) == 1 and "buruk" in hasil:
        return "1buruk"
    elif len(hasil) == 2 and (("baik" in hasil) and ("buruk" in hasil)):
        return "baik, buruk"
    else:
        return "invalid"

hasil_analisa_komentar = analisa_komentar(komentar_produk_yang_dibeli)
if "1baik" in hasil_analisa_komentar:
    print("Anda mengomentari produk ini baik.")
elif "1buruk" in hasil_analisa_komentar:
    print("Anda mengomentari produk ini buruk.")
elif "baik, buruk" in hasil_analisa_komentar:
    print("Anda mengomentari produk ini baik dan juga buruk")
else:
    print("Kamu tidak masuk kualifikasi analisa sentimen (baik/buruk) kami.")