import sys
from cx_Freeze import setup, Executable

# Uygulama adı ve versiyonu
application_name = "wiamtool"
application_version = "1.0"

# Uygulamanın çalıştığı ana dosya
main_script = "mami.py"

# setup fonksiyonu
setup(
    name=application_name,
    version=application_version,
    description="wiamtool",
    executables=[Executable(main_script)],
)
