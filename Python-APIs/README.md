
#Weather Analysis:
The analysis is based on current weather obtained on june 20 and june 21. 
The plot of latitude vs weather indicates that the temperature is highest near the tropic of cancer with latitude around 
23.5 deg N. T The maximum temperatures in the northern hemisphere falls considerably moving north of the 23.5 deg latitude 
and moving south from the equator at 0 deg. There is also a wide variation in the maximum temperatures around the world 
based on the latitude. The southern hemishphere experiences lower temperatures when it is  summer in  the northern hemisphere.


There does not seem to any correlation of latitude to cloudiness, windspeed or humidity. More historical analysis of weather data may be  needed to infer any correlations between latitude and cloudiness, windspeed or humidity. There does seem to be a concentration of data around 45-50 % humidity. This value is considered very conducive for humans. 


```python
#import required python libs.
import requests
import json
from pprint import pprint
from citipy import citipy
import random
import pandas as pd
import openweathermapy.core as owm
#import seaborn as sns
#config
from config import api_key
print(api_key)
```

    105bc2c8a00675ea3a807f619fd5e9cc
    


```python
#urlw for openweather
#url = "http://api.openweathermap.org/data/2.5/weather?"
cnt=0
latlist=list()
longlist=list()

for k in range(-180,181,20):
    longlist.append(k)
#longlist=[-180,-160,-140,-120,-100,-8-75,-50,0,50,75,100,150,175]

#list of cities
cityset=set()

#list of countries corresponding to the city.
cnylist=list()
#create list of longitudes for use as a random choice

for i in range(-90,90,+2):
#use latitude choice from -90 to +90 and get a city closest to that latitude.
    for j in longlist:
        lat=i
        long=j
        city = citipy.nearest_city(lat, long)
        cityset.add(city.city_name)
        cnylist.append(city.country_code)
print(str(len(cityset)))
print(str(len(cnylist)))

```

    555
    1710
    


```python
# Save config information.
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"

# Build partial query URL
query_url = f"{url}appid={api_key}&units={units}&q="
print(query_url)
#print(api_key)
```

    http://api.openweathermap.org/data/2.5/weather?appid=105bc2c8a00675ea3a807f619fd5e9cc&units=metric&q=
    


