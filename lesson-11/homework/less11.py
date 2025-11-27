# TASK 1
import os
import subprocess
import sys

# 1. Virtual environment nomi
venv_name = "venv"

# 2. venv yaratish
print(">>> Virtual environment yaratilyapti...")
subprocess.run([sys.executable, "-m", "venv", venv_name])

# 3. Platformani aniqlash
if os.name == "nt":  # Windows
    activate_path = f"{venv_name}\\Scripts\\activate"
else:  # Mac/Linux
    activate_path = f"source {venv_name}/bin/activate"

print(f">>> Virtual environment yaratildi: {venv_name}")
print(f">>> Uni quyidagi buyruq bilan faollashtirasiz:\n{activate_path}\n")

# 4. Paket o‘rnatish
packages = ["requests", "numpy", "pandas"]  # kerakli paketlar ro‘yxati

print(">>> Paketlar o‘rnatilyapti...")
subprocess.run([f"{venv_name}/bin/pip" if os.name != "nt" else f"{venv_name}\\Scripts\\pip.exe", "install", *packages])

print(">>> Hammasi tayyor!")



#TASK 2

#A)
import math_operations as mo

mo.add(10,20)

mo.divide(30,5)

#B)
import stringg_utils as su


print(su.count_vowels('sardor'))

print(su.reverse_string('sardor'))



#TASK 3

#A)
import geometry.circle as c


print(c.calculate_area(10))

print(c.calculate_circumference(20))


#B)
import file_operations.file_reader as gr

print(gr.read_file('my_modul.py'))

print(gw.write_file('newt_file.txt','hello'))






