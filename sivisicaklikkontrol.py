import smtplib

tfile = open("/sys/bus/w1/devices/28-0309977939a0/w1_slave") # Sensörün veri aldığı dosyayı açtık.28- ile başlayan numaraya kendi numaranızı girin.
text = tfile.read() # Dosyanın içindeki tüm metni oku.
tfile.close()       # Metnin okunduğu dosyayı kapat.
secondline = text.split("\n")[1] # Metni satırlara böl ve 2. satırı seç.
sicaklikdata = secondline.split(" ")[9] # Satırı boşluklara bakarak kelimelere ayır ve 10. kelimeyi seç (0'dan saymaya başlar).
sicaklik = float(sicaklikdata[2:]) # İlk iki karakter "t =" dir, bu yüzden onlardan kurtul ve sıcaklığı bir dizgiden bir sayıya çevir.
sicaklik = sicaklik / 1000 # Alınan verideki sıcaklığı tam gösterebilmek için 1000e bölünür.
print ('sivinin sicakligi=',sicaklik,'C')

if (sicaklik >= 25 and sicaklik <= 100):    
    try:                
                                                           # Hesap bilgilerimiz
        kullanici="gonder mail"
        kullanici_sifresi = 'sifre'
        alici = 'alici mail'              # alıcının mail adresi
        konu = 'sivi sicakligi'
        msj = 'sivi sicakligi cok yuksek'
                                                         # bilgileri bir metinde derledik
        email_text = """
        From: {}
        To: {}
        Subject: {}
        {}
        """ .format(kullanici,alici, konu, msj)
            
        server = smtplib.SMTP('smtp.gmail.com:587')   #servere bağlanmak için gerekli host ve portu belirttik
        server.starttls() #serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
        server.login(kullanici, kullanici_sifresi)   # Gmail SMTP server'ına giriş yaptık
        server.sendmail(kullanici, alici, email_text) # Mail'imizi gönderdik             server.close()     # SMTP serverimizi kapattık
        print ('email gönderildi')
            
           
    except:
        print("bir hata oluştu")
elif (sicaklik >=1 and sicaklik <=10):
    print('sivinin sicakligi dusuk ve sicaklik=',sicaklik,'C')
elif (sicaklik >=10 and sicaklik<=25):
    print('sivi sicakligi normal=',sicaklik,'C')
