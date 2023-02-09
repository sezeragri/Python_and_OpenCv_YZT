
# %% giris
import inline as inline
import matplotlib as matplotlib

print("Hello world!")

# ½½ Degiskenler

# Listeler

"""
- bileşik veri türüdür ve çok yönlüdür
- [1 , "a" , 1.0] 
- burada veri tipini yazmaya gerek yok 
-farklı veri tiplerini içerisinde barındırablilir

"""

liste = [ 1,2,3,4,5,6]
print(type(liste))

hafta_günleri = ["pazartesi", "Salı", "Carsamba", "persembe","cuma","cumartesi","pazar"]

print(hafta_günleri[0])
print(hafta_günleri[3])
# boyut
print(len(hafta_günleri))


print(len(hafta_günleri)-3)

print(hafta_günleri[1:3])  # bir dahil fakat 3 dahil değil 3 e kadar olan dahil

sayi_listesi  = [1,2,3,4,5,6]

sayi_listesi.append(7)
print(sayi_listesi)
#eleman cıkarma

sayi_listesi.remove(4)
print(sayi_listesi)

# listeyi ters cevir
sayi_listesi.reverse()
print(sayi_listesi)

print(sayi_listesi.reverse())  # none degerini verir


new_liste = [1,3,2,5,4,67,0]

new_liste.sort()  # kücükten büyüğe sıralama işlemi yaptım
print(new_liste)


# Tuple

"""
-sıralı ve değiştiirlemez bir veri tipidir 
-(1,2,3)

"""

tuple_veri = (1,2,3,3,4,5,6)

#ilk eleman
print(tuple_veri[0])

#2. indexten sonraki elemanlarını yazınız

print(tuple_veri[2:])


# count eleman

print(tuple_veri.count(3))

tuple_xyz = (1,2,3)

x,y,z = tuple_xyz
print(x)
print(x,y,z)


# Deque
"""
- listelere cok benzerler  bilgisayar bilinümlerinde cıft uclu  kuyruk olarak adlandırılır 

-yani aslında burada boyutunu belirtmek lazım 

- yani önden veya arkadan elemanların eklendiği yada önden vya arkadan elenaların cıkarıldıgı bır veri yapsısıdır 

"""


from collections import deque

dq = deque(maxlen=3)

print(len(dq))


# şu an dque nin içi boş ben aeleman eklemek istiyorum

dq.append(1)
print(dq)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq)



"""
-matrisler için hesaplama kolaylığı sağlar 
"""

import numpy as np


# 1*15 boyutunda bir array - dizi

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(dizi)

print(dizi.shape)  # arrayın boyutu

# 2 boyutlu bir matris haline getirelim

dizi2 = dizi.reshape(3,5)
print("Şekil: ", dizi2.shape)
print("Boyut: ", dizi2.ndim)
print("Veri tipi : ",dizi2.dtype.name)
print("Boy : ", dizi2.size)

# array type

print("Type  :" , type(dizi2))

# 2 boytulu array
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)

# sıfırlardan oluşan bir array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

# birlerden oluşan bir array
birler_dizi = np.ones((3,4))
print(birler_dizi)

# boş array
bos_dizi = np.empty((3,4))
print(bos_dizi)

# arrange kavramı (x,y ,basamak)
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)

# linspace (x,y , basamak)  burada x y dahil
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)

# float array yaratmak istiyorum
float_array = np.float32([[1,2],[3,4]])
print(float_array)


# matematiksel işlemler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)


# dizi elemanı toplama
print(np.sum(a))

# dizi max deger
print(np.max(a))

# dizi min deger
print(np.min(a))

# dizi ort
print(np.mean(a))

# median ortalama
print(np.median(a))

# rastgele sayı uretme [0,1] arasında sürekli dağılım 3*3 bir matris

ratgele_dizi = np.random.random((3,3))
print(ratgele_dizi)

# index
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])
# ilk dört eleman
print(dizi[0:4]) # 0 dahil 4 dahil değil

#
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1.satir ve 1. sütunda bulunan elemanı yazduruıcaz
print(dizi2D[1,1])

# 1. sütun ve tüm satırlar
print(dizi2D[:,1])

# satır 1 sütun 1,2,3
print(dizi2D[1,1:4])

# dizinin son satır tüm sütunlar
print(dizi2D[-1,:])

#
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

# diziiyi vektör yapalım
vektor = dizi2D.ravel()
print(vektor)

# vektor içinde maksimum sayının indexini bulalım
maksimum_sayinin_indeksi = vektor.argmax()
print(maksimum_sayinin_indeksi)

# Pandas

"""
- Hızlı esnek ve güçlü 

"""

import pandas as pd

data = np.random.random((4,3))
print(data)
data_frame = pd.DataFrame(data)
print(data_frame)

type(data_frame)
print(type(data_frame))

new_data_frame = pd.DataFrame(data, index=["sezer", "ogras", "cahit","mehmet"],columns=["yas","boy","kilo"])

print(new_data_frame)


print(new_data_frame.describe())
print(new_data_frame["yas"])

# sütun ekleme
new_data_frame["sehir"] = ["Ankara","Agrı","Istanbul","Bursa"]
print(new_data_frame)

# yas sütununu alalım loc  location kısaltması
print(new_data_frame.loc[:,"yas"])

# yaş sütunu icinde bulunan ilk üc örneği alalım yani üç satır
print(new_data_frame.loc[:,"boy"])


import matplotlib.pyplot as plt
from matplotlib.image import imread


yasListesi = [10,20,30,40,50,60,70,75]

kiloLİstesi = [20,60,80,85,86,87,70,90,95,90]


numpyYasListesi = np.array(yasListesi)
nupyKiloListesi = np.array(kiloLİstesi)

"""
plt.plot(numpyYasListesi,nupyKiloListesi,"y")
plt.xlabel("Yas")
plt.ylabel("Kilo")
plt.title("Kilonun yaşa göre değişim grafiği")

print(plt.xlabel)

print(plt.plot(numpyYasListesi,nupyKiloListesi,"y"))

"""


numpydizisi1 = np.linspace(0.10,20)

print(numpydizisi1)

numpydizisi2 = numpydizisi1 ** 3
print(numpydizisi2)


print(plt.plot(numpydizisi1,numpydizisi2,"b*-"))
"""
# OS
import os

print(os.name)

currentDir = os.getcwd()
print(currentDir)
# new folder
folder_name = "new_folder_sezer1"
os.mkdir(folder_name)

new_folder_name = "new_folder_2_sezer1"
os.rename(folder_name,new_folder_name)

os.chdir(currentDir+"//"+new_folder_name)
print(os.getcwd())

os.chdir(currentDir)
print(os.getcwd())
files = os.listdir()
# sadece python dosyası istiyorsan
for f in  files :
    if f.endswith(".py"):
        print(f)
os.rmdir(new_folder_name)
for i in os.walk(currentDir):
    print(i)

# aradığımız dosya ver mı yok mu
os.path.exists("pythohdfıun_hatırlatma.py")
"""
"""

"""
# GÖRÜNTÜ İŞLEME

import cv2 as cv

# içe aktarma
img = cv.imread("uu_logo.png",0)  # -> buradaki 0 resmin gray tonda olmasınnı sağlıyor

# görselleştirme

cv.imshow("Ilk Resim",img)

cv.waitKey(0)  # -> klavtyeden koöut bekliyor
cv.imwrite("uludag_gray.png",img)


















