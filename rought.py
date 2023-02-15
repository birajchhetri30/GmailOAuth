datetime = "Wed, 21 Dec 2022 09:45:43 -0800 (PST)"
date = datetime[5:16].replace(" ", "-")
time = datetime[17:-12]
print(time)