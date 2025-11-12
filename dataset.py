import pandas as pd
from io import StringIO

# Full dataset as a string
data = """
Country,City,Place Name,Category,Rating,Popularity
Jordan,Petra,Petra Archaeological Site,Historical,5,High
Jordan,Amman,Amman Citadel,Historical,4,High
Jordan,Aqaba,Aqaba Beach,Natural,4,Medium
Jordan,Dead Sea,Dead Sea Resort,Natural,5,High
Jordan,Wadi Rum,Wadi Rum Desert,Natural,5,High
Jordan,Madaba,Madaba Mosaic Map,Historical,4,Medium
Jordan,Jerash,Jerash Ruins,Historical,4,Medium
Jordan,Ajloun,Ajloun Castle,Historical,4,Medium
Jordan,Karak,Karak Castle,Historical,3,Medium
Jordan,Al-Salt,Historic Downtown,Historical,4,Medium
Lebanon,Beirut,National Museum,Cultural,4,High
Lebanon,Byblos,Byblos Castle,Historical,4,Medium
Lebanon,Baalbek,Baalbek Temples,Historical,5,High
Lebanon,Tyre,Tyre Beach,Natural,4,Medium
Lebanon,Jeita,Jeita Grotto,Natural,5,High
Lebanon,Beirut,Hamra Street,Cultural,4,High
Lebanon,Zahlé,Kantara Valley,Natural,3,Medium
Lebanon,Sidon,Sidon Sea Castle,Historical,4,Medium
Lebanon,Tripoli,Tripoli Souk,Cultural,4,High
Lebanon,Ehden,Ehden Forest,Natural,4,Medium
Syria,Damascus,Umayyad Mosque,Religious,5,High
Syria,Palmyra,Palmyra Ruins,Historical,5,High
Syria,Aleppo,Citadel of Aleppo,Historical,4,High
Syria,Lattakia,Beach Resort,Natural,4,Medium
Syria,Hama,Water Wheels,Historical,4,Medium
Syria,Homs,Al-Qusayr Castle,Historical,3,Medium
Syria,Dara,Ancient Ruins,Historical,3,Low
Syria,Tartus,Tartus Port,Cultural,3,Medium
Syria,Ma'loula,Monastery,Religious,4,Medium
Syria,Idlib,Serjilla Village,Historical,3,Low
Palestine,Jerusalem,Al-Aqsa Mosque,Religious,5,High
Palestine,Bethlehem,Birth Church,Religious,5,High
Palestine,Hebron,Old City,Historical,4,Medium
Palestine,Nablus,Jacob's Well,Religious,4,Medium
Palestine,Ramallah,Museum,Cultural,3,Medium
Palestine,Gaza,Seashore,Natural,3,Medium
Palestine,Jenin,Archaeological Site,Historical,3,Low
Palestine,Tulkarm,Old Market,Cultural,3,Low
Palestine,Qalqilya,Local Park,Natural,3,Low
Palestine,Jericho,Hisham Palace,Historical,4,Medium
Saudi Arabia,Riyadh,Masmak Fort,Historical,4,High
Saudi Arabia,Mecca,Grand Mosque,Religious,5,High
Saudi Arabia,Medina,Prophet's Mosque,Religious,5,High
Saudi Arabia,Jeddah,Red Sea Mall,Cultural,4,Medium
Saudi Arabia,Dammam,Dhahran Beach,Natural,3,Medium
Saudi Arabia,Al-Ula,Madain Saleh,Historical,5,High
Saudi Arabia,Taif,Rose Gardens,Natural,4,Medium
Saudi Arabia,Abha,Al-Soudah Park,Natural,4,Medium
Saudi Arabia,Al Khobar,Corniche,Natural,4,Medium
Saudi Arabia,Diriyah,Historic Centre,Historical,4,Medium
UAE,Abu Dhabi,Sheikh Zayed Mosque,Religious,5,High
UAE,Dubai,Burj Khalifa,Entertainment,5,High
UAE,Dubai,Dubai Mall,Entertainment,5,High
UAE,Sharjah,Sharjah Museum,Cultural,4,Medium
UAE,Fujairah,Fujairah Fort,Historical,4,Medium
UAE,Ras Al Khaimah,Jebel Jais,Natural,5,High
UAE,Abu Dhabi,Louvre Abu Dhabi,Cultural,5,High
UAE,Dubai,Marina Walk,Natural,4,High
UAE,Ajman,Ajman Beach,Natural,4,Medium
UAE,Umm Al Quwain,Umm Al Quwain Fort,Historical,3,Medium
Qatar,Doha,Museum of Islamic Art,Cultural,5,High
Qatar,Doha,The Pearl,Entertainment,4,High
Qatar,Doha,Doha Corniche,Natural,5,High
Qatar,Al Khor,Khor Al Adaid,Natural,4,Medium
Qatar,Al Wakrah,Al Wakrah Souq,Cultural,4,Medium
Qatar,Doha,Katara Cultural Village,Cultural,5,High
Qatar,Doha,National Library,Cultural,4,Medium
Qatar,Al Shamal,Farm Visits,Natural,3,Low
Qatar,Al Rayyan,Sheikh Faisal Museum,Cultural,4,Medium
Qatar,Doha,Mathaf Museum,Cultural,4,Medium
Kuwait,Kuwait City,Kuwait Towers,Natural,5,High
Kuwait,Kuwait City,Grand Mosque,Religious,5,High
Kuwait,Al Ahmadi,Oil Museum,Cultural,4,Medium
Kuwait,Kuwait City,Mall of Kuwait,Entertainment,4,Medium
Kuwait,Kuwait City,Seef Palace,Historical,3,Medium
Kuwait,Failaka Island,Archaeological Site,Historical,4,Medium
Kuwait,Kuwait City,Marina Beach,Natural,4,High
Kuwait,Salmiya,Marina Mall,Entertainment,4,Medium
Kuwait,Al Jahra,Al Jahra Fort,Historical,3,Low
Kuwait,Al Ahmadi,Lube Oil Museum,Cultural,3,Low
Bahrain,Manama,Bahrain National Museum,Cultural,5,High
Bahrain,Manama,Bab Al Bahrain,Historical,4,High
Bahrain,Manama,Bahrain Fort,Historical,4,High
Bahrain,Sitra,Al Dar Islands,Natural,4,Medium
Bahrain,Muharraq,Shrine of Pearl,Religious,3,Medium
Bahrain,Manama,Adliya District,Cultural,4,Medium
Bahrain,Riffa,Riffa Fort,Historical,3,Medium
Bahrain,Amwaj Islands,Beach,Natural,4,Medium
Bahrain,Budaiya,Al Dar Gardens,Natural,3,Low
Bahrain,Manama,Dhow Harbour,Natural,3,Medium
Oman,Muscat,Sultan Qaboos Grand Mosque,Religious,5,High
Oman,Muscat,Mutrah Souq,Cultural,4,High
Oman,Nizwa,Nizwa Fort,Historical,4,Medium
Oman,Salalah,Al Baleed Archaeological Park,Historical,4,Medium
Oman,Jebel Shams,Mountain Park,Natural,5,High
Oman,Muscat,Qurum Beach,Natural,4,High
Oman,Sur,Traditional Dhow Factory,Cultural,4,Medium
Oman,Muscat,Royal Opera House,Cultural,5,High
Oman,Nakhal,Nakhal Fort,Historical,4,Medium
Oman,Salalah,Frankincense Land,Natural,4,Medium
Morocco,Marrakech,Jemaa el-Fnaa,Cultural,5,High
Morocco,Fez,Al-Attarine Madrasa,Historical,4,High
Morocco,Casablanca,Hassan II Mosque,Religious,5,High
Morocco,Rabat,Rabat Kasbah,Historical,4,Medium
Morocco,Chefchaouen,Blue City,Natural,4,Medium
Morocco,Agadir,Agadir Beach,Natural,4,Medium
Morocco,Essaouira,Medina,Cultural,4,Medium
Morocco,Meknes,Meknes Medina,Historical,4,Medium
Morocco,Ouarzazate,Ait Benhaddou,Historical,5,High
Morocco,Tangier,Cape Spartel,Natural,4,Medium
Libya,Tripoli,Red Castle Museum,Historical,4,Medium
Libya,Leptis Magna,Leptis Magna Ruins,Historical,5,High
Libya,Derna,Derna Beach,Natural,4,Medium
Libya,Al Khums,Leptis Magna Ruins,Historical,4,Medium
Libya,Sirte,Sirte Corniche,Natural,3,Medium
Libya,Ghadames,Ghadames Old Town,Historical,4,Medium
Libya,Benghazi,Benghazi Museum,Cultural,3,Medium
Libya,Misrata,Beach,Natural,3,Medium
Libya,Tobruk,Tobruk Fort,Historical,3,Low
Libya,Tripoli,Martyrs' Square,Cultural,3,Medium
Algeria,Algiers,Kasbah of Algiers,Historical,5,High
Algeria,Oran,Oran Medina,Cultural,4,Medium
Algeria,Tipaza,Tipaza Ruins,Historical,4,Medium
Algeria,Tlemcen,Tlemcen National Park,Natural,4,Medium
Algeria,Constantine,Constantine Bridges,Historical,4,Medium
Algeria,Annaba,St. Augustine Basilica,Religious,3,Medium
Algeria,Setif,Setif Roman Ruins,Historical,3,Medium
Algeria,Béjaïa,Béjaïa Beach,Natural,4,Medium
Algeria,Oran,Fort Santa Cruz,Historical,4,Medium
Algeria,Algiers,Basilique Notre-Dame d'Afrique,Religious,4,Medium
Tunisia,Tunis,Bardo Museum,Cultural,5,High
Tunisia,Cartage,Carthage Ruins,Historical,5,High
Tunisia,Sousse,Ribat of Sousse,Historical,4,High
Tunisia,Hammamet,Hammamet Beach,Natural,4,Medium
Tunisia,Kairouan,Great Mosque,Religious,5,High
Tunisia,Monastir,Monastir Marina,Natural,4,Medium
Tunisia,El Jem,El Jem Amphitheatre,Historical,5,High
Tunisia,Djerba,Djerba Island,Natural,4,Medium
Tunisia,Sfax,Mediterranean Port,Natural,3,Medium
Tunisia,Tunis,Medina of Tunis,Cultural,4,High
Egypt,Cairo,Pyramids of Giza,Historical,5,High
Egypt,Luxor,Luxor Temple,Historical,5,High
Egypt,Aswan,Philae Temple,Historical,4,High
Egypt,Hurghada,Hurghada Beach,Natural,4,Medium
Egypt,Alexandria,Library of Alexandria,Cultural,4,Medium
Egypt,Sharm El Sheikh,Ras Mohammed,Natural,5,High
Egypt,Cairo,Egyptian Museum,Cultural,4,High
Egypt,Luxor,Valley of the Kings,Historical,5,High
Egypt,Sohag,White Monastery,Religious,3,Medium
Egypt,Cairo,Khan El Khalili Bazaar,Cultural,4,High
Turkey,Istanbul,Hagia Sophia,Historical,5,High
Turkey,Istanbul,Blue Mosque,Religious,5,High
Turkey,Izmir,Ephesus,Historical,5,High
Turkey,Antalya,Antalya Beach,Natural,4,High
Turkey,Cappadocia,Cave Hotels,Natural,5,High
Turkey,Konya,Mevlana Museum,Cultural,4,Medium
Turkey,Ankara,Anitkabir,Historical,4,High
Turkey,Bodrum,Bodrum Castle,Historical,4,Medium
Turkey,Istanbul,Grand Bazaar,Cultural,5,High
Turkey,Pamukkale,Travertine Pools,Natural,5,High
"""

# Read as CSV
df = pd.read_csv(StringIO(data))

# Save to CSV file
df.to_csv("data.csv", index=False)

print("Full CSV file created successfully!")