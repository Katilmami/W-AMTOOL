import subprocess
import time

def run_background_command(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Windows'ta color komutu kullanma örneği
color_command = 'color a'  # 0a renk kodu, siyah zemin üzerine yeşil yazı demektir
run_background_command(color_command)

# Programın durmaması için bir bekleme ekleyebilirsiniz
time.sleep(5)  # Örnek olarak 5 saniye boyunca bekleyelim

# Ardından diğer işlemlerinizi devam ettirebilirsiniz
print("Program devam ediyor.")
