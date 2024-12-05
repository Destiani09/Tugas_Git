data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

print("No. 1")
for i, j in data_panen.items():
    print(i, j)
print("\n")

print("No. 2")
muncul = (data_panen['lokasi2']['hasil_panen']['jagung'])
print(f"Jumlah Hasil Panen Jagung di Lokasi 2 adalah {muncul}")
print("\n")

print("No. 3")
cetak = (data_panen['lokasi3']['nama_lokasi'])
print(f"Nama Lokasi 3 adalah {cetak}")
print("\n")

print("No. 4")
for i, j in data_panen.items():
    h_padi = j['hasil_panen']['padi']
    h_kedelai = j['hasil_panen']['kedelai']
    print(i)
    print(f"Jumlah Hasil Panen Padi : {h_padi}")
    print(f"Jumlah Hasil Panen Kedelai : {h_kedelai} \n")
print("\n")

print("N0. 5")
padi1 = (data_panen['lokasi1']['hasil_panen']['padi'])
kedelai1 = (data_panen['lokasi1']['hasil_panen']['kedelai'])
padi2 = (data_panen['lokasi2']['hasil_panen']['padi'])
kedelai2 = (data_panen['lokasi2']['hasil_panen']['kedelai'])
padi3 = (data_panen['lokasi3']['hasil_panen']['padi'])
kedelai3 = (data_panen['lokasi3']['hasil_panen']['kedelai'])
padi4 = (data_panen['lokasi4']['hasil_panen']['padi'])
kedelai4 = (data_panen['lokasi4']['hasil_panen']['kedelai'])
padi5 = (data_panen['lokasi5']['hasil_panen']['padi'])
kedelai5 = (data_panen['lokasi5']['hasil_panen']['kedelai'])

print(f"Jumlah Hasil Panen Padi Lokasi 1 : {padi1}")
print(f"Jumlah Hasil Panen Kedelai Lokasi 1 : {kedelai1} \n")
print(f"Jumlah Hasil Panen Padi Lokasi 2 : {padi2}")
print(f"Jumlah Hasil Panen Kedelai Lokasi 2 : {kedelai2} \n")
print(f"Jumlah Hasil Panen Padi Lokasi 3 : {padi3}")
print(f"Jumlah Hasil Panen Kedelai Lokasi 3 : {kedelai3}\n")
print(f"Jumlah Hasil Panen Padi Lokasi 4 : {padi4}")
print(f"Jumlah Hasil Panen Kedelai Lokasi 4 : {kedelai4} \n")
print(f"Jumlah Hasil Panen Padi Lokasi 5 : {padi5}")
print(f"Jumlah Hasil Panen Kedelai Lokasi 5 : {kedelai5}")
print("\n")

print("No. 6")
for i, j in data_panen.items():
    nma_lks = j['nama_lokasi']
    h_padi = j['hasil_panen']['padi']
    h_jagung = j['hasil_panen']['jagung']

    print(i)
    if h_padi > 1300 or h_jagung > 800:
        print(f"{nma_lks} Memerlukan Perhatian Khusus \n")
    else :
        print(f"{nma_lks} Kondisi Baik \n")


print("Nama : Destiani \n Kelas : EE \n NRP : 152023201")
print("Nama : Destiani \n Kelas : EE \n Matkul : PemDas")
