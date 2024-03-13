# Some intro stuff

### Attention!
This note is in Indonesian. Please translate it if you're a foreigner.

## What is Flask?
Flask adalah salah satu framework web Python yang ringan dan fleksibel. Dibuat oleh Armin Ronacher, Flask memungkinkan pengembang untuk membuat aplikasi web dengan cepat dan mudah. Dengan filosofi "bawaan yang minimal", Flask memberikan kebebasan kepada pengembang untuk membangun aplikasi web sesuai kebutuhan mereka, tanpa memaksakan struktur atau paket tertentu.

## Main Features
- **Ringan dan Fleksibel**: Flask dirancang untuk menjadi ringan dan tidak membebani proyek Anda dengan fitur yang tidak diperlukan.
- **Rute URL**: Flask menyediakan sistem rute URL yang mudah untuk menentukan bagaimana aplikasi Anda merespons permintaan dari klien.
- **Templat**: Flask memiliki sistem templat yang kuat yang memungkinkan Anda untuk memisahkan tata letak dari logika aplikasi Anda.
- **Pembina Pengembangan Bawaan**: Flask hadir dengan pembina pengembangan bawaan yang memudahkan pengembangan dan debugging.
- **Ekosistem Yang Kaya**: Flask memiliki ekosistem plugin yang luas yang memungkinkan Anda untuk menambahkan fungsionalitas tambahan ke aplikasi Anda dengan mudah.

## Flask Installation
Kamu dapat menginstal Flask menggunakan pip, manajer paket Phyton:

```bash
    pip install virtualenv
    
    virtualenv env

    pip install flask
```

## Example of code
Berikut adalah contoh kode sederhana untuk membuat aplikasi web "Hello, World!" menggunakan Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

## Run the Flask App
Setelah menyimpan contoh kode di atas dalam file `app.py`, Kamu dapat menjalankan aplikasi Flask dengan mengetikkan perintah berikut dalam terminal:

```bash
python main.py
```

Aplikasi akan berjalan dan Kamu dapat mengaksesnya melalui browser dengan alamat `http://localhost:5000`.

## Conclusion
Flask adalah pilihan yang sangat baik untuk pengembangan aplikasi web Python yang ringan dan fleksibel. Dengan fitur-fitur yang kuat dan komunitas yang besar, Flask memungkinkan pengembang untuk membangun aplikasi web dengan cepat dan mudah.

Untuk informasi lebih lanjut, kunjungi situs web resmi Flask di [http://flask.pocoo.org/](http://flask.pocoo.org/).