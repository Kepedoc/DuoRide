import subprocess

def play_mp3():
    subprocess.Popen(['mpg123','-q', "/home/keped/Dev/python/usb.mp3"]).wait()

prevUsb = subprocess.run('lsusb', capture_output=True, text=True)

try:
    while True:
        usb = subprocess.run('lsusb', capture_output=True, text=True)

        if prevUsb.stdout == usb.stdout:
            pass
        else:
            play_mp3()
            prevUsb = usb
except Exception as e:
    print(e)

