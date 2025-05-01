from flask import Flask, request, jsonify, render_template
import logging
import graypy
import hashlib

# Flask uygulamasını başlat
app = Flask(__name__)

# Graylog ile loglama ayarları
graylog_handler = graypy.GELFUDPHandler('localhost', 12201)  # Graylog sunucusu ve portu
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(graylog_handler)

# Kullanıcı adı ve şifreyi saklamak için statik bir dictionary
users = {
    "testuser": hashlib.sha256("testpassword".encode()).hexdigest(),  # Örnek kullanıcı ve şifre
    "admin": hashlib.sha256("admin1234".encode()).hexdigest()
}

# Şifreyi hashlemek için fonksiyon
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    # Kullanıcıyı kontrol et
    if username in users:
        # Şifreyi hash ile karşılaştır
        if users[username] == hash_password(password):
            logger.info(f"Başarılı giriş: Kullanıcı {username} giriş yaptı.")
            return render_template('login.html', message="Giriş başarılı!")
        else:
            logger.warning(f"Hatalı giriş: Kullanıcı {username} hatalı şifre girdi.")
            return render_template('login.html', message="Hatalı şifre!")
    else:
        logger.warning(f"Kullanıcı bulunamadı: {username} adıyla kullanıcı yok.")
        return render_template('login.html', message="Kullanıcı bulunamadı!")

if __name__ == '__main__':
    app.run(debug=True)
