import smtplib

tfile = open("/sys/bus/w1/devices/28-0309977939a0/w1_slave") 
text = tfile.read() 
tfile.close() 
secondline = text.split("\n")[1] 
sicaklikdata = secondline.split(" ")[9] 
sicaklik = float(sicaklikdata[2:]) 
sicaklik = sicaklik / 1000
print ('sivinin sicakligi=',sicaklik,'C')

if (sicaklik >= 25 and sicaklik <= 100):    
    try:                
                                                           # Hesap bilgilerimiz
        kullanici="sivisicaklik@gmail.com"
        kullanici_sifresi = 'sivisicaklik123'
        alici = 'erdemtonga@yandex.com'              # alıcının mail adresi
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
