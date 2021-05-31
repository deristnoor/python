# Soal exercise 05 session 03

# Jarak mobil A dan B = 120 km
# A berjalan 60km/h dari Timur 
# B berjalan 40km/h dari barat
# A dan B start pukul 9 WIB
# jam berapa A dan B bertemu?

# 60 km/h + 40 km/h = 100 km/h
# 120 km / 100 km/h = 1.2 h
# 0.2 h = 12 minute
# bertemu setelah 1 h 12 m

import math

initial_time =  9
distance = 120
total_velocity_per_hour = 100

duration = distance / total_velocity_per_hour
duration_hour = math.floor(distance / total_velocity_per_hour)
duration_minute = math.ceil((duration - duration_hour) * 60)
hour = 9 + duration_hour
minute = duration_minute

txt = "Mobil A dan Mobil B akan bertemu setelah perjalanan {} jam {} menit, pada pukul {}:{}"
print(txt.format(duration_hour, duration_minute, hour, minute))