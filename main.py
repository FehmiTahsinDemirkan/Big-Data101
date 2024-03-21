import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Veri setini oku
data = pd.read_excel('kayseri_kaza_verileri.xlsx')

# Veri setinin başını göster
print("Veri setinin başı:\n", data.head())

# Keşifsel veri analizi işlemleri
# Örnek olarak veri setinin şekli, özet istatistikler, eksik değerler kontrol edilebilir
print("\nVeri setinin şekli:", data.shape)
print("\nVeri setinin özet istatistikleri:\n", data.describe())
print("\nEksik değerlerin sayısı:\n", data.isnull().sum())

# # Kaza ciddiyetini hesaplamak için k-means algoritması
# X = data[['ENLEM', 'BOYLAM']]  # Veri setinden ilgili öznitelikleri seç
# kmeans = KMeans(n_clusters=3, random_state=42)  # 3 küme için k-means modeli oluştur
# data['Ciddiyet_Kumesi'] = kmeans.fit_predict(X)  # Kümeleme işlemini gerçekleştir

# Kaza ciddiyetini görselleştir
# plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=data['Ciddiyet_Kumesi'], cmap='viridis')
# plt.title('Kaza Ciddiyeti Kümeleme')
# plt.xlabel('Enlem')
# plt.ylabel('Boylam')
# plt.colorbar(label='Küme')
# plt.show()

# Kazaya karışan araç sayısına bağlı olarak kazaları kümeleme
# Bu kısımda k-means algoritması kullanılabilir veya başka bir kümeleme algoritması tercih edilebilir
# Örneğin, kazaya karışan araç sayısına göre veriyi kümelendirebilir ve bu küme sayısını 3 veya 5 olarak seçebilirsiniz
