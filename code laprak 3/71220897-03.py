def pembulatan(bilangan):
    satuan = bilangan % 10
    puluhan = bilangan - satuan
    if satuan >= 5:
        puluhan += 10
    return puluhan

bil1 = int(input('Masukkan Bilangan 1 : '))
bil2 = int(input('Masukkan Bilangan 2 : '))
bil3 = int(input('Masukkan Bilangan 3 : '))

bil1 = pembulatan(bil1)
bil2 = pembulatan(bil2)
bil3 = pembulatan(bil3)

jumlah = bil1 + bil2 + bil3

print(f'Maka jawabannya adalah {bil1} + {bil2} + {bil3} = {jumlah}')