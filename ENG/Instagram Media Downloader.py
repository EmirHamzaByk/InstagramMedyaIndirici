import instaloader
import os

test = instaloader.Instaloader()
test.context.save_metadata = False

try:
    acc = input('Enter User Name-->> ')
    test.context.log("Saving photos to 'Instagram/Photos' directory")
    test.dirname_pattern = 'Instagram/Photos/{profile}'
    test.context.log("Saving videos to 'Instagram/Videos' directory")

    download_all = input('If you want to download profile picture only type "pp"\nIf you want to download all photos of the user type "f"(This feature will not work on private accounts!!!)\n(PP/F)-->>  ')
    if download_all.lower() == "pp":
        test.download_profile(acc, profile_pic_only=True)
        print("Your profile picture has been saved here --> Directory : Instagram/Photos/{}".format(acc))
    else:
        download_videos = input("Do you want to download videos too? (Y/N): ")
        if download_videos.lower() == "y":
            test.download_profile(acc)
            test.download_videos(acc, targetfolder="Instagram/Videos")
            print("All photos and videos have been saved here --> Directory : Instagram/Photos/{} and Instagram/Videos".format(acc))
        else:
            test.download_profile(acc)
            print("All photos have been saved here -->> Directory : Instagram/Photos/{}".format(acc))

except instaloader.exceptions.ProfileNotExistsException:
    print("Profile does not exist.")
except instaloader.exceptions.CookieError:
    print("Unfortunately, you cannot download photos from a private account.")
except instaloader.exceptions.LoginRequiredException:
    print("Login Required.")
except instaloader.exceptions.InvalidArgumentException:
    print("Account not found.")
except:
    print("An error occurred.")