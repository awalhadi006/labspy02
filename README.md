<h1> Tugas Praktikum 2 </h1>
  <p> Membuat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan tersebut ditampilkan terbesarnya. Menggunakan             statement if.</br>
    <ul>
      <li> Pertama, kita gunakan statement <b><em>if</em></b>. Fungsinya adalah menentukan tindakan apa yang akan diambil sesuai dengan              kondisi.
      <li> Kedua, kita gunakan statement <b><em>elif</em></b>. Fungsinya adalah membuat kondisi/logika tambahan apabila kondisi yang                  dibuat oleh <b><em>if</em></b> sebelumnya bernilai salah.
      <li> Ketiga, kita gunakan statement <b><em>else</em></b>. Fungsinya adalah menangani semua kondisi selain kondisi yang telah                    dituliskan. </ul></p>
      
  <h3> Langkah-langkah membuat Program </h3>
  <p> 
  <ol> 
  <li> Mendeklarasikan a, b, c sebagai variable.
  
  > a = int(input("Masukkan bilangan a: ")) </br>
  b = int(input("Masukkan bilangan b: ")) </br>
  c = int(input("Masukkan bilangan c: ")) </br>
  
  <li> Membuat sebuah kondisi, jika a>b dan a>c, maka akan tampil besar bilangan a.
  
 > if a > b and a > c: </br>
     print("Bilangan terbesar adalah bilangan a =",a)
     
Note : Penulisan blok <b><em>if</em></b>, harus diberikan indentasi tab atau spasi 2x. </br>

  <li> Jika kondisi a>b dan a>c salah, maka akan membuat kondisi baru jika b>a dan b>c, maka akan tampil besar bilangan b. </br>

> if a > b and a > c: </br>
    print("Bilangan terbesar adalah bilangan a =",a) </br>
  elif b > a and b > c: </br>
    print("Bilangan terbesar adalah bilangan b =",b)
    
  <li> Ketika dari dua kondisi tersebut bernilai salah, maka akan tampil hasil dari mengeksekusi kode yang ada di dalam <em>else</em>.

> if a > b and a > c: </br>
    print("Bilangan terbesar adalah bilangan a =",a) </br>
  elif b > a and b > c: </br>
    print("Bilangan terbesar adalah bilangan b =",b) </br>
  else: </br>
    print("Bilangan terbesar adalah bilangan c =",c)

Contoh program yang telah dieksekusi </br>
Jika nilai <b>a</b> yang terbesar : </br>
![Bila a yang terbesar](https://user-images.githubusercontent.com/24362384/67976202-3e9f8f80-fc48-11e9-8970-c9f81f9bb5bf.PNG)

Jika nilai <b>b</b> yang terbesar : </br>
![Bila b yang terbesar](https://user-images.githubusercontent.com/24362384/67976301-6bec3d80-fc48-11e9-998d-76ea839baf39.PNG)

Jika nilai <b>c</b> yang terbesar : </br>
![Bila c yang terbesar](https://user-images.githubusercontent.com/24362384/67976351-82929480-fc48-11e9-8bf5-606ab75c710e.PNG)

<h3> Flowchart </h3>

![Flowchart_page-0001](https://user-images.githubusercontent.com/24362384/68922377-05216500-07ae-11ea-8988-349f91cab7c7.jpg)

<p>Kurang lebihnya mohon maaf.</br>
Sekian dan Terima Kasih.</p>
