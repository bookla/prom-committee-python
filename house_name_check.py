house_names = """
B13:
Poom Kecharananta (Student)
Ingke Samranyoo (Student)
Nene Chaipornvadee (Student)
Andy Jittarat (Student)
Knight Ponghathaikul (Student)
Ploy Surasingtothong (Student)
Frame Hiransrisoontorn (Student)
Bun Dhitavat (Student)
Guy Kaewsringam (Student)
Krit Somboon (Student)
Angelina Lim (Student)
Ken Synsukpermpoon (Student)
Phukhao Poolsawat (Student)
Copter Sesavej (Student)

C13:
Kaopod Ladavalya (Student)
Piam Fuang-Arom (Student)
Dol Jutasompakorn (Student)
Tong Pramoj (Student)
Prae Vichaidith (Student)
Un-Un Visukamol (Student)
Ike Bodhidatta (Student)
Proud Kitnichiva (Student)
William Wollmann (Student)
Cesar Chunharatchapan (Student)
Aim Ruangpattana (Student)
Lavik Hour (Student)
Mai Kitcharoenwong (Student)
Ray Supornsahusrungsi (Student)
Jaehwan Kim (Student)

K13:
Momo Ota (Student)
Jeffy Chotiwitsavaitkul (Student)
Pike Amornchat (Student)
All Ruangkanchanasetr (Student)
Erika Laungjessadakun (Student)
Punpun Sukanonsawas (Student)
Jun Suh (Student)
Tang-Tai Petsuksomvilai (Student)
Minnie Putamadilok (Student)
Farhan Ali (Student)
Josh Lingham (Student)
Lala Somsuwansak (Student)
Copter Sriworakun (Student)
Ben Anivat (Student)
Pat Charnvirakul (Student)
May Aurluecha (Student)
Oak Chivatxaranukul (Student)
Trey Chaney (Student)
Steph Hoffmann (Student)

N13:
Pear Punsri (Student)
Memee Jirapojaphorn (Student)
Finlay Prout (Student)
Nont Phucharoenyos (Student)
Anna Boscher (Student)
Thomas Laohapornsvan (Student)
Kent Masters (Student)
Max Prasertsan (Student)
May Viratikul (Student)
FongFong Hosakul (Student)
Temmy Luangtana-anan (Student)
Annabel Jennings-Chick (Student)
L.A. Kulsubsatit (Student)
Tim Vichit-vadakan (Student)


So13:
Pham Deevilaiphan (Student)
Pear Masathienvong (Student) 
Brew Piyawalaluck (Student) 
Henry To (Student) 
Sea Chanchaiwwichai (Student) 
Serene Boonnasitha (Student) 
Brian Chung (Student) 
Ken Kuwabara (Student) 
Prem Sirisuttinunt (Student) 
Ruby Qu (Student) 
Danial Yahaya (Student) 

S13:
Pooh Makingrilas (Student)
Bambi Kiatanant (Student)
March Bunluesak (Student)
Prance Thongyai Na Ayudhaya (Student)
Peter Niramitsiripong (Student)
Pang Sukhee (Student)
Perry Sato (Student)
Nikko Juengsophonvitavas (Student)
Primmy Titipunya (Student)
Chada Lovisuth (Student)
Arm Tubtimthongchai (Student)
Pony Karnplumchit (Student)
Pun Kamthornthip (Student)
JiSeon Park (Student)
Thund Owarang (Student)
Sweety Moe (Student)
"""

names = ['Aim Ruangpattana', 'All Ruangkanchanasetr', 'Andy Jittarat', 'Angelina Lim', 'Anna Boscher', 'Annabel Jennings-Chick', 'Arm Tubtimthongchai', 'Bambi Kiatanant', 'Ben Anivat', 'Brew Piyawalaluck', 'Brian Chung', 'Bun Dhitavat', 'Cesar Chunharatchapan', 'Chada Lovisuth', 'Copter Sesavej', 'Copter Sriworakun', 'Danial Yahaya', 'Dol Jutasompakorn', 'Erika Laungjessadakun', 'Farhan Ali', 'Fern Bulakul', 'Finlay Prout', 'Frame Hiransrisoontorn', 'Guy Kaewsringam', 'Henry To', 'Ike Bodhidatta', 'Ingke Samranyoo', 'Jaehwan Kim', 'Jeffy Chotiwitsavaitkul', 'Sunny Park', 'Josh Lingham', 'Jun Suh', 'Kaopod Ladavalya', 'Ken Kuwabara', 'Ken Synsukpermpoon', 'Kent Masters', 'Knight Ponghathaikul', 'Krit Somboon', 'Lala Somsuwansak', 'Lavik Hour', 'Mai Kitcharoenwong', 'March Bunluesak', 'Max Prasertsan', 'May Aurluecha', 'May Viratikul', 'Memee Jirapojaphorn', 'Minnie Putamadilok', 'Momo Ota', 'Nene Chaipornvadee', 'Nikko Juengsophonvitavas', 'Nont Phucharoenyos', 'Oak Chivatxaranukul', 'Pang Sukhee', 'Pat Charnvirakul', 'Pear Masathienvong', 'Pear Punsri', 'Perry Sato', 'Peter Niramitsiripong', 'Pham Deevilaiphan', 'Phukhao Poolsawat', 'Piam Fuang-Arom', 'Pike Amornchat', 'Ploy Surasingtothong', 'Pony Karnplumchit', 'Pooh Makingrilas', 'Poom Kecharananta', 'Prae Vichaidith', 'Prance Thongyai Na Ayudhaya', 'Prem Sirisuttinunt', 'Primmy Titipunya', 'Proud Kitnichiva', 'Pun Kamthornthip', 'Punpun Sukanonsawas', 'Ray Supornsahusrungsi', 'Ruby Qu', 'Sea Chanchaiwwichai', 'Serene Boonnasitha', 'Steph Hoffmann', 'Sweety Moe', 'Tang-Tai Petsuksomvilai', 'Temmy Luangtana-anan', 'Thomas Laohapornsvan', 'Thund Owarang', 'Tim Vichit-vadakan', 'Tong Pramoj', 'Trey Chaney', 'Un-Un Visukamol',  'William Wollmann']

existing_names = []
for each_line in house_names.split("\n"):
    if each_line == "" or ":" in each_line:
        continue
    existing_names.append(each_line.replace(" (Student)", "").replace("\u2028", ""))

print(existing_names)

missing_names = []
for each_name in names:
    if each_name not in existing_names:
        missing_names.append(each_name)
for each_missing in missing_names:
    print(each_missing)