# TUGAS 3
## 1. Perbedaan POST dan GET
### a. Dalam pengiriman data
- POST, data dikirim ke server sebagai bagian dari permintaan HTTP, data ini tidak terlihat dalam URL. Karena tersembunyi, maka cocok untuk mengirim data sensitif seperti kata sandi.
- GET, data dikirim sebagai bagian dari URL dengan parameter yang terlihat dalam query string. Kurang aman, karena data terlihat dalam URL.
### b. Penggunaan Caching
- POST tidak di-cache oleh browser
- GET biasanya di cache oleh browser
### c.Tujuan penggunaan
- POST digunakan untuk mengirimkan data hasil isi form seperti pendaftaran penggunaan, memuat komentar, dan lain-lain.
- GET digunakan untuk meminta data dari server seperti pencarian atau tautan berbagi.
### d. Perubahan pada data server
- POST dapat menghasilkan perubahan pada data server setiap kali digunakan, seperti penambahan data , dan lain-lain
- GET hanya digunakan untuk membaca data sehingga tidak menghasilkan perubahan pada server.


## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Perbedaan utama dibagi menjadi 3 bagian, yakni format, struktur, dan tujuan.
- XML (eXtensible Markup Language)
Merupakan bahasa markup yang menggunakan tag untuk menandai elemen -elemen dalam dokumen, sehingga dalam menggunakannya terdapat aturan ketat untuk sintaksis.
Memiliki struktur hierarkis yang merepresentasikan data dengan baik dalam struktur pohon.
Digunakan untuk pertukaran data yang sangat terstruktur, seperti SOAP (Simple Object Access Protocol) dalam layanan web atau penyimpanan konfigurasi data dalam format yang dapat dibaca oleh manusia.
- JSON (JavaScript Object Notation)
Merupakan format daya yang lebih ringkas dan ringan daripada XML. Sintaksnya mirip dengan JavaScript yang digunakan dalam merepresentasikan objek dan array.
Strukturnya sederhana dengan objek terdiri dari pasangan key:value dan array yang berisi nilai-nilai.
Digunakan secara luas dalam pertukaran data antara aplikasi web modern, salah satunya dalam RESTful API, karena kesederhanaan, kecepatan, dan efisiensinya. JSON cocok untuk berbagai jenis data, termasuk data dinamis yang diproses oleh JavaScript di sisi klien.
- HTML (Hypertext Markup Language)
Merupakan bahasa markup yang digunakan untuk membuat halaman web. HTML punya sintaks khusus yang mengatur tampilan dan struktur konten pada halaman web
Struktur dokumen khusus dengan elemen seperti <html>, <head>, <body> ,dan tag-tag lainnya
Digunakan untuk membuat halaman web yang dapat ditampilkan oleh browser web, sebagai antarmuka pengguna pada aplikasi web.
### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Format JSON sederhana sehingga data mudah dipahami oleh manusia dan mudah diproses juga oleh komputer. 
- Ukuran data format JSON lebih kecil dibandingkan dengan XML, sehingga lebih efisien dalam penggunaan bandwidth dan pengiriman data melalui jaringan. 
- JSON berintegrasi dengan baik dengan JavaScript, yang merupakan bahasa klien yang umum digunakan di aplikasi web modern, sehingga sangat cocok digunakan dalam komunikasi antara sisi klien dan sisi server. 
- Format JSON cocok untuk pertukaran data antara aplikasi web karena banyak bahasa pemrograman dan framework web yang memiliki dukungan bawaan untuk membaca dan menulis data JSON. 
### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat input form untuk menambahkan objek model pada app sebelumnya
    Dengan membuat berkas baru bernama forms.py di main yang gunanya mendefinisikan struktur form apa yang akan ditampilkan untuk menginput data produk baru. Ada dua didefinisikan, yakni data yang disimpan dalam bentuk Product dengan atribut seperti name, price, amount, dan description. 
    Setelah membuat kelas struktur form di forms.py, untuk penggunaannya kita harus menyambungkan nya di views.py dengan mengimpor class ProductForm dari forms.py tadi. Di views.py, kita membuat  
    form = ProductForm(request.POST or None)
    di dalam sebuah fungsi create_product, tetapi di dalamnya terdapat pengecekan apakah pengisian form sudah valid dah apakah benar request metodenya POST. Jika benar, maka dipanggil form.save() da balik ke main.html. Jika tidak valid maka tetap di create_product.html dengan context ({‘form’ : form}).
    Pada fungsi show_main karena tidak hanya menampilkan name dan class pada main-html, kita harus menambahkan  products juga. 
- Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID dan JSON by ID. 
    Baik XML dan JSON  menggunakan import dari HttpResponse dan serializers (untuk menerjemahkan objek model menjadi format lain seperti XML atau JSON). Bedanya kalau tanpa id, maka parameter fungsinya hanaya request saja. Kemudian, jika kita mau objek model dalam bentuk XML, maka paramter dari serializernya “xml”, sedangkan kalau JSON maka paramternya “JSON”. Kalau dengan id,  maka tidak menggunakan all(), tetapi filter(pk=id) sehingga parameternya juga tidak hanya request tetapi juga id. 
- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
    Routing dari masing-masing fungsi yang ada di views dilakukan dengan terlebih dahulu menambahkan import dari from main.views. Setelah ditambahkan baru menambahkan path url ke dalam urlpatterns agar fungsi di views tadi bisa diakses. Salah satu contoh:
    `path('json/', show_json, name='show_json'),`
- Mengakses kelima URL di poin 2 menggunakan Postman
    Postman digunakan sebagai data viewer untuk mengetes apakah request baru dengan method GET sudah benar dikirim dengan baik. Pengecekannya harus terlebih dahulu run server kode kita dengan  python manage.py runserver.
- Menambahkan bonus berupa kalimat “ Kamu menyimpan X item pada toko ini”
    Penambahan dilakukan dengan dengan membuat variabel total_items terlebih dahulu pada views.py yang ada di main, dengan kode
    ` total_items = products.count()`
   total_items = products.count()
    Kemudian, dimasukan ke dalam fungsi dictionary. Karena show_main me-render halaman main.html, maka di main.html, kita memasukkan 
    `<p>Kamu menyimpan {{ total_items }} item pada toko ini.</p>`
## Foto POSTMAN
- XML
![XML](foto/Screenshot%20(4485).png)
- XML by ID
![XML by ID](foto/Screenshot%20(4486).png)
- JSON
![JSON](foto/Screenshot%20(4487).png)
- JSON by ID
![JSON by ID](foto/Screenshot%20(4488).png)

# TUGAS 2
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat sebuah proyek Django baru.
`django-admin startproject nama_proyek`

    Proyek ini berfungsi untuk menampung keseluruhan situs web atau aplikasi web yang dibangun, sehingga di dalamnya dapat dilakukan pengaturan global proyek, seperti mengatur database, URL, dan konfigurasi lainnya. Di dalamnya terdapat __init__.py, asgi.py, settings.py, urls.py, wsgi.py, dan manage.py.
-  Membuat aplikasi dengan nama main pada proyek tersebut.
    Dalam virtual environment, kita membuat aplikasi dari proyek STOKTOKOSARAS dengan kode
    `python manage.py startapp main`
    Kode ini membuat direktori baru dengan nama main, yang didalamnya terdapat berkas-berkas dasar untuk keperluan aplikasi, seperti models.py (untuk mendefinisikan model-model), views.py (menghubungkan permintaan HTTP dengan logika bisnis dan tampilan yang akan digunakan dalam respons, seperti interaksi dengan data, proses permintaan, dan pemerian tampilan pada pengguna), urls.py (unuk mendefinisikan routing), dan admin.py (untuk memanajmeni admin aplikasi). __init__.py berupa berkas kosong (menunjukkan direktori apliasi merupakan sebuah paket Python yang dapat diimpor). 
    tidak lupa menambahkan ‘main’ pada INSTALLED_APPS pada setting.py karena kita membentuk suatu app dengan nama main, app ini harus didaftarkan. 
    Untuk tampilan HTML-nya kita membuat folder templates.
