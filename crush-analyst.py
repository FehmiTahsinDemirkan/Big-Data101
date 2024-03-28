import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Veri setini yükle
try:
    file_path = r'C:\Users\fehmi\PycharmProjects\Big_Data101\kayseri_kaza_verileri.xlsx'
    accident_data = pd.read_excel(file_path)
    print("Veri seti başarıyla yüklendi.")
except FileNotFoundError:
    print("Belirtilen dosya bulunamadı.")
    exit()
except Exception as e:
    print("Bir hata oluştu:", e)
    exit()

# Kazaya karışan araç sayısı sütununu seçme
vehicle_count = accident_data[['TASIT SAYISI']]

# Eksik değerleri doldurma
imputer = SimpleImputer(strategy='median')
vehicle_count_imputed = imputer.fit_transform(vehicle_count)

# Ölçeklendirme
scaler = StandardScaler()
scaled_vehicle_count = scaler.fit_transform(vehicle_count_imputed)

# K-means algoritması
num_clusters = 3  # veya 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Modeli veriye uygula ve kümeleme yap
clusters = kmeans.fit_predict(scaled_vehicle_count)

# Küme merkezlerini al
cluster_centers = kmeans.cluster_centers_

# Sonuçları veri setine ekle
accident_data['Cluster'] = clusters

# Kümeleme sonuçlarını ve küme merkezlerini yazdır
print(f"{num_clusters} kümeleme için elde edilen küme merkezleri:\n{cluster_centers}")
print(f"\nKazaların {num_clusters} kümeleme sonuçları:\n{accident_data.head()}")