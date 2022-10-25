import instaloader
from instaloader import Post

def downloadFull():
    test = instaloader.Instaloader()
    acc = input('Enter username: ')
    print('Please wait, it may take a few minutes to download...')
    test.download_profile(acc, profile_pic_only=False)
    
def downloadByURLPost():
    url = input("Enter instagram post URL: ")
    print('Please wait, it may take a few minutes to download...')
    shorted_url = url[28:len(url) - 1]
    i = instaloader.Instaloader()                                              
    post = Post.from_shortcode(i.context, shorted_url)
    i.download_post(post, target='download_file')
    
def main():
    choice = input('[1]-Download full, [2]-Download by URL post: ')
    if choice == '1':
        downloadFull()
    elif choice == '2':
        downloadByURLPost()
    else:
        print('invalid choice')

if __name__ == '__main__':
    main()