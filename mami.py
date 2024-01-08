import tkinter as tk
from tkinter import ttk

def execute_commands(commands):
    for command in commands:
        try:
            exec(command)
        except Exception as e:
            print(f"Hata oluştu: {e}")

def update_font_size(event=None):
    screen_width = root.winfo_screenwidth()

    # Başlık yazı boyutunu ekran genişliğine göre ayarla
    title_font_size = int(min(screen_width / 25, screen_width / len(title_text)))
    title_label.configure(font=('Arial', title_font_size))

# Ana pencere oluşturuluyor
root = tk.Tk()
root.title("WİAM TOOL - DİSCORD HERŞEY")

# Ekran boyutunu al
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Pencereyi tam ekran yap
root.attributes('-fullscreen', True)

# Arka plan rengi koyu mor yapılıyor
root.configure(bg="#2E0854")

# Başlık için etiket oluşturuluyor
title_text = "WİAM TOOL - DİSCORD HERŞEY"
title_font_size = int(min(screen_width / 25, screen_width / len(title_text)))
title_label = ttk.Label(root, text=title_text, font=('Arial', title_font_size), background="#2E0854", foreground="white")
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))  # pady ile üst boşluğu ayarla

# Stil oluşturuluyor
style = ttk.Style()

# Normal durum için stil (koyu mor)
button_font_size = int(screen_width / 50)
style.configure('TButton', padding=(20, 10), background='#2E0854', foreground='white', font=('Arial', button_font_size))

# Farenin üzerine gelindiğinde stil (açık mor)
style.map('TButton', background=[('active', '#4B0082')])

# Seçenekler için 10 tane buton ve her birine özel komut ekleniyor
button_commands = {
    "Button 1": ["print('Button 1 - Komut 1')", "print('Button 1 - Komut 2')"],
    "Button 2": ["print('Button 2 - Komut 1')", "print('Button 2 - Komut 2')"],
    "Button 3": ["print('Button 3 - Komut 1')", "print('Button 3 - Komut 2')"],
    "Button 4": ["print('Button 4 - Komut 1')", "print('Button 4 - Komut 2')"],
    "Button 5": ["print('Button 5 - Komut 1')", "print('Button 5 - Komut 2')"],
    "Button 6": ["print('Button 6 - Komut 1')", "print('Button 6 - Komut 2')"],
    "Button 7": ["print('Button 7 - Komut 1')", "print('Button 7 - Komut 2')"],
    "Button 8": ["print('Button 8 - Komut 1')", "print('Button 8 - Komut 2')"],
    "Button 9": ["print('Button 9 - Komut 1')", "print('Button 9 - Komut 2')"],
    "Button 10": ["print('Button 10 - Komut 1')", "print('Button 10 - Komut 2')"],
}

buttons = []

# Butonların renkleri koyu mor
button_font_size = int(screen_width / 50)
button_style = ttk.Style()
button_style.configure('TButton', padding=(20, 10), background='#2E0854', foreground='white', font=('Arial', button_font_size))
button_style.map('TButton', background=[('active', '#4B0082')])

# Butonları oluştur ve grid'e yerleştir
columns = 2
rows = (len(button_commands) + columns - 1) // columns

for i, (text, commands) in enumerate(button_commands.items()):
    command = lambda cmds=commands: execute_commands(cmds)
    button = ttk.Button(root, text=text, command=command, style='TButton')
    button.grid(row=(i // columns) + 1, column=i % columns, padx=10, pady=5)  # row ile başlık için ayrı bir satır kullanıldı
    buttons.append(button)

# Grid düzenini ayarla
for i in range(columns):
    root.columnconfigure(i, weight=1)

for i in range(rows + 1):  # Başlık için bir satır daha eklenmişti, bu nedenle rows + 1 kullanıldı
    root.rowconfigure(i, weight=1)

# Pencere boyutu değiştikçe başlık yazı boyutunu güncelle
root.bind("<Configure>", update_font_size)

# Pencereyi göster
root.mainloop()
