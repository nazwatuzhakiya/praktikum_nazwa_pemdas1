cuaca = str(input("Pilih kondisi cuaca (hujan/kemarau): "))

switcher ={
    "hujan": "banjir!",
    "kemarau": "kekeringan!"

}

hasil = cuaca.get(cuaca, "Input tidak valid. Silakan coba lagi!")

print(hasil)