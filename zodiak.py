def zodiak_checker(tanggal, bulan):
    if (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
        return "Aries"
    elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
        return "Taurus"
    elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
        return "Gemini"
    elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
        return "Cancer"
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        return "Leo"
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        return "Virgo"
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        return "Libra"
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
        return "Scorpio"
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
        return "Sagittarius"
    elif (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        return "Capricorn"
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def print_zodiak_ascii_art():
    print("""
 _____         _ _               ____ _               _             
|__  /___   __| (_) __ _  ___   / ___| |__   ___  ___| | _____ _ __ 
  / // _ \ / _` | |/ _` |/ __| | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 / /| (_) | (_| | | (_| | (__  | |___| | | |  __/ (__|   <  __/ |   
/____\___/ \__,_|_|\__,_|\___|  \____|_| |_|\___|\___|_|\_\___|_|     
    """)

# Main program
while True:
    print_zodiak_ascii_art()

    tanggal_lahir = int(input("Masukkan tanggal lahir: "))
    bulan_lahir = int(input("Masukkan bulan lahir (dalam angka): "))

    zodiak = zodiak_checker(tanggal_lahir, bulan_lahir)
    print(f"Zodiak Anda adalah {zodiak}.")

    ulang = input("Apakah Anda ingin Mengecek Zodiac lagi? (Y/T): ").upper()
    if ulang != 'Y':
        break
