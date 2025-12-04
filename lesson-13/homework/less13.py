#1
from datetime import datetime
from dateutil.relativedelta import relativedelta

birthday = str(input('tug`ilgan kunni oyni va yilni kirit(YYYY-MM-DD)'))

today = datetime.now()

age_date = datetime.strptime(birthday,'%Y-%m-%d')

age = relativedelta(today,age_date)

print(f'Sizning yoshingiz: {age.years} yil, {age.months} oy va {age.days} kun')


#2
from datetime import datetime

tugilgan_sana = str(input('yyyy-mm-dd'))

today = datetime.now()

birth_date = datetime.strptime(tugilgan_sana,'%Y-%m-%d')

next_birthday = birth_date.replace(year=today.year)

if next_birthday < today:
    next_birthday = birth_date.replace(year=today.year+1)

days_left = (next_birthday-today).days


print(f"Keyingi tug'ilgan kuningizgacha {days_left} kun qoldi.")



#3
from datetime import datetime

time_str = str(input('yyyy-mm-dd hh:mm'))

time_date = datetime.strptime(time_str,'%Y-%m-%d %H:%M')

soat = int(input('soatni kirit'))
minut = int(input('min ni kirit'))

davomiylik = timedelta(hours=soat,minutes=minut)

tugash = time_date + davomiylik

print(f'Uchrashuv to`gash vaqt:\n{tugash}')


#4
from datetime import datetime
import pytz

# 1) Userdan sana va vaqt olish
datetime_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")

# 2) Userdan joriy timezone
current_tz_str = input("Hozir qaysi timezone-dasiz? (masalan: Asia/Tashkent): ")

# 3) Userdan qaysi timezone-ga o'tkazmoqchisiz
target_tz_str = input("Qaysi timezone-ga o‘tkazmoqchisiz? (masalan: Europe/London): ")

# 4) Stringni datetimega aylantiramiz
user_dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

# 5) Timezone obyektlari yaratish
current_tz = pytz.timezone(current_tz_str)
target_tz = pytz.timezone(target_tz_str)

# 6) Sana-vaqtni joriy timezone-ga bog‘lash
localized_dt = current_tz.localize(user_dt)

# 7) Boshqa timezone-ga o‘tkazish
converted_dt = localized_dt.astimezone(target_tz)

# 8) Natija chiqarish
print("\nNatija:")
print("Yangi timezone dagi vaqt:", converted_dt.strftime("%Y-%m-%d %H:%M"))



#5
from datetime import datetime
import time

# 1) Foydalanuvchidan kelajak sana-vaqtni olish
future_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")

# 2) String → datetime ga aylantirish
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

print("\nCountdown boshlandi...\n")

# 3) Timer
while True:
    now = datetime.now()
    diff = future_time - now

    # Agar vaqt tugagan bo'lsa
    if diff.total_seconds() <= 0:
        print("⏰ Vaqt tugadi!")
        break

    # Kun, soat, minut, sekundni ajratish
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Qolgan vaqt: {days} kun, {hours} soat, {minutes} minut, {seconds} sekund", end="\r")

    time.sleep(1)  # Har 1 sekundda yangilash



#6
import re

email = input('email kirit(name@gamil.com)')

pattern = r"^[a-yA-Y._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern,email):
    print('email to`g`ri')
else:
    print('xatolik bor qayta tekshir')


#7
import re

phone = input('telefon (10 tadan oshmasin)')

natija = re.sub(r'\D','',phone)

if len(phone) != 10:
    print("Telefon raqam 10 ta raqamdan iborat bo‘lishi kerak!")
else:
    tayyor = f'({natija[0:3]}) {natija[3:6]}-{natija[6:10]}'
    print("Formatlangan raqam:", tayyor)



#8
import re

kod = input('kodni kirit')

len_ok = len(kod)>=8
upper = re.search(r'[A-Y]',kod) is not None
lower = re.search(r'[a-y]',kod) is not None
digit = re.search(r'\D',kod) is not None

if len_ok and upper and lower and digit:
    print("parol kuchli")
else:
    print("Parol zaif! ✘")
    if not len_ok:
        print("- Parol kamida 8 belgidan iborat bo'lishi kerak.")
    if not upper:
        print("- Kamida bitta KATTA harf bo'lishi kerak.")
    if not lower:
        print("- Kamida bitta kichik harf bo'lishi kerak.")
    if not digit:
        print("- Kamida bitta raqam bo'lishi kerak.")


#9
import re

# 1) Sample text (matn)
text = """
Python is a powerful programming language. 
Many people use Python for data analysis, machine learning, and automation. 
Python is simple yet very effective.
"""

# 2) Userdan so'zni olish
word = input("Qaysi so'zni qidiramiz? ")

# 3) Regex orqali hamma uchrashuvlarni topish (case-insensitive)
pattern = rf"\b{word}\b"   # faqat to'liq so'zni izlaydi
matches = re.findall(pattern, text, flags=re.IGNORECASE)

# 4) Natijani chiqarish
if matches:
    print(f"\nMatnda '{word}' so'zi {len(matches)} marta uchradi.")
else:
    print(f"\n'{word}' so'zi matnda topilmadi.")



#10
import re

# 1) Userdan matn olish
text = input("Matn kiriting: ")

# 2) Sana formatlarini aniqlaydigan regex patternlar
pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}[/-]\d{2}[/-]\d{4}\b"

# 3) Barcha sanalarni topish
dates = re.findall(pattern, text)

# 4) Natijani chiqarish
if dates:
    print("\nTopilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("\nMatnda sana topilmadi.")

