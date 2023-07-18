# İnstagram Medya İndirici

Bu Python kodu, Instagram profil fotoğrafı, gönderiler ve hikayeleri indirmek için Instaloader adlı bir kütüphane kullanır. Kullanıcıdan seçimler alarak Instagram hesaplarından içerikleri indirme işlemini gerçekleştirir.

**Kodun işleyişi aşağıdaki adımlardan oluşur:
**
İlk olarak, is_profile_exists fonksiyonu, belirtilen kullanıcı adının Instagram'da mevcut olup olmadığını kontrol eder. Bu işlem, kullanıcı adının Instagram API'sini kullanarak doğrulama yaparak gerçekleştirilir.

create_dirs fonksiyonu, indirilen içerikleri saklamak için gerekli dizinleri oluşturur. Bu dizinler "Instagram" adlı ana bir dizin altında, kullanıcı adına göre alt dizinler oluşturur. Bu alt dizinler, "Photos", "Videos" ve "Stories" olarak üçe ayrılır.

download_profile_picture fonksiyonu, belirtilen kullanıcı adına ait profil fotoğrafını indirir. Önce is_profile_exists fonksiyonunu kullanarak hesabın mevcut olup olmadığı kontrol edilir, ardından Instaloader kütüphanesini kullanarak profil fotoğrafı indirilir.

download_posts fonksiyonu, belirtilen kullanıcı adına ait gönderileri indirir. Yine is_profile_exists fonksiyonu kullanılarak hesabın mevcut olup olmadığı kontrol edilir. Daha sonra Instaloader kütüphanesi kullanılarak gönderileri indirir. İndirme işlemi paralel olarak gerçekleştirilir, bu da işlemi hızlandırır.

download_stories fonksiyonu, belirtilen kullanıcı adına ait hikayeleri indirir. Yine is_profile_exists fonksiyonu kullanılarak hesabın mevcut olup olmadığı kontrol edilir. Instaloader kütüphanesi kullanılarak hikayeler indirilir.

main_menu fonksiyonu, kullanıcıya yapmak istediği işlemi seçme imkanı sunan bir menü gösterir.

Ana main fonksiyonu, kullanıcıya menü seçeneklerini göstererek onun seçimine göre ilgili fonksiyonları çalıştırır. Kullanıcı çıkış yapmak istediğinde program sonlanır.

Bu kod, Instagram hesaplarından içerik indirme işlemlerini basit ve kullanıcı dostu bir şekilde gerçekleştiren etkileyici bir Python programıdır. Kullanıcı dostu menü seçenekleri sayesinde, Instagram içeriklerini indirme işlemi hızlı ve kolay bir şekilde tamamlanabilir.
