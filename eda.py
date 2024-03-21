# eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    """Veri setini yükler ve ilk beş satırı döndürür."""
    data = pd.read_excel(filepath)
    return data.head()


def get_basic_info(data):
    """Veri seti hakkında temel bilgiler sağlar."""
    info = data.info()
    return info


def get_missing_values(data):
    """Veri setindeki eksik değerlerin sayısını döndürür."""
    missing_values = data.isnull().sum()
    return missing_values


def get_statistical_summary(data):
    """Veri setinin istatistiksel özetini döndürür."""
    summary = data.describe()
    return summary


def visualize_data(data, column):
    """Belirtilen sütun için veri dağılımını görselleştirir."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()


# Modülün doğrudan çalıştırılmasını engellemek için bu kontrolü ekleyebiliriz.
if __name__ == "__main__":
    print(get_basic_info(load_data('kayseri_kaza_verileri.xlsx')))
    print("******************************************************")
    print(get_missing_values(load_data('kayseri_kaza_verileri.xlsx')))
    print("******************************************************")
    print(get_missing_values(load_data('kayseri_kaza_verileri.xlsx')))
    print("******************************************************")
    print(visualize_data(load_data('kayseri_kaza_verileri.xlsx'),'AY'))

    print("This module is intended to be imported rather than run directly.")