-  Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Setelah menambahkan aplikasi, agar dapat dijalankan, kita melakukan routing. Routing adalah proses pengarahan permintaan HTTP yang diterima oleh server web ke fungsi atau aksi yang telah didefinisikan pada aplikasi web kita. TIndakannya itu akan diarahkan ke views.  Penambahannya dengan mengetik pada urlpatterns dengan kode
    `from main.views import show_main
    app_name = 'main'
    path('', show_main, name='show_main'),`
    path untuk URLnya string kosong (‘ ‘), ini dibuat seperti ini agar ketika pengguna masuk ke domain situs web tanpa tambahan path atau akar situs maka yang dimunculkan fungsi show_main. 
-  Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    Langkah ini dilakukan di model.py karena model.py merupakan tempat untk mendefinsikan sturktur model dalam Django. Model digunakan untuk menggambarkan bagaimana data akan disimpan dalam basis data kita. Di dalam model bernama “Item”, dalam tugas ini, kita harus memiliki tiga atribut wajib seperti, “name”, “amount”, dan “description” dengan jenis tipe-tipe berbeda, seperti Char, Integer, dan Text. Jadi tiap objek yang dibuat akan memiliki attribute ini.  Kedepannya, karena program STOKTOKOSARAS ada atribut-atributnya yang saya tambahkan di kemudian. 
    Setelah kita mendefinisikan bagaimana bentuk format data dengan atributnya, untuk dalam tampilan website kita perlu file HTML dengan membuat template. Folder templates harus dimasukkan ke dalam TEMPLATES pada setting.py. 
    Di tutorial 2, menggunakan base.html untuk template utama, sehingga untuk tiap html yang ada terdapat {% extends 'base.html' %}
    Berhubungan dengan atribut produk, untuk create produk juga perlu form untuk struktur produk dengan menambahkan kode pada forms.py
-  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    Sejauh ini dalam views, saya menggunakan dua jenis fungsi. Satu untuk membuat objek, satu lagi untuk menampilkan objek tersebut ke dalam html. 
    `def show_main(request):
        products = Product.objects.all()


        context = {
            'name': 'Pak Bepe', # Nama kamu
            'class': 'PBP A', # Kelas PBP kamu
            'products': products
        }
        return render(request, "main.html", context)`
    Fungsi diatas ini menerima argumen request yang mewakili permintaan HTTP yang dikirim pengguna ketika mereka mengakses halam tertentu. Kemudian, kita mengambil semua objek yang ada dalam model Product dengan query ‘Product. objects.all()’. Kemudian dalam context ini , memuat dictionary. Dan return render(request, “main. html”, context) ini ada terdapat ‘render’ yang menggabungkan template HTML dengan data yang diberikan dalam bentuk context. 
    `def create_product(request):
        form = ProductForm(request.POST or None)


        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))


        context = {'form': form}
        return render(request, "create_product.html", context)`
    Ini fungsi kedua yang bertujuan untuk  menangani pembuatan dan penyimpanan data produk baru ke dalam basis data. 
    `form = ProductForm(request.POST or None)
        if form.is_valid() and request.method == "POST"`
    ini memeriksa apakah form tersebut dibuat dengan valid atau permintaan merupakan metode HTTP POST. 
    form.save()
    produk baru yang diisi oleh pengguna akan disimpan ke dalam basis data sesuai dengan model Product yang telah didefinisikan sebelumnya. 
    return HttpResponseRedirect(reverse('main:show_main'))
    setelah data produk baru disimpan, akan diarah ke halaman “show_main” dengan HttpResponseRedicrect. reserve digunakan untuk menghasilkan URL berdasarkan nama view, ini untuk menghindari hardcoding URL di dalam kode. 
    jika isi form tidak valid atau permintaan bukan POST, atau pengguna memang mengakses halaman untuk pertama kali, maka halaman akan di render dengan menampilkan form input kepada pengguna. 
