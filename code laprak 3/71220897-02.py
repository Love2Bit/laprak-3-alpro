# input
num1 = int(input("Masukkan bilangan pertama (10-99): "))
num2 = int(input("Masukkan bilangan kedua (10-99): "))

# mengubah jadi string
num1_str = str(num1)
num2_str = str(num2)

# Proses
for digit1 in num1_str:
    for digit2 in num2_str:
        if digit1 == digit2:
            print("Sama.")
            quit()

print("Tidak sama.")