```python
# Get current weather for all the cities using openweathermapy. 
#initialize count variables. 
cntcity=0
cntfail=0
     
# set up lists to hold reponse info
citylist=list()
cloudiness=list()
temp = list()
cnycode=list()
date=list()
humidity=list()
lat = list()
long=list()
tempmax=list()
windspeed=list()

# Loop through the list of cities and perform a request for weather data on each city.store results in lists. 
for city in cityset:
    #print(str(city))
    cntcity=cntcity+1
    print("Retrieving  data for record " + str(cntcity) + " " + city)
    try:
        weatherdetails = requests.get(query_url + city).json()
        #pprint(weatherdetails)
        citylist.append (weatherdetails["name"])
        cloudiness.append (weatherdetails["clouds"]["all"])
        cnycode.append (weatherdetails["sys"]["country"])
        #datetime=weatherdetails["dt"]
        date.append (weatherdetails["dt"])
        humidity.append (weatherdetails["main"]["humidity"])
        lat.append (weatherdetails["coord"]["lat"])
        long.append (weatherdetails["coord"]["lon"])
        tempmax.append (weatherdetails["main"]["temp_max"])
        windspeed.append (weatherdetails["wind"]["speed"])
    except:
        cntfail +=1
        print("Error in getting data for city " + city)
        print("error code: " + weatherdetails["cod"])
        print("message: " + weatherdetails["message"])

pprint(weatherdetails)        
print("Data Retrieval Complete....")
print("---------------------------------------------------------")
print("Number of cities weather data  not found: " + str(cntfail))
```

    Retrieving  data for record 1 mogocha
    Retrieving  data for record 2 nizhneyansk
    Error in getting data for city nizhneyansk
    error code: 404
    message: city not found
    Retrieving  data for record 3 buala
    Retrieving  data for record 4 marcona
    Error in getting data for city marcona
    error code: 404
    message: city not found
    Retrieving  data for record 5 louisbourg
    Error in getting data for city louisbourg
    error code: 404
    message: city not found
    Retrieving  data for record 6 lucapa
    Retrieving  data for record 7 novo aripuana
    Retrieving  data for record 8 lixourion
    Retrieving  data for record 9 clyde river
    Retrieving  data for record 10 baixa grande
    Retrieving  data for record 11 mombasa
    Retrieving  data for record 12 khonuu
    Error in getting data for city khonuu
    error code: 404
    message: city not found
    Retrieving  data for record 13 port hedland
    Retrieving  data for record 14 karauzyak
    Error in getting data for city karauzyak
    error code: 404
    message: city not found
    Retrieving  data for record 15 reconquista
    Retrieving  data for record 16 sovetskaya gavan
    Retrieving  data for record 17 bandarbeyla
    Retrieving  data for record 18 makakilo city
    Retrieving  data for record 19 orlik
    Retrieving  data for record 20 chuy
    Retrieving  data for record 21 rungata
    Error in getting data for city rungata
    error code: 404
    message: city not found
    Retrieving  data for record 22 oussouye
    Retrieving  data for record 23 alyangula
    Retrieving  data for record 24 morag
    Retrieving  data for record 25 danilov
    Retrieving  data for record 26 guerrero negro
    Retrieving  data for record 27 upernavik
    Retrieving  data for record 28 ushuaia
    Retrieving  data for record 29 port hardy
    Retrieving  data for record 30 hovd
    Retrieving  data for record 31 delvine
    Retrieving  data for record 32 marin
    Retrieving  data for record 33 koumac
    Retrieving  data for record 34 crab hill
    Error in getting data for city crab hill
    error code: 404
    message: city not found
    Retrieving  data for record 35 pavilosta
    Retrieving  data for record 36 yoichi
    Retrieving  data for record 37 butaritari
    Retrieving  data for record 38 fushe-arrez
    Retrieving  data for record 39 bosobolo
    Retrieving  data for record 40 sokoni
    Retrieving  data for record 41 chase
    Retrieving  data for record 42 bubaque
    Retrieving  data for record 43 parana
    Retrieving  data for record 44 matranovak
    Retrieving  data for record 45 tolaga bay
    Retrieving  data for record 46 angoche
    Retrieving  data for record 47 ampanihy
    Retrieving  data for record 48 jamestown
    Retrieving  data for record 49 birjand
    Retrieving  data for record 50 kirkland lake
    Retrieving  data for record 51 iranshahr
    Retrieving  data for record 52 saurimo
    Retrieving  data for record 53 sawtell
    Retrieving  data for record 54 lyngseidet
    Retrieving  data for record 55 nacala
    Retrieving  data for record 56 bambous virieux
    Retrieving  data for record 57 cabra
    Retrieving  data for record 58 ayan
    Retrieving  data for record 59 severo-kurilsk
    Retrieving  data for record 60 abu kamal
    Retrieving  data for record 61 robe
    Retrieving  data for record 62 aksu
    Retrieving  data for record 63 bethel
    Retrieving  data for record 64 calvinia
    Retrieving  data for record 65 hollins
    Retrieving  data for record 66 vanimo
    Retrieving  data for record 67 broome
    Retrieving  data for record 68 constitucion
    Retrieving  data for record 69 fecamp
    Retrieving  data for record 70 koupela
    Retrieving  data for record 71 kanjiza
    Retrieving  data for record 72 geraldton
    Retrieving  data for record 73 severodvinsk
    Retrieving  data for record 74 jitauna
    Retrieving  data for record 75 osmena
    Retrieving  data for record 76 sturgeon falls
    Retrieving  data for record 77 shingu
    Retrieving  data for record 78 tumannyy
    Error in getting data for city tumannyy
    error code: 404
    message: city not found
    Retrieving  data for record 79 bluff
    Retrieving  data for record 80 pedernales
    Retrieving  data for record 81 moyale
    Retrieving  data for record 82 vaitupu
    Error in getting data for city vaitupu
    error code: 404
    message: city not found
    Retrieving  data for record 83 taolanaro
    Error in getting data for city taolanaro
    error code: 404
    message: city not found
    Retrieving  data for record 84 cayenne
    Retrieving  data for record 85 veinticinco de mayo
    Retrieving  data for record 86 coquimbo
    Retrieving  data for record 87 namatanai
    Retrieving  data for record 88 hermanus
    Retrieving  data for record 89 korem
    Retrieving  data for record 90 tres arroyos
    Retrieving  data for record 91 kiunga
    Retrieving  data for record 92 jalu
    Retrieving  data for record 93 laguna
    Retrieving  data for record 94 nizhniy tagil
    Retrieving  data for record 95 lishui
    Retrieving  data for record 96 kamennomostskiy
    Retrieving  data for record 97 nerchinskiy zavod
    Retrieving  data for record 98 lima
    Retrieving  data for record 99 mayor pablo lagerenza
    Retrieving  data for record 100 pangnirtung
    Retrieving  data for record 101 mosquera
    Retrieving  data for record 102 torbay
    Retrieving  data for record 103 souillac
    Retrieving  data for record 104 ajdabiya
    Retrieving  data for record 105 lethem
    Retrieving  data for record 106 mangai
    Retrieving  data for record 107 rongcheng
    Retrieving  data for record 108 lindi
    Retrieving  data for record 109 kiruna
    Retrieving  data for record 110 bayburt
    Retrieving  data for record 111 simao
    Retrieving  data for record 112 jiuquan
    Retrieving  data for record 113 zhangye
    Retrieving  data for record 114 luderitz
    Retrieving  data for record 115 binga
    Retrieving  data for record 116 santa maria
    Retrieving  data for record 117 olmos
    Retrieving  data for record 118 manuk mangkaw
    Retrieving  data for record 119 uyskoye
    Retrieving  data for record 120 saskylakh
    Retrieving  data for record 121 orangeville
    Retrieving  data for record 122 galle
    Retrieving  data for record 123 adrar
    Retrieving  data for record 124 hualmay
    Retrieving  data for record 125 primore
    Error in getting data for city primore
    error code: 404
    message: city not found
    Retrieving  data for record 126 vilhena
    Retrieving  data for record 127 richards bay
    Retrieving  data for record 128 biltine
    Retrieving  data for record 129 mikhaylovskoye
    Retrieving  data for record 130 chunskiy
    Retrieving  data for record 131 bang len
    Retrieving  data for record 132 evensk
    Retrieving  data for record 133 mocuba
    Retrieving  data for record 134 montanha
    Retrieving  data for record 135 sobinka
    Retrieving  data for record 136 leh
    Retrieving  data for record 137 allonnes
    Retrieving  data for record 138 tanete
    Retrieving  data for record 139 nayudupeta
    Retrieving  data for record 140 dunedin
    Retrieving  data for record 141 lerwick
    Retrieving  data for record 142 susanville
    Retrieving  data for record 143 castro
    Retrieving  data for record 144 bartica
    Retrieving  data for record 145 skjervoy
    Retrieving  data for record 146 ribeira grande
    Retrieving  data for record 147 tarko-sale
    Retrieving  data for record 148 northam
    Retrieving  data for record 149 goderich
    Retrieving  data for record 150 lebu
    Retrieving  data for record 151 viransehir
    Retrieving  data for record 152 zabol
    Retrieving  data for record 153 port alfred
    Retrieving  data for record 154 erhlin
    Error in getting data for city erhlin
    error code: 404
    message: city not found
    Retrieving  data for record 155 pemba
    Retrieving  data for record 156 shimoda
    Retrieving  data for record 157 san pedro
    Retrieving  data for record 158 attawapiskat
    Error in getting data for city attawapiskat
    error code: 404
    message: city not found
    Retrieving  data for record 159 svetlaya
    Retrieving  data for record 160 salvacion
    Retrieving  data for record 161 palu
    Retrieving  data for record 162 pierre
    Retrieving  data for record 163 xining
    Retrieving  data for record 164 thompson
    Retrieving  data for record 165 sao joao da barra
    Retrieving  data for record 166 gold coast
    Retrieving  data for record 167 dodge city
    Retrieving  data for record 168 mecca
    Retrieving  data for record 169 mul
    Retrieving  data for record 170 avarua
    Retrieving  data for record 171 pondicherry
    Retrieving  data for record 172 poso
    Retrieving  data for record 173 grimari
    Error in getting data for city grimari
    error code: 404
    message: city not found
    Retrieving  data for record 174 verkhnyaya khava
    Retrieving  data for record 175 sebastian
    Retrieving  data for record 176 benidorm
    Retrieving  data for record 177 cidreira
    Retrieving  data for record 178 barrow
    Retrieving  data for record 179 codrington
    Retrieving  data for record 180 nizhniy ufaley
    Retrieving  data for record 181 qinhuangdao
    Retrieving  data for record 182 aflu
    Error in getting data for city aflu
    error code: 404
    message: city not found
    Retrieving  data for record 183 oum hadjer
    Retrieving  data for record 184 coihaique
    Retrieving  data for record 185 palabuhanratu
    Error in getting data for city palabuhanratu
    error code: 404
    message: city not found
    Retrieving  data for record 186 kilindoni
    Retrieving  data for record 187 waraseoni
    Retrieving  data for record 188 antofagasta
    Retrieving  data for record 189 ron phibun
    Retrieving  data for record 190 burnie
    Retrieving  data for record 191 bargal
    Error in getting data for city bargal
    error code: 404
    message: city not found
    Retrieving  data for record 192 gisborne
    Retrieving  data for record 193 hvolsvollur
    Error in getting data for city hvolsvollur
    error code: 404
    message: city not found
    Retrieving  data for record 194 esperance
    Retrieving  data for record 195 aranos
    Retrieving  data for record 196 aklavik
    Retrieving  data for record 197 ust-nera
    Retrieving  data for record 198 angouleme
    Retrieving  data for record 199 nuevo laredo
    Retrieving  data for record 200 mashhad
    Retrieving  data for record 201 kazalinsk
    Error in getting data for city kazalinsk
    error code: 404
    message: city not found
    Retrieving  data for record 202 dongkan
    Retrieving  data for record 203 sun valley
    Retrieving  data for record 204 tukrah
    Error in getting data for city tukrah
    error code: 404
    message: city not found
    Retrieving  data for record 205 salalah
    Retrieving  data for record 206 ruteng
    Retrieving  data for record 207 strezhevoy
    Retrieving  data for record 208 yendi
    Retrieving  data for record 209 merced
    Retrieving  data for record 210 hithadhoo
    Retrieving  data for record 211 tuatapere
    Retrieving  data for record 212 umm lajj
    Retrieving  data for record 213 chaoyang
    Retrieving  data for record 214 krasnoyarskiy
    Retrieving  data for record 215 jaguarari
    Retrieving  data for record 216 longkou
    Retrieving  data for record 217 taixing
    Retrieving  data for record 218 poum
    Retrieving  data for record 219 kodinsk
    Retrieving  data for record 220 winneba
    Retrieving  data for record 221 presidencia roque saenz pena
    Retrieving  data for record 222 yaan
    Retrieving  data for record 223 wahran
    Error in getting data for city wahran
    error code: 404
    message: city not found
    Retrieving  data for record 224 provideniya
    Retrieving  data for record 225 grandview
    Retrieving  data for record 226 qurayyat
    Error in getting data for city qurayyat
    error code: 404
    message: city not found
    Retrieving  data for record 227 inta
    Retrieving  data for record 228 resistencia
    Retrieving  data for record 229 davila
    Retrieving  data for record 230 tarakan
    Retrieving  data for record 231 kristiinankaupunki
    Error in getting data for city kristiinankaupunki
    error code: 404
    message: city not found
    Retrieving  data for record 232 paitan
    Retrieving  data for record 233 dauphin
    Retrieving  data for record 234 umzimvubu
    Error in getting data for city umzimvubu
    error code: 404
    message: city not found
    Retrieving  data for record 235 iraucuba
    Retrieving  data for record 236 vaini
    Retrieving  data for record 237 acarau
    Error in getting data for city acarau
    error code: 404
    message: city not found
    Retrieving  data for record 238 tuktoyaktuk
    Retrieving  data for record 239 kirakira
    Retrieving  data for record 240 erie
    Retrieving  data for record 241 murray bridge
    Retrieving  data for record 242 nikolskoye
    Retrieving  data for record 243 illoqqortoormiut
    Error in getting data for city illoqqortoormiut
    error code: 404
    message: city not found
    Retrieving  data for record 244 kosjeric
    Retrieving  data for record 245 gao
    Retrieving  data for record 246 victoria
    Retrieving  data for record 247 luena
    Retrieving  data for record 248 bageshwar
    Retrieving  data for record 249 khatanga
    Retrieving  data for record 250 hay river
    Retrieving  data for record 251 fort saint john
    Error in getting data for city fort saint john
    error code: 404
    message: city not found
    Retrieving  data for record 252 tessalit
    Retrieving  data for record 253 mataura
    Retrieving  data for record 254 sarkand
    Retrieving  data for record 255 georgetown
    Retrieving  data for record 256 goba
    Retrieving  data for record 257 port-gentil
    Retrieving  data for record 258 weligama
    Retrieving  data for record 259 saint-philippe
    Retrieving  data for record 260 am timan
    Retrieving  data for record 261 grand river south east
    Error in getting data for city grand river south east
    error code: 404
    message: city not found
    Retrieving  data for record 262 taua
    Retrieving  data for record 263 port hawkesbury
    Retrieving  data for record 264 sentyabrskiy
    Error in getting data for city sentyabrskiy
    error code: 404
    message: city not found
    Retrieving  data for record 265 cabo san lucas
    Retrieving  data for record 266 tura
    Retrieving  data for record 267 rantauprapat
    Retrieving  data for record 268 christchurch
    Retrieving  data for record 269 garissa
    Retrieving  data for record 270 chimbote
    Retrieving  data for record 271 carnarvon
    Retrieving  data for record 272 kurara
    Retrieving  data for record 273 turayf
    Retrieving  data for record 274 san quintin
    Retrieving  data for record 275 rawson
    Retrieving  data for record 276 puerto ayora
    Retrieving  data for record 277 tonneins
    Retrieving  data for record 278 asau
    Error in getting data for city asau
    error code: 404
    message: city not found
    Retrieving  data for record 279 sidi ali
    Retrieving  data for record 280 urengoy
    Retrieving  data for record 281 san rafael
    Retrieving  data for record 282 mys shmidta
    Error in getting data for city mys shmidta
    error code: 404
    message: city not found
    Retrieving  data for record 283 avenal
    Retrieving  data for record 284 inongo
    Retrieving  data for record 285 novoleushkovskaya
    Retrieving  data for record 286 waipawa
    Retrieving  data for record 287 semey
    Retrieving  data for record 288 klyuchi
    Retrieving  data for record 289 vysokogornyy
    Retrieving  data for record 290 saint-augustin
    Retrieving  data for record 291 methoni
    Retrieving  data for record 292 hertford
    Retrieving  data for record 293 moron
    Retrieving  data for record 294 akropong
    Retrieving  data for record 295 petropavlovsk-kamchatskiy
    Retrieving  data for record 296 jiaonan
    Retrieving  data for record 297 el triunfo
    Retrieving  data for record 298 grootfontein
    Retrieving  data for record 299 kui buri
    Retrieving  data for record 300 benghazi
    Retrieving  data for record 301 chifeng
    Retrieving  data for record 302 almaznyy
    Retrieving  data for record 303 mabaruma
    Retrieving  data for record 304 grand gaube
    Retrieving  data for record 305 saint george
    Retrieving  data for record 306 barbastro
    Retrieving  data for record 307 temascalcingo
    Retrieving  data for record 308 robertson
    Retrieving  data for record 309 mount gambier
    Retrieving  data for record 310 rio claro
    Retrieving  data for record 311 punta arenas
    Retrieving  data for record 312 qaanaaq
    Retrieving  data for record 313 kaka
    Retrieving  data for record 314 raudeberg
    Retrieving  data for record 315 halalo
    Error in getting data for city halalo
    error code: 404
    message: city not found
    Retrieving  data for record 316 hilo
    Retrieving  data for record 317 karasburg
    Retrieving  data for record 318 kuala kedah
    Retrieving  data for record 319 byron bay
    Retrieving  data for record 320 hasaki
    Retrieving  data for record 321 hailar
    Retrieving  data for record 322 ewa beach
    Retrieving  data for record 323 port macquarie
    Retrieving  data for record 324 chabahar
    Retrieving  data for record 325 cape coast
    Retrieving  data for record 326 brae
    Retrieving  data for record 327 ginda
    Retrieving  data for record 328 bokspits
    Error in getting data for city bokspits
    error code: 404
    message: city not found
    Retrieving  data for record 329 carutapera
    Retrieving  data for record 330 ouricuri
    Retrieving  data for record 331 ndele
    Error in getting data for city ndele
    error code: 404
    message: city not found
    Retrieving  data for record 332 filadelfia
    Retrieving  data for record 333 gobabis
    Retrieving  data for record 334 tawkar
    Error in getting data for city tawkar
    error code: 404
    message: city not found
    Retrieving  data for record 335 fuyang
    Retrieving  data for record 336 lexington
    Retrieving  data for record 337 faya
    Retrieving  data for record 338 uniontown
    Retrieving  data for record 339 charleston
    Retrieving  data for record 340 nagai
    Retrieving  data for record 341 witu
    Retrieving  data for record 342 florence
    Retrieving  data for record 343 norman wells
    Retrieving  data for record 344 rosarito
    Retrieving  data for record 345 anadyr
    Retrieving  data for record 346 toliary
    Error in getting data for city toliary
    error code: 404
    message: city not found
    Retrieving  data for record 347 matara
    Retrieving  data for record 348 bodden town
    Retrieving  data for record 349 kidal
    Retrieving  data for record 350 channel-port aux basques
    Retrieving  data for record 351 apaxtla
    Error in getting data for city apaxtla
    error code: 404
    message: city not found
    Retrieving  data for record 352 gunjur
    Retrieving  data for record 353 beaverlodge
    Retrieving  data for record 354 gangotri
    Error in getting data for city gangotri
    error code: 404
    message: city not found
    Retrieving  data for record 355 mitsukaido
    Retrieving  data for record 356 vila franca do campo
    Retrieving  data for record 357 moose factory
    Retrieving  data for record 358 ruatoria
    Error in getting data for city ruatoria
    error code: 404
    message: city not found
    Retrieving  data for record 359 pawayan
    Retrieving  data for record 360 samusu
    Error in getting data for city samusu
    error code: 404
    message: city not found
    Retrieving  data for record 361 los llanos de aridane
    Retrieving  data for record 362 abilene
    Retrieving  data for record 363 russell
    Retrieving  data for record 364 tateyama
    Retrieving  data for record 365 aventura
    Retrieving  data for record 366 yunjinghong
    Error in getting data for city yunjinghong
    error code: 404
    message: city not found
    Retrieving  data for record 367 skagastrond
    Error in getting data for city skagastrond
    error code: 404
    message: city not found
    Retrieving  data for record 368 dombarovskiy
    Retrieving  data for record 369 wulanhaote
    Error in getting data for city wulanhaote
    error code: 404
    message: city not found
    Retrieving  data for record 370 doctor arroyo
    Retrieving  data for record 371 haines junction
    Retrieving  data for record 372 the valley
    Retrieving  data for record 373 tshikapa
    Retrieving  data for record 374 woodward
    Retrieving  data for record 375 sitka
    Retrieving  data for record 376 bogorodskoye
    Retrieving  data for record 377 boa vista
    Retrieving  data for record 378 ilulissat
    Retrieving  data for record 379 waingapu
    Retrieving  data for record 380 acapulco
    Retrieving  data for record 381 dawson creek
    Retrieving  data for record 382 tungkang
    Error in getting data for city tungkang
    error code: 404
    message: city not found
    Retrieving  data for record 383 khanu woralaksaburi
    Retrieving  data for record 384 scarborough
    Retrieving  data for record 385 rikitea
    Retrieving  data for record 386 boende
    Retrieving  data for record 387 dikson
    Retrieving  data for record 388 north platte
    Retrieving  data for record 389 shalakusha
    Retrieving  data for record 390 peachland
    Retrieving  data for record 391 vestmannaeyjar
    Retrieving  data for record 392 broken hill
    Retrieving  data for record 393 kpandae
    Retrieving  data for record 394 sinait
    Retrieving  data for record 395 pandan niog
    Retrieving  data for record 396 ancud
    Retrieving  data for record 397 ngunguru
    Retrieving  data for record 398 manaus
    Retrieving  data for record 399 ormond beach
    Retrieving  data for record 400 deputatskiy
    Retrieving  data for record 401 takoradi
    Retrieving  data for record 402 polunochnoye
    Retrieving  data for record 403 alamor
    Retrieving  data for record 404 abomsa
    Error in getting data for city abomsa
    error code: 404
    message: city not found
    Retrieving  data for record 405 rocha
    Retrieving  data for record 406 kharovsk
    Retrieving  data for record 407 redmond
    Retrieving  data for record 408 volchansk
    Retrieving  data for record 409 merauke
    Retrieving  data for record 410 east wenatchee bench
    Retrieving  data for record 411 ponta do sol
    Retrieving  data for record 412 trabzon
    Retrieving  data for record 413 adwa
    Retrieving  data for record 414 kodiak
    Retrieving  data for record 415 chiang rai
    Retrieving  data for record 416 tenno
    Retrieving  data for record 417 borba
    Retrieving  data for record 418 te anau
    Retrieving  data for record 419 fort nelson
    Retrieving  data for record 420 cap malheureux
    Retrieving  data for record 421 dori
    Retrieving  data for record 422 bridlington
    Retrieving  data for record 423 ko samui
    Retrieving  data for record 424 addanki
    Retrieving  data for record 425 kargasok
    Retrieving  data for record 426 bengkulu
    Error in getting data for city bengkulu
    error code: 404
    message: city not found
    Retrieving  data for record 427 palana
    Retrieving  data for record 428 payakumbuh
    Retrieving  data for record 429 longyearbyen
    Retrieving  data for record 430 den chai
    Retrieving  data for record 431 fortuna
    Retrieving  data for record 432 nelson bay
    Retrieving  data for record 433 narsaq
    Retrieving  data for record 434 isla vista
    Retrieving  data for record 435 portobelo
    Retrieving  data for record 436 khani
    Retrieving  data for record 437 panzhihua
    Retrieving  data for record 438 whitley bay
    Retrieving  data for record 439 ubinskoye
    Retrieving  data for record 440 hazorasp
    Retrieving  data for record 441 valvedditturai
    Retrieving  data for record 442 ergani
    Retrieving  data for record 443 port elizabeth
    Retrieving  data for record 444 mahebourg
    Retrieving  data for record 445 margate
    Retrieving  data for record 446 wajir
    Retrieving  data for record 447 uvalde
    Retrieving  data for record 448 egvekinot
    Retrieving  data for record 449 tazovskiy
    Retrieving  data for record 450 porto novo
    Retrieving  data for record 451 busselton
    Retrieving  data for record 452 puerto escondido
    Retrieving  data for record 453 atuona
    Retrieving  data for record 454 pisco
    Retrieving  data for record 455 aripuana
    Retrieving  data for record 456 bredasdorp
    Retrieving  data for record 457 tulun
    Retrieving  data for record 458 brandon
    Retrieving  data for record 459 shache
    Retrieving  data for record 460 kamiiso
    Retrieving  data for record 461 mayo
    Retrieving  data for record 462 portland
    Retrieving  data for record 463 beringovskiy
    Retrieving  data for record 464 port hueneme
    Retrieving  data for record 465 esmeraldas
    Retrieving  data for record 466 pankrushikha
    Retrieving  data for record 467 arraial do cabo
    Retrieving  data for record 468 rundu
    Retrieving  data for record 469 burriana
    Retrieving  data for record 470 mnogovershinnyy
    Retrieving  data for record 471 kedrovyy
    Retrieving  data for record 472 nhulunbuy
    Retrieving  data for record 473 singkang
    Retrieving  data for record 474 mar del plata
    Retrieving  data for record 475 lumut
    Retrieving  data for record 476 awjilah
    Retrieving  data for record 477 mangit
    Retrieving  data for record 478 barentsburg
    Error in getting data for city barentsburg
    error code: 404
    message: city not found
    Retrieving  data for record 479 beloha
    Retrieving  data for record 480 san andres
    Retrieving  data for record 481 isangel
    Retrieving  data for record 482 zhigansk
    Retrieving  data for record 483 devils lake
    Retrieving  data for record 484 honiara
    Retrieving  data for record 485 solnechnyy
    Retrieving  data for record 486 la palma
    Retrieving  data for record 487 the pas
    Retrieving  data for record 488 pozo colorado
    Retrieving  data for record 489 anuradhapura
    Retrieving  data for record 490 dakar
    Retrieving  data for record 491 labuhan
    Retrieving  data for record 492 armacao dos buzios
    Error in getting data for city armacao dos buzios
    error code: 404
    message: city not found
    Retrieving  data for record 493 kaitangata
    Retrieving  data for record 494 zharkent
    Retrieving  data for record 495 milkovo
    Retrieving  data for record 496 maarianhamina
    Error in getting data for city maarianhamina
    error code: 404
    message: city not found
    Retrieving  data for record 497 bismarck
    Retrieving  data for record 498 saldanha
    Retrieving  data for record 499 dingle
    Retrieving  data for record 500 iqaluit
    Retrieving  data for record 501 cape town
    Retrieving  data for record 502 emba
    Retrieving  data for record 503 nouadhibou
    Retrieving  data for record 504 serra
    Retrieving  data for record 505 skelleftea
    Retrieving  data for record 506 mahbubabad
    Retrieving  data for record 507 black river
    Retrieving  data for record 508 wieliczka
    Retrieving  data for record 509 east london
    Retrieving  data for record 510 new norfolk
    Retrieving  data for record 511 itarantim
    Retrieving  data for record 512 umea
    Retrieving  data for record 513 naze
    Retrieving  data for record 514 kapaa
    Retrieving  data for record 515 sakakah
    Error in getting data for city sakakah
    error code: 404
    message: city not found
    Retrieving  data for record 516 tasiilaq
    Retrieving  data for record 517 viedma
    Retrieving  data for record 518 sur
    Retrieving  data for record 519 airai
    Retrieving  data for record 520 lowicz
    Retrieving  data for record 521 peterhead
    Retrieving  data for record 522 hobart
    Retrieving  data for record 523 kodino
    Retrieving  data for record 524 faanui
    Retrieving  data for record 525 taybad
    Retrieving  data for record 526 corralillo
    Retrieving  data for record 527 mount isa
    Retrieving  data for record 528 belushya guba
    Error in getting data for city belushya guba
    error code: 404
    message: city not found
    Retrieving  data for record 529 ostrovnoy
    Retrieving  data for record 530 verkhnevilyuysk
    Retrieving  data for record 531 korablino
    Retrieving  data for record 532 amderma
    Error in getting data for city amderma
    error code: 404
    message: city not found
    Retrieving  data for record 533 saint-francois
    Retrieving  data for record 534 tecoanapa
    Retrieving  data for record 535 albany
    Retrieving  data for record 536 ayagoz
    Retrieving  data for record 537 cochrane
    Retrieving  data for record 538 vernon
    Retrieving  data for record 539 chicama
    Retrieving  data for record 540 simbahan
    Retrieving  data for record 541 nanortalik
    Retrieving  data for record 542 kieta
    Retrieving  data for record 543 high point
    Retrieving  data for record 544 cherskiy
    Retrieving  data for record 545 dali
    Retrieving  data for record 546 guarare
    Retrieving  data for record 547 roald
    Retrieving  data for record 548 padang
    Retrieving  data for record 549 pawai
    Retrieving  data for record 550 leningradskiy
    Retrieving  data for record 551 mitrofanovka
    Retrieving  data for record 552 hamilton
    Retrieving  data for record 553 yellowknife
    Retrieving  data for record 554 fernandez
    Retrieving  data for record 555 manicaragua
    {'base': 'stations',
     'clouds': {'all': 0},
     'cod': 200,
     'coord': {'lat': 22.14, 'lon': -79.97},
     'dt': 1529582340,
     'id': 3547976,
     'main': {'humidity': 94,
              'pressure': 1017,
              'temp': 23.49,
              'temp_max': 24,
              'temp_min': 23},
     'name': 'Manicaragua',
     'sys': {'country': 'CU',
             'id': 4089,
             'message': 0.0037,
             'sunrise': 1529577429,
             'sunset': 1529625990,
             'type': 1},
     'weather': [{'description': 'clear sky',
                  'icon': '01d',
                  'id': 800,
                  'main': 'Clear'}],
     'wind': {'deg': 110, 'speed': 2.1}}
    Data Retrieval Complete....
    ---------------------------------------------------------
    Number of cities weather data  not found: 52
    