-  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Routing dilakukan untuk memetakan URL yang diterima oleh aplikasi web dengan fungsi view yang akan menangani permintaan tersebut. Kita menambahkan path ke dalam urlpatterns yang ada di dalam urls.py, seperti untuk dua fungsi di views, untuk show_ main dan untuk create_product. 

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![bagan](foto/gambar.png)
Ketika ada request client maka pertama diarahkan ke urls.py terlebih dahulu. Urls.py akan melakuakn routing dan memilih fungsi apa yang ada di views.py yang akan difire. Pada fungsi di views.py mengembalikan html yang ditaruh di folder templates yang dirender. Jika dalam requestnya ada berhubungan dengan data, seperti menambahkan item melalui form, maka akan dipanggil model juga. Data tersebut akan ditambah berdasarkan logika yang sudah didefinisikan di models.py, seperti atribut data. 


## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Virtual environment digunakan agar tidak memunculkan adanya konflik dependensi antara proyek satu dengan proyek lainnya. Misalnya, proyek A membutuhkan paket A versi 2.0 sedangkan proyek B membutuhkan paket A versi 1.0. Tanpa virtual environment, ketika kita langsung secara global mengupdate paket A menjadi versi 2.0, proyek B kita bisa saja terjadi error. Virtual environment ini juga berfungsi untuk menjaga kebersihan lingkungan, pendistribusian proyek dengan orang lain, mengisolasi lingkungan pengujian proyek, dan menghindari adanya penyebaran potensi risiko keamanan antara semua proyek yang berbagi lingkungan yang sama. 
- Tetap bisa, tetapi berisiko untuk terjadi nya konflik dependensi dan kerusakan karena penyebaran potensi risiko keamanan dapat terjadi dibandingkan dengan pembuatan aplikasi dilakukan dalam virtual environment. 

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC (Model-View-Controller)
    Model bertanggung jawab untuk mengelola data dan logika aplikasi. Model merupakan bagian yang menggambarkan struktur data dan operasi yang dapat dilakukan pada data. 
    View bertanggung jawab untuk menampilkan data kepada pengguna dalam tampilan antarmuka pengguna (user interface). 
    Controller bertanggung jawab untuk mengelola input dari pengguna dan mengirimkan perintah ke model atau view. Controller adalah penghubung antara model dan view.
- MVT (Model-View-Template)
    Template adalah komponen tambahan dalam MVT yang digunakan untuk tampilan yang dinamis. Templates menggambarkan data dari Model yang direpresentasikan dalam View. Template memnungkinkan penggunaann variabel dan logika sederhana untuk mengatur tampilan berdasarkan data dari Model. 
- MVVM (Model-View-ViewModel)
    Model dalam MVVM juga bertanggung jawab untuk mengelola data dan logika bisnis aplikasi , seperti dengan konsep Model dalam MVT, tetapi model lebih berfokus pada pengelolaan data dan sering kali lebih terlibat dalam komunikasi dengan sumber data eksternal seperti basis data atau API.  Model juga berkomunikasi dengan ViewModel yang kemudian mengelola presentasi data untuk View. 
    ViewModel merupakan komponen tambahan yang bertindak sebagai perantara antara Model dan View. ViewModel ini mengubah data dari Model menjadi format yang dapat ditampilkan di View dan juga menangani interaksi pengguna yang dikirimkan kembali ke Model. 
- Perbedaan Utama
MVC adalah pola arsitektur yang lebih umum digunakan dalam pengembangan perangkat lunak pada umumnya, dengan Controller bertindak sebagai penghubung antara Model dan View. MVT adalah pola arsitektur yang digunakan dalam kerangka kerja Django, dengan penggunaan Template untuk menghasilkan tampilan dinamis dalam aplikasi web. MVVM sering digunakan dalam pengembangan aplikasi desktop dan mobile yang memerlukan tampilan yang lebih dinamis dan interaksi antara tampilan dan data yang lebih kompleks. ViewModel berfungsi sebagai perantara antara Model dan View.

