meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }
anlami = 0
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın! ve çıkmak için: Çıkış,çıkış,exit,Exit): ")
    if word in meme_dict.keys():
        print(word,"'ın anlamı:")
        print(meme_dict[word])
    elif word == "Çıkış" or word == "çıkış" or word == "exit" or word == "Exit":
        print("İyi günler 🖐")
        break
    elif anlami == 10 or anlami > 10:
        print("Toplan 10 adet deneme yaptınız tekrar kullanmak için tekrar başlatın!")
        break
    else:
        print("Yazdığınız kelime veritabanında bulunamadı!")
        print("Tekrar deneyiniz!")
        continue
    anlami += 1