```python
print(len(citylist))
print(len(cloudiness))
print(len(tempmax))
print(len(humidity))
print(len(lat))
```

    503
    503
    503
    503
    503
    


```python
#store results into a dictionary and convert to a dataframe. 
weatherdict=dict()
weatherdict={"City":citylist,"Cloudiness":cloudiness,"Country_code":cnycode,"Date":date,
             "Humidity":humidity,"Latitude":lat,"Longitude":long,"Max_temp":tempmax,
             "Wind_speed":windspeed}
#print(len(weatherdict))
weather_df = pd.DataFrame(weatherdict)
weather_df.tail(10)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country_code</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Max_temp</th>
      <th>Wind_speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>493</th>
      <td>Guarare</td>
      <td>20</td>
      <td>PA</td>
      <td>1529585788</td>
      <td>100</td>
      <td>7.82</td>
      <td>-80.28</td>
      <td>22.63</td>
      <td>1.51</td>
    </tr>
    <tr>
      <th>494</th>
      <td>Roald</td>
      <td>75</td>
      <td>NO</td>
      <td>1529583600</td>
      <td>93</td>
      <td>62.58</td>
      <td>6.12</td>
      <td>10.00</td>
      <td>5.70</td>
    </tr>
    <tr>
      <th>495</th>
      <td>Padang</td>
      <td>56</td>
      <td>ID</td>
      <td>1529585788</td>
      <td>100</td>
      <td>-0.92</td>
      <td>100.36</td>
      <td>29.08</td>
      <td>2.06</td>
    </tr>
    <tr>
      <th>496</th>
      <td>Pawai</td>
      <td>44</td>
      <td>IN</td>
      <td>1529585788</td>
      <td>45</td>
      <td>24.27</td>
      <td>80.17</td>
      <td>35.68</td>
      <td>1.26</td>
    </tr>
    <tr>
      <th>497</th>
      <td>Leningradskiy</td>
      <td>24</td>
      <td>RU</td>
      <td>1529585788</td>
      <td>92</td>
      <td>69.38</td>
      <td>178.42</td>
      <td>-0.48</td>
      <td>6.06</td>
    </tr>
    <tr>
      <th>498</th>
      <td>Mitrofanovka</td>
      <td>8</td>
      <td>UA</td>
      <td>1529585788</td>
      <td>53</td>
      <td>45.45</td>
      <td>34.68</td>
      <td>30.68</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Hamilton</td>
      <td>20</td>
      <td>CA</td>
      <td>1529582400</td>
      <td>77</td>
      <td>43.26</td>
      <td>-79.87</td>
      <td>18.00</td>
      <td>6.20</td>
    </tr>
    <tr>
      <th>500</th>
      <td>Yellowknife</td>
      <td>75</td>
      <td>CA</td>
      <td>1529582400</td>
      <td>72</td>
      <td>62.45</td>
      <td>-114.38</td>
      <td>17.00</td>
      <td>6.70</td>
    </tr>
    <tr>
      <th>501</th>
      <td>Fernandez</td>
      <td>56</td>
      <td>PH</td>
      <td>1529585789</td>
      <td>100</td>
      <td>11.38</td>
      <td>122.76</td>
      <td>24.13</td>
      <td>1.66</td>
    </tr>
    <tr>
      <th>502</th>
      <td>Manicaragua</td>
      <td>0</td>
      <td>CU</td>
      <td>1529582340</td>
      <td>94</td>
      <td>22.14</td>
      <td>-79.97</td>
      <td>24.00</td>
      <td>2.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Save weather data in a csv file for future reference and use. 
weather_df.to_csv("weatherdata.csv",index=False,header=True)
weather_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 503 entries, 0 to 502
    Data columns (total 9 columns):
    City            503 non-null object
    Cloudiness      503 non-null int64
    Country_code    503 non-null object
    Date            503 non-null int64
    Humidity        503 non-null int64
    Latitude        503 non-null float64
    Longitude       503 non-null float64
    Max_temp        503 non-null float64
    Wind_speed      503 non-null float64
    dtypes: float64(4), int64(3), object(2)
    memory usage: 35.4+ KB
    


```python
#Import dependencies for plotting.
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
x_axis=weather_df["Latitude"]
y_axis_maxtemp=weather_df["Max_temp"]
y_axis_humidity=weather_df["Humidity"]
y_axis_cloudiness = weather_df["Cloudiness"]
y_axis_Windspeed = weather_df["Wind_speed"]
```


```python
#Review cities that have temperature greater than 28 deg C.
weather_df.loc[weather_df["Max_temp"] >= 38]
#weather_df_sortedbytemp = weather_df.sort("Max_temp",axis=1,ascending=False,inplace=False)
#weather_df_sortedbytemp.head(10)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country_code</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Max_temp</th>
      <th>Wind_speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>43</th>
      <td>Iranshahr</td>
      <td>20</td>
      <td>IR</td>
      <td>1529582400</td>
      <td>8</td>
      <td>27.21</td>
      <td>60.69</td>
      <td>46.00</td>
      <td>4.10</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Adrar</td>
      <td>0</td>
      <td>DZ</td>
      <td>1529582400</td>
      <td>14</td>
      <td>27.87</td>
      <td>-0.29</td>
      <td>40.00</td>
      <td>10.80</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Zabol</td>
      <td>0</td>
      <td>IR</td>
      <td>1529582400</td>
      <td>9</td>
      <td>31.03</td>
      <td>61.49</td>
      <td>42.00</td>
      <td>9.80</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Mecca</td>
      <td>0</td>
      <td>SA</td>
      <td>1529582400</td>
      <td>24</td>
      <td>21.43</td>
      <td>39.83</td>
      <td>45.00</td>
      <td>2.10</td>
    </tr>
    <tr>
      <th>218</th>
      <td>Gao</td>
      <td>0</td>
      <td>ML</td>
      <td>1529585742</td>
      <td>28</td>
      <td>16.28</td>
      <td>-0.04</td>
      <td>40.18</td>
      <td>4.26</td>
    </tr>
    <tr>
      <th>224</th>
      <td>Tessalit</td>
      <td>0</td>
      <td>ML</td>
      <td>1529585743</td>
      <td>11</td>
      <td>20.20</td>
      <td>1.01</td>
      <td>41.98</td>
      <td>6.91</td>
    </tr>
    <tr>
      <th>242</th>
      <td>Kurara</td>
      <td>0</td>
      <td>IN</td>
      <td>1529585746</td>
      <td>36</td>
      <td>25.98</td>
      <td>79.99</td>
      <td>39.73</td>
      <td>1.96</td>
    </tr>
    <tr>
      <th>312</th>
      <td>Kidal</td>
      <td>0</td>
      <td>ML</td>
      <td>1529585759</td>
      <td>17</td>
      <td>18.44</td>
      <td>1.41</td>
      <td>41.53</td>
      <td>2.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Plot Latitude vs maximum temp(C)
