import random

buyuklu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*!&$#?=@1234567890"
kucuklu = "abcdefghijklnopqrstuvwxyz+-/*!&$#?=@1234567890"
karisikli = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz+-/*!&$#?=@1234567890"
password = ""
buyukkucuksecim = ""


while True:
    prompt = int(input("Parola uzunluğu giriniz: "))
    if prompt == "exit":
        break
    while True:
        buyukkucuksecim = input("Sadece Büyük yada Küçük veya Karışık yazarak kullanacağınız harf türünü belirtin: ")
        if buyukkucuksecim == "Büyük" or buyukkucuksecim == "büyük":
            buyukkucuksecim = "buyuk"
            break
        elif buyukkucuksecim == "Küçük" or buyukkucuksecim == "küçük":
            buyukkucuksecim = "kucuk"
            break
        elif buyukkucuksecim == "Karışık" or buyukkucuksecim == "karışık":
            buyukkucuksecim = "karışık"
            break
        else:
            print("Büyük,Küçük yada Karışık yazmalısınız!")
    if buyukkucuksecim == "buyuk":
        for i in range(prompt):
            password += random.choice(buyuklu)
    elif buyukkucuksecim == "kucuk":
        for i in range(prompt):
            password += random.choice(kucuklu)
    elif buyukkucuksecim == "karışık":
        for i in range(prompt):
            password += random.choice(karisikli)
    print("Oluşturulan şifreniz: ")
    print(password)
    soru = input("Tekrar oluşturmak istermisiniz?")
    if soru == "hayır" or soru == "Hayır":
        print("İyi günler 🖐")
        break
    elif soru == "evet" or soru == "Evet":
        pass
