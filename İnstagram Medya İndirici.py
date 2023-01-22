import instaloader
import os

test = instaloader.Instaloader()
test.context.save_metadata = False

try:
    acc = input('Kullanıcı Adını girin--> ')
    test.context.log("Saving photos to 'İnstagram/Photos' directory")
    test.dirname_pattern = 'İnstagram/Photos/{profile}'
    test.context.log("Saving videos to 'İnstagram/Videos' directory")

    download_all = input('Sadece profil fotoğrafını indirmek istiyosanız "pp" yazın\nKullanıcının attığı tüm fotoğrafları indirmek istiyosanız "f" yazın(Bu özellik gizli hesaplarda çalışmaz!!!)\n(PP/F)-->> ')
    if download_all.lower() == "pp":
        test.download_profile(acc, profile_pic_only=True)
        print("Resminizi şuraya kaydettik --> Dizin : İnstagram/Photos/{}".format(acc))
    else:
        download_videos = input("Videolarıda indirmek istiyor musunuz? (E/H): ")
        if download_videos.lower() == "e":
            test.download_profile(acc)
            test.download_videos(acc, targetfolder="İnstagram/Videos")
            print("Tüm fotoğrafları ve videoları şuraya kaydettik --> Dizin : İnstagram/Photos/{} ve İnstagram/Videos".format(acc))
        else:
            test.download_profile(acc)
            print("Tüm fotoğrafları şuraya kaydettik --> Dizin : İnstagram/Photos/{}".format(acc))

except instaloader.exceptions.ProfileNotExistsException:
    print("Profil mevcut değil.")
except instaloader.exceptions.CookieError:
    print("Hesap gizli olduğu için malesef fotoğraflarını indiremezsiniz.")
except instaloader.exceptions.LoginRequiredException:
    print("Login Required.")
except instaloader.exceptions.InvalidArgumentException:
    print("Böyle bir hesap bulunamadı.")
except:
    print("Bir hata oluştu.")