sns.regplot(x_axis, y_axis_maxtemp, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label="Latitude vs Max temperature(C)", 
            color=None,marker='o', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Max temperature(C) Date: 06/21/2018 ")
plt.grid()
plt.xlim(-65,85)
plt.ylim(-10,50)
plt.ylabel("Maximum Temp in C")
plt.savefig("latvsMaxtemp.png")
```


![png](output_11_0.png)



```python
#Plot of latitude vs Humidity
sns.regplot(x_axis, y_axis_humidity, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=False, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color="g", 
            marker='o', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Humidity, Date: 06/21/2018 ")
plt.xlim(-65,85)
plt.ylim(-0,100)
plt.ylabel("Humidity % ")
plt.savefig("latvshumidity.png")
```


![png](output_12_0.png)



```python
#Plot of latitude vs Cloudiness
sns.regplot(x_axis, y_axis_cloudiness, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=False, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color="grey", 
            marker='o', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Cloudiness, Date: 06/21/2018 ")
plt.xlim(-65,85)
plt.ylim(-5,100)
plt.ylabel("Cloudiness ")
plt.savefig("latvscloudiness.png")
```


![png](output_13_0.png)



```python
#Latitude vs windspeed
sns.regplot(x_axis, y_axis_Windspeed, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=False, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color="cyan", 
            marker='+', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Wind speed, Date: 06/21/2018 ")
plt.grid()
plt.xlim(-65,85)
plt.ylim(-0,20)
plt.ylabel("Wind Speed ")
plt.savefig("latvswindspeed.png")
```


![png](output_14_0.png)

