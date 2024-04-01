import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Veri setini yükle
data = pd.read_excel('kayseri_kaza_verileri.xlsx')

# Gereksiz sütunları çıkar (örneğin, ID sütunu gibi)
data = data.drop(['ID'], axis=1)

# Kategorik sütunları kodlayın (gerekirse)
# Örneğin, pd.get_dummies() veya LabelEncoder() gibi yöntemler kullanılabilir

# Sayısal sütunları standartlaştırın
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# K-means modelini oluştur
kmeans = KMeans(n_clusters=3, random_state=42)

# Modeli eğitin
kmeans.fit(scaled_data)

# Küme merkezlerini al
cluster_centers = kmeans.cluster_centers_

# Her gözlem için küme tahminlerini al
cluster_labels = kmeans.labels_

# Küme tahminlerini veri setine ekleyin
data['Cluster'] = cluster_labels

# Kaza ciddiyetini her küme için hesaplayın (örneğin, ortalama)
cluster_impact = data.groupby('Cluster')['Kaza Ciddiyet Seviyesi'].mean()

# Sonuçları görüntüle
print(cluster_impact)

# Kümeleme sonuçlarını görselleştirin (örneğin, Kaza Saati ve Kaza Ciddiyeti)
plt.figure(figsize=(10, 6))
plt.scatter(data['KAZA SAAT'], data['Kaza Ciddiyet Seviyesi'], c=cluster_labels, cmap='viridis')
plt.xlabel('KAZA SAAT')
plt.ylabel('Kaza Ciddiyet Seviyesi')
plt.title('K-means Kümeleme Sonuçları')
plt.colorbar(label='Küme')
plt.show()
