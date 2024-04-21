import os
import subprocess
import ctypes
import yt-dlp # Important

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def is_link_allowed(link):
    allowed_domains = ['youtu.be/', 'youtube.com/watch?v=']
    return any(domain in link for domain in allowed_domains)

def download_video(video_url):
    if not is_link_allowed(video_url):
        print('Error: The site you provided isn\'t allowed.')
        input('Press Enter to continue...')
        return False

    output_dir = os.path.join(os.getenv('USERPROFILE'), 'Videos', 'YouTube')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = f'yt-dlp -f "bestvideo+bestaudio" --merge-output-format mp4 -o "{output_dir}/%(title)s.%(ext)s" "{video_url}"'
    subprocess.run(command, shell=True)

    print('\nVideo downloaded successfully.')
    return True

def main():
    set_console_title("YouTube Video Downloader")  # Set console window title

    while True:
        output_dir = os.path.join(os.getenv('USERPROFILE'), 'Videos', 'YouTube')
        os.system('cls' if os.name == 'nt' else 'clear')
        print('--------------------------------------------------')
        print('          YouTube Video Downloader')
        print('--------------------------------------------------')
        print()
        print(f'The downloaded file will be saved to {os.path.join(os.getenv("USERPROFILE"), "Videos", "YouTube")}')
        video_url = input('Enter the YouTube video URL: ')

        if download_video(video_url):
            input('Press Enter to exit...')
            subprocess.run(['start', '', output_dir], shell=True)
            break

if __name__ == '__main__':
    main()
