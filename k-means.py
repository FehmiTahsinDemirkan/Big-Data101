import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Veri setini yükle
try:
    # Dosya yolunu güncelle
    file_path = r'C:\Users\fehmi\PycharmProjects\Big_Data101\kayseri_kaza_verileri.xlsx'
    accident_data = pd.read_excel(file_path)
    print("Veri seti başarıyla yüklendi.")
except FileNotFoundError:
    print("Belirtilen dosya bulunamadı.")
    exit()
except Exception as e:
    print("Bir hata oluştu:", e)
    exit()

# Ön işleme için eksik verileri median ile doldurma
imputer = SimpleImputer(strategy='median')

# İlgili sütunları seçme ve eksik verileri doldurma
selected_columns = accident_data[['Kaza Ciddiyet Seviyesi', 'AY', 'MAHALLE yoğunluğu']]
selected_columns_imputed = imputer.fit_transform(selected_columns)

# Ölçeklendirme
scaler = StandardScaler()
scaled_features = scaler.fit_transform(selected_columns_imputed)

# K-means algoritması 3 küme ile uygulanıyor
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

# Küme merkezlerini ve küme etiketlerini veri setine ekliyoruz
accident_data['Cluster'] = clusters
cluster_centers = kmeans.cluster_centers_

# İlk beş sıradaki verileri ve küme merkezlerini gösterelim
print("Veri setinin ilk beş sırası:\n", accident_data.head())
print("\nKüme merkezleri:\n", cluster_centers)
