# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('kayseri_kaza_verileri.xlsx')

# info() her sütundaki kayıt sayısı, boş veya boş olmayan veriler, Veri türü,
# veri kümesinin bellek kullanımı dahil olmak üzere veri türünü ve verilerle ilgili bilgileri anlamaya yardımcı olur
# print(data.info())

# nunique() her sütundaki birkaç benzersiz değere ve veri açıklamasına dayanarak , verilerdeki sürekli ve kategorik sütunları tanımlayabiliriz.
# Tekrarlanan veriler daha fazla analize dayalı olarak işlenebilir veya kaldırılabilir
# print(data.nunique())

# isnull(), verilerdeki boş değerleri tanımlamak için tüm ön işleme adımlarında yaygın olarak kullanılmaktadır
# data.isnull().sum() her sütundaki eksik kayıtların sayısını bulmak için kullanılır
# print(data.isnull().sum())

# Aşağıdaki kod, her sütundaki eksik değerlerin yüzdesini hesaplamaya yardımcı olur
# print((data.isnull().sum()/(len(data)))*100)

# Remove OLU SAYISI column from data
# data = data.drop(['OLU SAYISI'], axis = 1)
# print(data.info())

# Some names of the variables are not relevant and not easy to understand. Some data may have data entry errors,
# and some variables may need data type conversion. We need to fix this issue in the data.
# print(data.AY.unique())
# print(data.AY.nunique())

#describe()– Provide a statistics summary of data belonging to numerical datatype such as int, float
print(data.describe().T)
